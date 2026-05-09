# Hướng dẫn cài đặt obsidian-second-brain (cho người mới)

> **Mục tiêu:** Sau khi đọc xong file này, bạn có thể gõ `/obsidian-save` trong Claude Desktop và Claude tự ghi cuộc trò chuyện vào vault Obsidian của bạn — bằng tiếng Việt.

> **Thời gian:** 20-30 phút nếu chưa có gì. 5-10 phút nếu đã có Obsidian + Claude Desktop.

> **Yêu cầu:** máy tính Windows/Mac/Linux, internet, có tài khoản Anthropic (Claude.ai).

---

## Bản đồ các bước

```
1. Cài Obsidian (nếu chưa có)        ──┐
2. Tạo vault                            │  Một lần thôi
3. Cài Node.js (cho mcp-obsidian)       │
4. Cài Claude Desktop                   │
5. Bật API trong Obsidian               │
6. Config Claude Desktop nối vault    ──┘
7. Cài skill obsidian-second-brain    ──┐  Cập nhật khi có version mới
8. Bootstrap vault với /obsidian-init ──┘
9. Bắt đầu dùng                       ──── Hằng ngày
```

---

## Bước 1 — Cài Obsidian

Bỏ qua nếu đã có Obsidian.

1. Mở https://obsidian.md
2. Tải bản cho hệ điều hành của bạn (Windows / macOS / Linux)
3. Cài đặt như mọi app khác (next next finish)
4. Mở Obsidian lần đầu — chọn ngôn ngữ tiếng Việt nếu muốn (Settings → About → Language → Tiếng Việt)

---

## Bước 2 — Tạo vault

Vault = thư mục chứa note của bạn. Skill này sẽ ghi/đọc trong thư mục đó.

1. Mở Obsidian
2. Click **Create new vault** (hoặc Tạo vault mới)
3. Đặt tên: ví dụ `bo-nao-thu-2`
4. Chọn vị trí: ví dụ `D:\Obsidian\bo-nao-thu-2` (Windows) hay `~/Obsidian/bo-nao-thu-2` (Mac/Linux)
5. **GHI NHỚ ĐƯỜNG DẪN NÀY** — Bạn sẽ paste vào config sau.
6. Click **Create**

Vault mở ra trống. Đó là điều bình thường.

> **Tip:** Đặt vault trong thư mục đồng bộ cloud (iCloud, Google Drive, Dropbox, OneDrive) để có backup tự động. KHÔNG đặt vault trong thư mục mà nhiều máy ghi cùng lúc — sẽ conflict.

---

## Bước 3 — Cài Node.js

Cần Node.js để chạy `mcp-obsidian` (cầu nối giữa Claude và vault).

**Windows / macOS:**
1. Mở https://nodejs.org
2. Tải bản **LTS** (xanh lá, bên trái)
3. Cài như app thường
4. Mở terminal (Windows: gõ `cmd` trong Start; macOS: mở Terminal app) và kiểm tra:
   ```
   node --version
   npm --version
   npx --version
   ```
   Nếu hiện 3 số version (vd `v22.10.0`, `10.9.0`, `10.9.0`) là OK.

Bỏ qua nếu đã có Node.js.

---

## Bước 4 — Cài Claude Desktop

1. Mở https://claude.ai/download
2. Tải Claude Desktop
3. Cài đặt
4. Mở app, đăng nhập tài khoản Anthropic (hoặc tạo mới)

---

## Bước 5 — Bật Local REST API trong Obsidian (cho mcp-obsidian)

`mcp-obsidian` cần Obsidian mở một REST endpoint nhỏ để đọc/ghi vault. Bật như sau:

