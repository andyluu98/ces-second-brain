# Hướng dẫn cài đặt ces second brain

> **Mục tiêu:** Sau 5 phút, bạn gõ `/obsidian-save` trong Claude và có markdown note ngay để paste vào Obsidian.

> **Yêu cầu:** Tài khoản Claude (claude.ai / Claude Desktop / Claude Code). Nên có Obsidian.

---

## Cài skill (2 bước)

### Bước 1 — Tải zip

Mở: https://github.com/andyluu98/ces-second-brain/releases/latest

Click `ces-second-brain.zip` để tải về.

### Bước 2 — Upload vào Claude

Tùy bạn dùng app nào:

**A. Claude Desktop hoặc claude.ai web:**
1. Mở app → click avatar → **Settings**
2. Vào tab **Capabilities** → **Skills** (hoặc tab tên tương tự)
3. Click **Upload skill** → chọn file `ces-second-brain.zip` vừa tải
4. Đợi vài giây → skill xuất hiện trong danh sách
5. Mở chat mới → gõ `/` → menu hiện 26 lệnh tiếng Việt

**B. Claude Code (terminal):**
```bash
# Mac / Linux
git clone https://github.com/andyluu98/ces-second-brain ~/.claude/skills/ces-second-brain

# Windows PowerShell
git clone https://github.com/andyluu98/ces-second-brain "$env:USERPROFILE\.claude\skills\ces-second-brain"
```

Restart Claude Code → skill auto-load.

---

## Bắt đầu dùng

### Có vault Obsidian rồi

1. Mở Claude → gõ `/obsidian-init`
2. Claude hỏi vài câu về cấu trúc vault → output `_CLAUDE.md` ở chat
3. Copy nội dung `_CLAUDE.md` → paste vào file `_CLAUDE.md` ở root vault
4. Từ đây: chat tự nhiên với Claude. Khi cần lưu, gõ `/obsidian-save` → Claude xuất markdown → bạn copy vào vault

### Chưa có vault

1. Tải Obsidian: https://obsidian.md
2. Mở Obsidian → **Create new vault** → đặt tên + chọn folder
3. Quay lại Claude → gõ `/obsidian-init`
4. Claude hỏi tên bạn + bạn dùng vault để làm gì + chọn cấu trúc
5. Claude xuất các file khởi tạo (`_CLAUDE.md`, folder structure, templates) ở chat
6. Bạn copy từng file vào vault Obsidian

---

## Quan trọng: Skill này không tự ghi vào vault

Skill chạy trong chat. Khi gõ `/obsidian-save`, Claude xuất markdown ở khung chat. **Bạn copy paste thủ công vào file Obsidian.**

Lý do: để skill cài 1 phát chạy mọi nơi (claude.ai, Desktop, Code) mà không cần plugin / Local REST API / MCP / Python / Node.js.

Nếu cần auto-ghi vault, sau này có thể bật MCP `filesystem` server trong Claude Desktop (nâng cao, không bắt buộc).

---

## Lệnh thường dùng cho người mới

| Khi nào | Gõ | Kết quả |
|---|---|---|
| Sau cuộc họp, cuộc trò chuyện | `/obsidian-save` | Claude xuất markdown các note đáng giữ — bạn copy vào vault |
| Đầu ngày | `/obsidian-daily` | Claude xuất daily note hôm nay |
| Cần ghi nhanh ý tưởng | `/obsidian-capture ý tưởng của tôi là...` | Claude xuất Ideas/note.md |
| Phân vân quyết định lớn | `/obsidian-challenge` (sau khi paste lịch sử liên quan) | Claude phản biện bằng vault history |
| Cuối tuần | `/obsidian-review` | Claude xuất review tuần |

Không nhớ slash → cứ nói tự nhiên: "Lưu cuộc trò chuyện này", "Tạo note hôm nay", "Phản biện ý tưởng X dùm". Claude tự hiểu.

Tham khảo [PHRASEBOOK-VN.md](PHRASEBOOK-VN.md) cho 25+ câu mẫu.

---

## Cập nhật skill

Khi có version mới:

**Cách A (zip upload):** Tải zip mới ở Releases → upload lại (Claude tự thay thế).

**Cách B (Claude Code clone):**
```bash
cd ~/.claude/skills/ces-second-brain
git pull
```

---

## Khắc phục sự cố

**Slash commands không hiện trong menu:**
- Restart Claude hoàn toàn (kill từ system tray / menu bar)
- Check Settings → Skills → `ces-second-brain` có trong danh sách không

**Upload zip báo lỗi:**
- Check zip có folder gốc tên đúng `ces-second-brain` không (mở zip xem)
- Nếu sai: giải nén → đổi tên folder thành `ces-second-brain` → nén lại → upload

**Claude trả lời tiếng Anh:**
- Mở chat mới (skill mới load đầy đủ ở chat mới)
- Hoặc gõ "Trả lời tôi bằng tiếng Việt" ở đầu chat

---

## Cần hỗ trợ?

- Issue / bug: https://github.com/andyluu98/ces-second-brain/issues
- Phrasebook: [PHRASEBOOK-VN.md](PHRASEBOOK-VN.md)
- Quy tắc AI-first cho note (advanced): `references/ai-first-rules.md` (tiếng Anh)
