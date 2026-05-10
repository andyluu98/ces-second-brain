<h1 align="center">ces second brain</h1>

<p align="center">
  <strong>Second brain AI cá nhân — biến vault Obsidian thành tri thức tự cập nhật qua Claude.</strong><br/><br/>
  <em>26 lệnh tiếng Việt · ghi note theo AI-first rule · phản biện ý tưởng · tổng hợp pattern · 4 preset cho 4 nghề</em>
</p>

<p align="center">
  <a href="docs/HUONG-DAN-CAI-DAT.md"><strong>Hướng dẫn cài đặt</strong></a> ·
  <a href="docs/PHRASEBOOK-VN.md"><strong>Phrasebook</strong></a> ·
  <a href="https://github.com/andyluu98/ces-second-brain/releases/latest"><strong>Tải zip mới nhất</strong></a>
</p>

---

## Cài 2 bước, chạy mọi nơi

1. Tải `ces-second-brain.zip` ở [Releases](https://github.com/andyluu98/ces-second-brain/releases/latest)
2. Mở Claude (claude.ai web / Claude Desktop / Claude Code) → **Settings → Capabilities → Skills → Upload skill** → chọn zip

Xong. Gõ `/` trong chat → menu hiện 26 lệnh tiếng Việt.

**Không cần:** Python, Node.js, Local REST API plugin, MCP config, API keys.

---

## Vấn đề

Bạn dùng Claude mỗi ngày. Mỗi cuộc trò chuyện bắt đầu lại từ đầu. Bạn giải thích lại mọi thứ. Cuộc trò chuyện kết thúc. Mọi thứ biến mất.

Bạn ghi chú trong Obsidian. Hàng trăm file. Chúng nằm im. Bạn ra cùng một quyết định hai lần vì quên đã quyết 6 tháng trước. Ý tưởng mục trong daily notes.

**Hai công cụ mạnh. Hoàn toàn rời rạc.**

ces second brain nối chúng lại — qua chat thường, không cần plugin.

---

## Skill làm gì

Khi user gõ `/obsidian-save` (hoặc nói tự nhiên "lưu cuộc trò chuyện này"), Claude:

1. Quét cuộc trò chuyện, rút ra mọi thứ đáng giữ — quyết định, người, task, ý tưởng
2. Output các markdown notes ở đúng format AI-first (preamble, frontmatter, wikilinks, recency markers)
3. Liệt kê notes nào cần update kèm theo (kanban, daily note, project note)
4. User **copy markdown vào vault Obsidian** thủ công

Không tự động ghi vault. Đổi lại: cài 1 phát chạy mọi nơi, không config gì.

---

## 26 lệnh

### Vận hành — Claude nhớ

| Lệnh | Làm gì |
|---|---|
| `/obsidian-save` | Lưu mọi thứ từ cuộc trò chuyện — quyết định, task, người, ý tưởng |
| `/obsidian-ingest` | Drop URL/PDF/transcript/screenshot → vault tự viết lại 5-15 trang |
| `/obsidian-synthesize` | Tự tìm pattern qua nhiều nguồn và viết trang tổng hợp |
| `/obsidian-reconcile` | Tìm mâu thuẫn và giải quyết — vault duy trì sự thật của nó |
| `/obsidian-export` | Snapshot JSON/markdown sạch để AI tool nào cũng đọc được |
| `/obsidian-daily` | Tạo hoặc cập nhật daily note hôm nay |
| `/obsidian-log` | Log phiên làm việc, liên kết khắp nơi |
| `/obsidian-task` | Thêm task vào đúng kanban với priority + due date |
| `/obsidian-person` | Tạo hoặc cập nhật note người |
| `/obsidian-decide` | Ghi quyết định vào project note phù hợp |
| `/obsidian-capture` | Ghi nhanh ý tưởng (zero-friction) |
| `/obsidian-find` | Tìm kiếm thông minh kèm ngữ cảnh |
| `/obsidian-recap` | Tóm tắt ngày/tuần/tháng |
| `/obsidian-review` | Tổng kết tuần/tháng có cấu trúc |
| `/obsidian-board` | Xem và cập nhật kanban board |
| `/obsidian-project` | Project note với board + daily link |
| `/obsidian-health` | Audit vault — mâu thuẫn, gap, claim cũ, orphan |
| `/obsidian-adr` | Decision record — vault biết vì sao nó được tổ chức như vậy |
| `/obsidian-visualize` | Canvas map vault — nhìn thấy hình dạng second brain |
| `/obsidian-learn` | Rà bài học vault, cắt cái cũ, làm nổi pattern đang sống |
| `/obsidian-init` | Tạo `_CLAUDE.md`, `index.md`, `log.md` cho vault |

### Tư duy — Claude tư duy cùng bạn

| Lệnh | Làm gì |
|---|---|
| `/obsidian-challenge` | Vault phản biện ý tưởng bằng chính lịch sử của bạn |
| `/obsidian-emerge` | Phát hiện pattern từ 30 ngày note bạn chưa đặt tên |
| `/obsidian-connect [A] [B]` | Bắc cầu hai chủ đề không liên quan để bật ý tưởng mới |
| `/obsidian-graduate` | Nâng cấp ý tưởng phôi thai thành project hoàn chỉnh |

### Context — Claude biết bạn

| Lệnh | Làm gì |
|---|---|
| `/obsidian-world` | Nạp danh tính + trạng thái với cấp độ token tăng dần (L0-L3) |

---

## Cách "ra lệnh"

Trên Claude (mọi surface), gõ `/` để mở menu skill → chọn lệnh. Menu hiển thị mô tả tiếng Việt.

Nếu không nhớ tên, dùng [Phrasebook](docs/PHRASEBOOK-VN.md) — danh sách câu nói tự nhiên VN. Ví dụ thay vì nhớ `/obsidian-save`, có thể chỉ cần nói:

> "Lưu cuộc trò chuyện này vào vault giúp tôi"

Claude tự hiểu và chạy lệnh tương ứng.

---

## Bộ note ra theo format AI-first

Mọi note skill xuất ra đều theo `references/ai-first-rules.md`:

- `## Cho Claude tương lai` preamble (2-3 câu tóm tắt)
- Frontmatter giàu (`type`, `date`, `tags`, `ai-first: true`, ...)
- Recency marker mỗi claim ngoài: `(tính đến 2026-05, source.com)`
- `[[wikilinks]]` cho mỗi người/dự án/ý tưởng
- URL nguồn nguyên văn
- Confidence level: `stated | high | medium | speculation`

Ý nghĩa: Claude tương lai (lần chat sau) đọc note dễ hiểu, dễ truy hồi, không lệ thuộc backlinks.

---

## Chọn preset (lúc bootstrap vault)

Khi user gõ `/obsidian-init`, skill hỏi 3 câu rồi sinh `_CLAUDE.md` phù hợp.

| Preset | Dành cho | Kanban style |
|---|---|---|
| **executive** | Founder, operator, manager | OKRs / Quarterly / Weekly |
| **builder** | Developer, engineer, architect | Backlog / Sprint / Done |
| **creator** | Writer, YouTuber, marketer | Ideas / Drafts / Published |
| **researcher** | Academic, analyst, deep-diver | Reading / Processing / Synthesized |

Không chọn preset → vault general-purpose.

---

## FAQ ngắn

**Skill có tự ghi vào vault Obsidian của tôi không?**
Mặc định: KHÔNG. Skill xuất markdown ở chat, user copy paste vào vault. Đổi lại: cài 1 phát chạy mọi nơi, không cần plugin/config gì.

**Có cần API key không?**
Không.

**Có cần Python / Node.js không?**
Không.

**Có chạy trên Windows / Mac / Linux không?**
Có. Chạy mọi nơi Claude chạy được — vì là pure markdown skill, không có script chạy local.

**Có an toàn cho vault hiện có không?**
Có. Skill không truy cập file của bạn. Chỉ đưa ra markdown. Bạn quyết định paste hay không.

**Khác Notion AI / Mem chỗ nào?**
Notion AI và Mem là SaaS đóng — họ giữ data. Skill này không lưu data ở đâu — markdown ở chat, user kiểm soát hoàn toàn.

---

## Triết lý

Hầu hết công cụ second brain biến bạn thành lao công — copy paste, format, tag tay.

ces second brain đảo ngược. Bạn nghĩ, làm, nói. Claude lo memory. Format AI-first chuẩn. Bạn chỉ paste vào vault.

**Note của bạn là moat của bạn.**

---

## Người dùng phổ thông

Xem [docs/HUONG-DAN-CAI-DAT.md](docs/HUONG-DAN-CAI-DAT.md) — hướng dẫn 1 trang, 5 phút.

---

## License

MIT — xem [LICENSE](LICENSE)