1. Trong Obsidian → Settings (Ctrl+,)
2. Vào tab **Community plugins** → bật **Community plugins** (lần đầu)
3. Click **Browse** → tìm "**Local REST API**" của tác giả Adam Coddington
4. Click **Install** → **Enable**
5. Vào tab plugin "Local REST API" trong Settings → copy **API Key** (chuỗi dài). **GHI NHỚ KEY NÀY.**
6. Mặc định plugin chạy ở `https://127.0.0.1:27124` (HTTPS với cert tự ký) — không đổi gì.

> **Mac/Linux:** sẽ có cảnh báo "self-signed certificate". Đó là bình thường vì plugin tạo cert local.

---

## Bước 6 — Config Claude Desktop nối vault

Đây là bước "lắp dây" — báo cho Claude Desktop biết: vault của bạn ở đâu và cách truy cập.

### 6.1. Mở file config

**Windows:**
- File ở: `%APPDATA%\Claude\claude_desktop_config.json`
- Mở Run (Win+R) → paste `%APPDATA%\Claude` → Enter
- Nếu chưa có file `claude_desktop_config.json`: tạo file mới rỗng.

**macOS:**
- File ở: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Mở Terminal:
  ```
  open ~/Library/Application\ Support/Claude/
  ```

**Linux:**
- File ở: `~/.config/Claude/claude_desktop_config.json`

### 6.2. Paste config sau (đã thay đường dẫn vault và API key)

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["-y", "mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "PASTE_API_KEY_VAO_DAY",
        "OBSIDIAN_HOST": "127.0.0.1",
        "OBSIDIAN_PORT": "27124"
      }
    }
  }
}
```

Thay `PASTE_API_KEY_VAO_DAY` bằng API key copy ở Bước 5.5.

### 6.3. Lưu file. Tắt hoàn toàn Claude Desktop. Mở lại.

> **Quan trọng:** Phải tắt từ system tray (Windows) / menu bar (Mac), không chỉ đóng cửa sổ.

### 6.4. Kiểm tra

1. Mở Obsidian — phải đang chạy (vì plugin Local REST API hoạt động khi Obsidian mở)
2. Mở Claude Desktop
3. Bắt đầu chat mới
4. Click icon 🔌 (plug) hoặc tương tự ở dưới ô chat → kiểm tra "obsidian" có trong danh sách MCP server đang kết nối không

Nếu **có** → tiếp Bước 7.
Nếu **không** → check lại API key, port, đường dẫn JSON. Xem [Khắc phục sự cố](#khắc-phục-sự-cố) cuối file.

---

## Bước 7 — Cài skill obsidian-second-brain

### Cách A — Tự động (khuyến nghị)

Mở terminal và chạy:

**macOS / Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/andyluu98/ces-second-brain/main/scripts/quick-install.sh | bash
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/andyluu98/ces-second-brain $HOME\.claude\skills\ces-second-brain
```

> Lưu ý: skill này đặt slash commands vào `~/.claude/commands/`. Claude Desktop tự load. Nếu không tự load, restart Claude Desktop.

### Cách B — Áp dụng bản tiếng Việt vào skill đã có

Nếu bạn đã clone repo này về local (như đang đọc file này), chạy:

```bash
cd duong-dan-toi-repo
python scripts/apply_vn_descriptions.py
```

Script chạy lần đầu sẽ:
- Dịch frontmatter `description:` của 31 commands sang tiếng Việt
- Append chỉ thị "trả lời + ghi note bằng tiếng Việt" vào mỗi command

Chạy lần 2 trở đi không nhân bản (idempotent).

Sau đó symlink hay copy `commands/*.md` vào `~/.claude/commands/`.

### Cách C — Manual

```bash
git clone https://github.com/andyluu98/ces-second-brain ~/.claude/skills/ces-second-brain
cd ~/.claude/skills/ces-second-brain
python scripts/apply_vn_descriptions.py
cp commands/*.md ~/.claude/commands/
```

---

## Bước 8 — Bootstrap vault

Bây giờ vault đang trống. Skill có script tạo cấu trúc folder, template, kanban tự động.

