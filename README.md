<p align="center">
  <a href="https://github.com/andyluu98/ces-second-brain">
    <img src="media/banner.png" alt="obsidian-second-brain — biến vault Obsidian thành second brain AI tự cập nhật" width="100%" />
  </a>
</p>

<h1 align="center">obsidian-second-brain (bản tiếng Việt)</h1>

<p align="center">
  <strong>Vault Obsidian biết tự viết lại chính nó.</strong><br/>
  <em>Mỗi nguồn mới CẬP NHẬT các trang đã có thay vì chỉ thêm trang mới. Mâu thuẫn tự hòa giải. Vault thông minh hơn trong khi bạn ngủ.</em><br/><br/>
  <em>31 lệnh · auto-tổng hợp · công cụ tư duy biết phản biện bạn · research live từ X, web, YouTube · 4 agent định kỳ · 4 preset</em>
</p>

<p align="center">
  <a href="docs/HUONG-DAN-CAI-DAT.md"><strong>Hướng dẫn cài đặt</strong></a> ·
  <a href="docs/PHRASEBOOK-VN.md"><strong>Phrasebook (cách nói lệnh)</strong></a> ·
  <a href="README-en.md">English README (upstream original)</a>
</p>

> **Đây là bản dịch tiếng Việt** của [obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain). Skill gốc bằng tiếng Anh; bản này việt hóa **mô tả 31 slash commands** và thêm **chỉ thị "trả lời + ghi note bằng tiếng Việt"** vào mỗi command. Code và logic vẫn nguyên upstream.

---

## Vấn đề

Bạn dùng Claude mỗi ngày. Mỗi cuộc trò chuyện bắt đầu lại từ đầu. Bạn giải thích lại mọi thứ. Cuộc trò chuyện kết thúc. Mọi thứ biến mất.

Bạn ghi chú trong Obsidian. Hàng trăm file. Chúng nằm im. Bạn ra cùng một quyết định hai lần vì quên đã quyết 6 tháng trước. Ý tưởng mục trong daily notes. Không ai nối các điểm.

**Hai công cụ mạnh. Hoàn toàn rời rạc.**

Skill này nối chúng lại.

---

## Skill này làm gì

| Lúc | Làm gì | Bạn được gì |
|---|---|---|
| Sau cuộc họp | `/obsidian-save` | Mọi quyết định/người/task/ý tưởng tự lưu đúng nơi |
| Có voice memo | `/obsidian-ingest meeting.m4a` | Whisper transcribe → tách từng promise/action item → phân phối khắp vault |
| Chụp whiteboard | `/obsidian-ingest photo.png` | Đọc ảnh → tạo concept notes → liên kết project liên quan |
| Có video hay | `/obsidian-ingest https://youtube.com/...` | Vault TỰ VIẾT LẠI — entity được cập nhật, mâu thuẫn được giải quyết |
| Trước quyết định lớn | `/obsidian-challenge` | Vault tìm thất bại quá khứ trên cùng chủ đề và phản biện bằng chính lời bạn |
| Bắt đầu ngày mới | `/obsidian-daily` | Lịch + việc trễ + thay đổi qua đêm vào note hôm nay |
| Đi ngủ | (auto) | Agent đêm chạy 5 pha — đóng ngày, hòa giải mâu thuẫn, tổng hợp pattern, chữa orphan, build lại index |
| Đọc post X | `/x-read [url]` | Grok truy cập live → post + thread + sentiment + voices đáng theo dõi |
| Cần research | `/research [topic]` | Perplexity Sonar Pro → báo cáo có trích dẫn, recency markers |
| Research sâu | `/research-deep [topic]` | Quét vault trước → chỉ lấp khoảng trống → cập nhật toàn vault |

**Bạn không bao giờ phải mở Obsidian.** Mọi thứ qua Claude.

---

## 4 lớp kiến trúc

```
+------------------------------------------+
|  LỚP 1: Vận hành (21 lệnh)               |
|  Claude nhớ mọi thứ                       |
+------------------------------------------+
|  LỚP 2: Tư duy (4 lệnh)                  |
|  Claude tư duy cùng bạn                   |
+------------------------------------------+
|  LỚP 3: Context Engine (1 lệnh)          |
|  Claude biết bạn là ai                    |
+------------------------------------------+
|  LỚP 4: Research Toolkit (5 lệnh)        |
|  Claude kéo kiến thức về                  |
+------------------------------------------+
|  LUÔN BẬT                                 |
|  Background agent + 4 scheduled agents    |
+------------------------------------------+
```

---

## 31 lệnh

### Vận hành — Claude nhớ

| Lệnh | Làm gì |
|---|---|
| `/obsidian-save` | Lưu mọi thứ từ cuộc trò chuyện — quyết định, task, người, ý tưởng |
| `/obsidian-ingest` | Drop URL/PDF/audio/screenshot vào → vault TỰ VIẾT LẠI 5-15 trang |
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
| `/obsidian-init` | Tạo `_CLAUDE.md`, `index.md`, `log.md` |

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

### Research — Claude kéo kiến thức về

Cần API key (xAI Grok + Perplexity + YouTube tùy chọn). Kết quả lưu vào `Research/` theo format AI-first.

