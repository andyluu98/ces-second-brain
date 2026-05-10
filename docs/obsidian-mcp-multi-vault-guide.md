# Hướng dẫn: Kết nối Claude Desktop với nhiều vault Obsidian qua MCP

> **Dành cho:** Học viên cài đặt Claude + Obsidian trên Windows hoặc macOS  
> **Mục tiêu:** Chạy được nhiều vault Obsidian song song trong Claude Desktop  
> **Đúc kết từ:** Lỗi thực tế khi debug trực tiếp

---

## Mục lục

1. [Yêu cầu](#1-yêu-cầu)
2. [Cấu hình Obsidian — Local REST API](#2-cấu-hình-obsidian--local-rest-api)
3. [Cấu hình Claude Desktop](#3-cấu-hình-claude-desktop)
4. [Patch bắt buộc cho mcp-obsidian](#4-patch-bắt-buộc-cho-mcp-obsidian)
5. [Lỗi thường gặp & cách fix](#5-lỗi-thường-gặp--cách-fix)
6. [Checklist xác nhận](#6-checklist-xác-nhận)

---

## 1. Yêu cầu

| Thành phần | Ghi chú |
|-----------|---------|
| Claude Desktop | Bản mới nhất |
| Obsidian | Mỗi vault mở trong 1 cửa sổ riêng |
| Plugin **Local REST API** | Cài trong mỗi vault qua Community Plugins |
| `uvx` | Đi kèm khi cài `uv` — dùng để chạy `mcp-obsidian` |

**Cài `uv` (nếu chưa có):**

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## 2. Cấu hình Obsidian — Local REST API

### Nguyên tắc quan trọng

> **Mỗi vault PHẢI dùng port khác nhau.** Nếu 2 vault cùng port → xung đột, vault sau không khởi động được.

### Bước thực hiện (lặp lại cho mỗi vault)

1. Mở vault trong Obsidian
2. Vào **Settings → Community Plugins → Local REST API**
3. Kéo xuống **Advanced Settings**
4. Đặt port theo bảng quy ước bên dưới
5. Bật **Enable Non-encrypted (HTTP) Server** nếu muốn dùng HTTP
6. Copy **API Key** (chuỗi dài ở phần "How to Access")

### Bảng port gợi ý

| Vault | HTTPS Port | HTTP Port |
|-------|-----------|-----------|
| Vault 1 | `27124` | `27123` |
| Vault 2 | `27126` | `27127` |
| Vault 3 | `27128` | `27129` |

> **Khuyến nghị:** Dùng **HTTPS** (cột trái) — an toàn hơn và là mặc định của `mcp-obsidian`.

---

## 3. Cấu hình Claude Desktop

### Vị trí file config

| Hệ điều hành | Đường dẫn |
|-------------|-----------|
| **Windows** | `C:\Users\{tên}\AppData\Roaming\Claude\claude_desktop_config.json` |
| **macOS** | `~/Library/Application Support/Claude/claude_desktop_config.json` |

### Cấu trúc đúng

```json
{
  "mcpServers": {
    "mcp-obsidian-vault1": {
      "command": "uvx",
      "args": ["mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "<api-key-của-vault-1>",
        "OBSIDIAN_HOST": "127.0.0.1",
        "OBSIDIAN_PORT": "27124",
        "OBSIDIAN_PROTOCOL": "https"
      }
    },
    "mcp-obsidian-vault2": {
      "command": "uvx",
      "args": ["mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "<api-key-của-vault-2>",
        "OBSIDIAN_HOST": "127.0.0.1",
        "OBSIDIAN_PORT": "27126",
        "OBSIDIAN_PROTOCOL": "https"
      }
    }
  }
}
```

> **Windows:** Đường dẫn `uvx` phải đầy đủ:  
> `"command": "C:\\Users\\{tên}\\.local\\bin\\uvx.exe"`

### 4 env vars bắt buộc

| Env var | Mô tả | Ví dụ |
|---------|-------|-------|
| `OBSIDIAN_API_KEY` | Lấy từ Local REST API settings | `a1b2c3d4e5f6...` |
| `OBSIDIAN_HOST` | Luôn để `127.0.0.1` | `127.0.0.1` |
| `OBSIDIAN_PORT` | Phải khớp với port trong Obsidian | `27124` |
| `OBSIDIAN_PROTOCOL` | `https` hoặc `http` — khớp với port dùng | `https` |

---

## 4. Patch bắt buộc cho mcp-obsidian

### Tại sao phải patch?

**Bug gốc của package:** `mcp-obsidian` chỉ đọc `OBSIDIAN_API_KEY` từ env, **bỏ qua** `OBSIDIAN_PORT`, `OBSIDIAN_HOST`, `OBSIDIAN_PROTOCOL` — luôn kết nối cứng đến `https://127.0.0.1:27124`.

**Hậu quả:** Tất cả các MCP server đều kết nối vào cùng 1 vault (vault đang dùng port 27124), vault khác dùng API key khác → lỗi `Authorization required`.

### Script patch tự động

Tạo file `patch-mcp-obsidian.py` và chạy **sau mỗi lần cài/update** `mcp-obsidian`:

```python
import os
import glob

# --- Tìm cache path theo OS ---
if os.name == 'nt':  # Windows
    cache_base = os.path.expandvars(r"%LOCALAPPDATA%\uv\cache\archive-v0")
else:  # macOS / Linux
    cache_base = os.path.expanduser("~/.cache/uv/archive-v0")

# Tìm tất cả tools.py của mcp_obsidian
pattern = os.path.join(cache_base, "**", "mcp_obsidian", "tools.py")
files = glob.glob(pattern, recursive=True)

# Cũng tìm trong site-packages (Windows)
pattern2 = os.path.join(cache_base, "**", "site-packages", "mcp_obsidian", "tools.py")
files += glob.glob(pattern2, recursive=True)
files = list(set(files))

if not files:
    print("Không tìm thấy mcp_obsidian/tools.py — kiểm tra lại uv cache path")
    exit(1)

# --- Nội dung cần thêm ---
old_header = 'api_key = os.getenv("OBSIDIAN_API_KEY", "")'
new_header = '''api_key = os.getenv("OBSIDIAN_API_KEY", "")
host = os.getenv("OBSIDIAN_HOST", "127.0.0.1")
port = int(os.getenv("OBSIDIAN_PORT", "27124"))
protocol = os.getenv("OBSIDIAN_PROTOCOL", "https")'''

old_call = 'obsidian.Obsidian(api_key=api_key)'
new_call = 'obsidian.Obsidian(api_key=api_key, host=host, port=port, protocol=protocol)'

# --- Patch ---
patched = 0
skipped = 0
for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if new_header in content:
        print(f"[SKIP - đã patch] {path}")
        skipped += 1
        continue
    content = content.replace(old_header, new_header)
    content = content.replace(old_call, new_call)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[PATCHED] {path}")
    patched += 1

print(f"\nKết quả: Patched {patched} | Skipped {skipped} | Tổng {len(files)} files")
```

**Chạy script:**

```bash
python patch-mcp-obsidian.py
```

> **Lưu ý:** Chạy lại script này mỗi khi `uvx` tự update `mcp-obsidian`.

---

## 5. Lỗi thường gặp & cách fix

### ❌ Lỗi 1: `Authorization required` (401)

```
Error 40101: Authorization required. Find your API Key in the 'Local REST API' section...
```

**Nguyên nhân có thể:**

| Nguyên nhân | Cách kiểm tra | Cách fix |
|-------------|--------------|----------|
| Vault chưa mở trong Obsidian | Mở Obsidian, chắc chắn vault đang active | Mở vault trước khi khởi động Claude |
| API Key sai | Vào Obsidian → Settings → Local REST API → copy key | Cập nhật key trong `claude_desktop_config.json` |
| Port sai | Xem port trong Local REST API → Advanced Settings | Sửa `OBSIDIAN_PORT` cho khớp |
| **Chưa patch** `mcp-obsidian` | Kiểm tra `tools.py` có dòng `host = os.getenv(...)` chưa | Chạy script patch ở mục 4 |
| Protocol sai | Dùng HTTP port nhưng `OBSIDIAN_PROTOCOL=https` | Đặt đúng protocol khớp với port |

**Kiểm tra nhanh bằng curl:**

```bash
# HTTPS
curl -sk -H "Authorization: Bearer <API_KEY>" https://127.0.0.1:<PORT>/vault/

# HTTP
curl -s -H "Authorization: Bearer <API_KEY>" http://127.0.0.1:<PORT>/vault/
```

Nếu curl trả về danh sách file → vault OK, vấn đề nằm ở MCP patch.  
Nếu curl trả về 401 → API Key hoặc port sai.  
Nếu curl timeout/refused → vault chưa mở.

---

### ❌ Lỗi 2: Cả 2 vault đều kết nối vào vault 1

**Triệu chứng:** vault 2 trả về đúng file của vault 1, hoặc báo 401.

**Nguyên nhân:** Chưa patch `mcp-obsidian` — package hardcode port 27124.

**Fix:** Chạy script patch ở mục 4, sau đó restart Claude Desktop.

---

### ❌ Lỗi 3: `OBSIDIAN_API_KEY environment variable required`

```
ValueError: OBSIDIAN_API_KEY environment variable required
```

**Nguyên nhân:** Thiếu `OBSIDIAN_API_KEY` trong `env` của config.

**Fix:** Kiểm tra `claude_desktop_config.json`, đảm bảo mỗi MCP server có đủ 4 env vars.

---

### ❌ Lỗi 4: MCP server không xuất hiện trong Claude

**Nguyên nhân có thể:**
- JSON config bị lỗi cú pháp (thiếu dấu phẩy, ngoặc)
- Đường dẫn `uvx` sai (Windows cần đường dẫn tuyệt đối)
- Chưa restart Claude Desktop sau khi sửa config

**Fix:**

```bash
# Validate JSON (macOS/Linux)
python3 -m json.tool ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Validate JSON (Windows)
python -m json.tool "%APPDATA%\Claude\claude_desktop_config.json"
```

---

### ❌ Lỗi 5: `uvx` không tìm thấy (Windows)

```
The system cannot find the file specified
```

**Fix:** Dùng đường dẫn tuyệt đối trong config:

```json
"command": "C:\\Users\\{TÊN_USER}\\.local\\bin\\uvx.exe"
```

Tìm đúng đường dẫn:

```powershell
where uvx
```

---

### ❌ Lỗi 6: Vault hoạt động lúc được lúc không

**Nguyên nhân:** Obsidian tắt vault (không focus) → Local REST API dừng.

**Fix:**
- Giữ Obsidian luôn mở (không đóng cửa sổ)
- Trên macOS: đảm bảo Obsidian không bị macOS suspend

---

### ❌ Lỗi 7: Patch bị mất sau khi update `uvx`

**Nguyên nhân:** `uvx` tạo cache mới khi update → file mới chưa được patch.

**Fix:** Chạy lại script patch sau mỗi lần `uvx` update `mcp-obsidian`.

---

## 6. Checklist xác nhận

Thực hiện theo thứ tự từ trên xuống:

```
[ ] 1. Plugin Local REST API đã cài trong TẤT CẢ vault
[ ] 2. Mỗi vault dùng port HTTPS khác nhau (27124, 27126, 27128...)
[ ] 3. Đã copy API Key của từng vault
[ ] 4. claude_desktop_config.json có đủ 4 env vars cho mỗi vault
[ ] 5. JSON config hợp lệ (chạy python -m json.tool để kiểm tra)
[ ] 6. Đã chạy script patch-mcp-obsidian.py
[ ] 7. Đã khởi động lại Claude Desktop
[ ] 8. Tất cả vault đang mở trong Obsidian
[ ] 9. Test curl thành công cho từng vault
[ ] 10. Test kết nối qua Claude — vault trả về đúng file
```

---

## Tóm tắt luồng hoạt động

```
Claude Desktop
    └── MCP Server: mcp-obsidian-vault1 (uvx mcp-obsidian)
    │       env: PORT=27124, PROTOCOL=https, KEY=xxx
    │       └── kết nối → https://127.0.0.1:27124 → Obsidian Vault 1
    │
    └── MCP Server: mcp-obsidian-vault2 (uvx mcp-obsidian)
            env: PORT=27126, PROTOCOL=https, KEY=yyy
            └── kết nối → https://127.0.0.1:27126 → Obsidian Vault 2
```

> **Điều kiện để hoạt động đúng:**  
> Port đúng ✓ + Protocol khớp ✓ + API Key đúng ✓ + Package đã patch ✓ + Vault đang mở ✓