```bash
cd ~/.claude/skills/obsidian-second-brain
python scripts/bootstrap_vault.py --path "DUONG_DAN_VAULT" --name "Tên Của Bạn" --preset PRESET
```

Thay:
- `DUONG_DAN_VAULT` = đường dẫn vault Bước 2
- `Tên Của Bạn` = tên thật của bạn (xuất hiện trong _CLAUDE.md)
- `PRESET` = một trong: `executive`, `builder`, `creator`, `researcher`, hoặc bỏ flag `--preset` để dùng general

Ví dụ:

```bash
# Founder/manager
python scripts/bootstrap_vault.py --path "D:\Obsidian\bo-nao-thu-2" --name "Hải Vũ" --preset executive

# Developer
python scripts/bootstrap_vault.py --path "~/Obsidian/bo-nao-thu-2" --name "Nguyễn Văn A" --preset builder

# Content creator
python scripts/bootstrap_vault.py --path "~/Obsidian/bo-nao-thu-2" --name "Trần Thị B" --preset creator
```

Sau đó mở Claude Desktop, gõ:

```
/obsidian-init
```

Skill sẽ quét vault và tạo `_CLAUDE.md` (sổ tay vận hành) + `index.md` (mục lục) + `log.md` (nhật ký).

---

## Bước 9 — Bắt đầu dùng

Mở Claude Desktop, gõ `/` → menu hiện 31 commands với mô tả tiếng Việt.

**Lệnh quan trọng nhất cho người mới:**

| Khi nào | Gõ | Kết quả |
|---|---|---|
| Sau cuộc họp | `/obsidian-save` | Lưu mọi thứ đáng giữ vào vault |
| Đầu ngày | `/obsidian-daily` | Tạo daily note hôm nay |
| Cần tìm gì | `/obsidian-find từ_khóa` | Tìm kiếm thông minh |
| Có ý tưởng | `/obsidian-capture ý tưởng của tôi là...` | Lưu vào Ideas/ |
| Cuối tuần | `/obsidian-review` | Tổng kết tuần tự động |

Không nhớ slash? Gõ tự nhiên: "Lưu cuộc trò chuyện này", "Tạo note hôm nay", "Tìm tôi xem có gì về dự án X". Claude tự hiểu.

Tham khảo [PHRASEBOOK-VN.md](PHRASEBOOK-VN.md) cho 30 câu mẫu.

---

## Khắc phục sự cố

### "obsidian" MCP server không kết nối

**1. Obsidian phải đang mở.**
Local REST API chỉ hoạt động khi Obsidian chạy. Tắt Obsidian = MCP đứt.

**2. Kiểm tra plugin Local REST API.**
Settings → Community plugins → Local REST API → bật toggle.

**3. Check JSON đúng cú pháp.**
Mở https://jsonlint.com → paste config → fix lỗi cú pháp (thiếu dấu phẩy, ngoặc).

**4. Port 27124 đã bị chiếm?**
Đổi port trong plugin settings và sync với JSON.

**5. Tự ký HTTPS bị reject?**
Một số máy reject self-signed cert. Trong plugin settings, bật chế độ HTTP (port 27123) và đổi config:
```json
"OBSIDIAN_HOST": "127.0.0.1",
"OBSIDIAN_PORT": "27123",
"OBSIDIAN_PROTOCOL": "http"
```

### Slash commands không hiện