| Lệnh | Làm gì |
|---|---|
| `/x-read [url]` | Đọc sâu post X — post + thread + TL;DR + claims + sentiment + voices |
| `/x-pulse [topic]` | Quét X xem chủ đề đang hot — themes, voices, hooks, ý tưởng post |
| `/research [topic]` | Web research có trích dẫn — báo cáo + recency markers + câu hỏi mở |
| `/research-deep [topic]` | Vault-first synthesis — chỉ lấp gap, lan tỏa update khắp People/Projects/Ideas |
| `/youtube [url]` | Trích transcript + metadata + comments → AI-first summary |

---

## Cài đặt

**Người dùng phổ thông VN:** xem **[docs/HUONG-DAN-CAI-DAT.md](docs/HUONG-DAN-CAI-DAT.md)** — hướng dẫn từng bước có ảnh, không cần biết tech.

**Power user:** một dòng (giống bản EN):

```bash
curl -fsSL https://raw.githubusercontent.com/andyluu98/ces-second-brain/main/scripts/quick-install.sh | bash
```

Sau đó: `/obsidian-init`

---

## Cách "ra lệnh" trên Claude Desktop

Trên Claude Desktop, gõ `/` để mở menu skill → chọn lệnh muốn chạy → menu hiển thị mô tả tiếng Việt.

Nếu không nhớ tên lệnh, dùng [PHRASEBOOK-VN](docs/PHRASEBOOK-VN.md) — danh sách câu nói tự nhiên VN tương ứng từng lệnh.

Ví dụ: thay vì nhớ `/obsidian-save`, bạn có thể chỉ cần nói:
> "Lưu cuộc trò chuyện này vào vault giúp tôi"

Claude tự hiểu và chạy lệnh tương ứng.

---

## Vault tự sống

Vault truyền thống là tủ hồ sơ. Bạn bỏ vào. Nó nằm im.

Vault này tự viết lại với mỗi input:

- **Nạp nguồn** → trang đã có được viết lại, mâu thuẫn được giải quyết, pattern được tổng hợp
- **Lưu cuộc trò chuyện** → entity, concept, decision phân phối khắp vault
- **Hỏi câu hỏi** → Two-Output Rule: mỗi câu trả lời cũng cập nhật trang
- **Sự kiện thay đổi** → bi-temporal facts theo dõi cả "khi nó đúng" lẫn "khi vault biết". Audit trail đầy đủ.
- **Không làm gì** → background agent + scheduled agents tự duy trì khi bạn ngủ
- **Đợi một tuần** → auto-synthesis tìm pattern xuyên nguồn và viết trang kết nối

Vault sau một tuần khác hẳn vault bạn bắt đầu.

---

## Chọn preset

Chọn role lúc bootstrap. Mỗi preset tạo cấu trúc folder, template, kanban riêng.

| Preset | Dành cho | Kanban style |
|---|---|---|
| **executive** | Founder, operator, manager | OKRs / Quarterly / Weekly |
| **builder** | Developer, engineer, architect | Backlog / Sprint / Done |
| **creator** | Writer, YouTuber, marketer | Ideas / Drafts / Published |
| **researcher** | Academic, analyst, deep-diver | Reading / Processing / Synthesized |

Không chọn preset → vault general-purpose.

---

## FAQ ngắn

**Có cần API key không?**
Không cho 26 lệnh chính. Chỉ 5 lệnh research cần (xAI, Perplexity, YouTube tùy chọn). Không có key thì 5 lệnh đó tự degrade — show thông báo, không vỡ.

**Có chạy trên Windows/Linux được không?**
Vault commands chạy mọi nơi Claude chạy. Research toolkit test trên macOS — Windows/Linux có thể cần điều chỉnh.

**Có an toàn cho vault hiện có không?**
Có. Skill không bao giờ xóa hay sửa note theo cách phá hoại nếu chưa xác nhận. Note cũ giữ nguyên. Note mới theo AI-first. `/obsidian-health` đánh dấu note tiền-AI-first để bạn cập nhật theo lịch của mình.

**Khác Notion AI / Mem chỗ nào?**
Notion AI và Mem là SaaS đóng — họ giữ data. Skill này lưu mọi thứ vào markdown local trong vault Obsidian, không vendor lock-in. AI ở **trên** data, không ở **sau** data.

Đầy đủ FAQ: xem README EN gốc.

---

## Triết lý

Hầu hết công cụ second brain biến bạn thành lao công.

Skill này đảo ngược. Bạn nghĩ, làm, nói. Claude lo memory. Rồi nó dùng memory đó để giúp bạn nghĩ tốt hơn — bề mặt cái bạn sẽ bỏ sót, phản biện cái bạn sẽ giả định, kết nối cái bạn sẽ không bao giờ link, tổng hợp pattern bạn không yêu cầu.

Vault không lớn lên. Nó tiến hóa.

**Note của bạn là moat của bạn.**

Lấy cảm hứng từ [LLM-Wiki của Andrey Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

---

## License

MIT — xem [LICENSE](LICENSE)

## Tác giả gốc

[Eugeniu Ghelbur](https://github.com/eugeniughelbur) — AI Automation Engineer @ Single Grain