1. Restart Claude Desktop hoàn toàn (kill từ tray/menu bar).
2. Check `~/.claude/commands/` có file `obsidian-*.md` chưa.
3. Trên Windows: `%USERPROFILE%\.claude\commands\`

### Claude trả lời tiếng Anh dù đã việt hóa

1. Check một command file (vd `commands/obsidian-save.md`) — có dòng `<!-- vn-directive:v1 -->` ở cuối không?
2. Nếu không: chạy lại `python scripts/apply_vn_descriptions.py`
3. Restart Claude Desktop.

### Bootstrap script báo lỗi

1. Check Python version ≥ 3.10: `python --version`
2. Đường dẫn vault có ký tự đặc biệt? Bọc trong dấu nháy kép `""`.
3. Vault đã có note? Bootstrap an toàn — không xóa note cũ, chỉ tạo folder + file mới nếu chưa có.

---

## Bước nâng cao (tùy chọn)

### Research toolkit

Cần 5 lệnh `/x-read`, `/x-pulse`, `/research`, `/research-deep`, `/youtube`? Cài thêm:

```bash
cd ~/.claude/skills/obsidian-second-brain
mkdir -p ~/.config/obsidian-second-brain
cp .env.example ~/.config/obsidian-second-brain/.env
chmod 600 ~/.config/obsidian-second-brain/.env  # Linux/macOS
```

Mở file `.env`, paste API key:
- `XAI_API_KEY` — lấy ở https://console.x.ai (~$5/tháng đủ dùng cá nhân)
- `PERPLEXITY_API_KEY` — lấy ở https://perplexity.ai/settings/api (~$5/tháng)
- `YOUTUBE_API_KEY` — tùy chọn, lấy ở https://console.cloud.google.com (free tier 10k/ngày)

Cài Python deps:
```bash
pip install uv
uv sync
```

### Scheduled agents (chỉ Claude Code)

Bốn agent định kỳ (sáng/tối/tuần/sức khỏe vault) chỉ chạy trên **Claude Code (CLI)**, không trên Claude Desktop. Nếu muốn:

```bash
# Trong Claude Code
/schedule obsidian-morning -- daily 8:00 AM
/schedule obsidian-nightly -- daily 10:00 PM
/schedule obsidian-weekly -- every Friday 6:00 PM
/schedule obsidian-health-check -- every Sunday 9:00 PM
```

Xem `SKILL.md` (EN) phần "Scheduled Agents" cho prompt chi tiết.

### Background agent (chỉ Claude Code)

PostCompact hook tự cập nhật vault sau mỗi context compaction. Chỉ chạy trên Claude Code. Setup ở `SKILL.md` phần "Background Agent".

---

## Cập nhật skill

```bash
cd ~/.claude/skills/obsidian-second-brain
git pull
python scripts/apply_vn_descriptions.py  # áp lại bản dịch nếu có command mới
```

Restart Claude Desktop.

---

## Cần hỗ trợ?

- Issue / bug bản tiếng Việt: https://github.com/andyluu98/ces-second-brain/issues
- Issue / bug bản gốc EN: https://github.com/eugeniughelbur/obsidian-second-brain/issues
- Phần dịch tiếng Việt có sai sót: tạo issue ở repo VN fork (nếu có) hoặc PR vào upstream
- AI-first rule chi tiết: `references/ai-first-rules.md`
- Vault schema chi tiết: `references/vault-schema.md`

---

## Câu hỏi thường gặp ngắn

**Có cần đăng ký gói Claude Pro không?**
Không bắt buộc. Free tier hoạt động nhưng có giới hạn message/ngày. Pro ($20/tháng) thì xài thoải mái.

**Vault của tôi có data nhạy cảm — có an toàn không?**
Vault hoàn toàn local. mcp-obsidian chỉ hoạt động ở `127.0.0.1` (localhost), không gửi ra internet. Claude Desktop gửi nội dung note đến Anthropic API khi bạn chat — đó là cách Claude hoạt động. Anthropic không train trên consumer data theo policy hiện tại.

**Có thể dùng nhiều vault không?**
Có. Đổi `OBSIDIAN_API_KEY` và port trong config trỏ đến vault khác. Hoặc dùng nhiều entry MCP server với tên khác nhau.

**Có dịch hết SKILL.md sang VN không?**
Không. SKILL.md là Claude đọc, hoạt động tốt hơn với EN. Người dùng cuối không cần đọc SKILL.md.

**Có chạy offline không?**
Không. Claude API yêu cầu internet. Chỉ vault thì local.
