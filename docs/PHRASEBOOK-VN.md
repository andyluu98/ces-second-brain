# Phrasebook — 30 câu nói tiếng Việt tự nhiên

> Không nhớ slash command? Cứ chat tự nhiên với Claude. Claude hiểu các câu sau và tự gọi đúng skill.

> **Cách dùng:** mở Claude Desktop, copy câu cột giữa, paste vào chat. Hoặc gõ slash trực tiếp ở cột phải nếu nhớ.

---

## Lưu thông tin

| Nhu cầu | Câu nói tự nhiên VN | Slash tương đương |
|---|---|---|
| Lưu mọi thứ từ cuộc trò chuyện | "Lưu cuộc trò chuyện này vào vault" hoặc "Cất trữ thông tin trong cuộc trò chuyện này lại giúp tôi" | `/obsidian-save` |
| Lưu một quyết định cụ thể | "Ghi quyết định vừa rồi vào vault, gắn vào dự án [X]" | `/obsidian-decide [X]` |
| Lưu nhanh một ý tưởng | "Capture ý tưởng: [nội dung]" hoặc "Lưu nhanh ý tưởng này: ..." | `/obsidian-capture [nội dung]` |
| Lưu phiên dev/làm việc | "Log phiên làm việc này, tôi đang làm dự án [X]" | `/obsidian-log` |
| Thêm task vào kanban | "Thêm task: [mô tả], hạn [ngày], ưu tiên cao" | `/obsidian-task [mô tả]` |
| Lưu/cập nhật người | "Tạo note cho anh Minh — anh ấy là CTO của Acme, vừa gặp hôm nay" | `/obsidian-person Minh` |
| Lưu/cập nhật project | "Tạo project note cho 'Ra mắt sản phẩm Q3'" | `/obsidian-project [tên]` |

## Daily / hằng ngày

| Nhu cầu | Câu nói tự nhiên VN | Slash tương đương |
|---|---|---|
| Tạo daily note hôm nay | "Tạo note hôm nay" hoặc "Mở daily note cho hôm nay" | `/obsidian-daily` |
| Xem daily note đã có gì chưa | "Hôm nay tôi đã ghi gì rồi?" | `/obsidian-daily` |
| Bắt đầu phiên làm việc mới | "Tôi đang làm gì hôm qua tới giờ?" | `/obsidian-world` |

## Tìm kiếm và tổng kết

| Nhu cầu | Câu nói tự nhiên VN | Slash tương đương |
|---|---|---|
| Tìm thông tin trong vault | "Tìm cho tôi mọi thứ về [chủ đề]" | `/obsidian-find [chủ đề]` |
| Tóm tắt tuần này | "Tổng kết tuần này tôi đã làm gì" | `/obsidian-recap week` |
| Tóm tắt tháng | "Recap tháng vừa rồi" | `/obsidian-recap month` |
| Tổng kết tuần có cấu trúc | "Viết review tuần cho tôi" | `/obsidian-review` |
| Xem kanban | "Cho tôi xem board [tên]" | `/obsidian-board [tên]` |

## Tư duy

| Nhu cầu | Câu nói tự nhiên VN | Slash tương đương |
|---|---|---|
| Phản biện ý tưởng | "Tôi đang định [làm gì]. Hãy tìm trong vault xem tôi đã từng thử và thất bại chưa" | `/obsidian-challenge` |
| Tìm pattern ẩn | "Trong 30 ngày qua tôi có pattern gì lặp lại mà tôi chưa nhận ra?" | `/obsidian-emerge` |
| Bắc cầu hai chủ đề | "Liên kết [chủ đề A] và [chủ đề B] cho tôi" | `/obsidian-connect "A" "B"` |
| Nâng ý tưởng thành project | "Lấy ý tưởng [tên] và biến thành project có roadmap" | `/obsidian-graduate [tên]` |

## Nạp nguồn (ingest)

| Nhu cầu | Câu nói tự nhiên VN | Slash tương đương |
|---|---|---|
| Nạp 1 video YouTube | "Nạp video này vào vault: [URL]" | `/obsidian-ingest [URL]` |
| Nạp PDF | "Đọc và lưu PDF này vào vault: [đường dẫn]" | `/obsidian-ingest [path]` |
| Nạp audio | "Transcribe và lưu audio này: [path]" | `/obsidian-ingest [path]` |
| Nạp screenshot | "Đọc ảnh whiteboard này và tạo concept notes" | `/obsidian-ingest [path]` |

## Research (cần API key)

| Nhu cầu | Câu nói tự nhiên VN | Slash tương đương |
|---|---|---|
| Đọc 1 post X | "Phân tích post X này: [URL]" | `/x-read [URL]` |
| Quét X xem trending | "Trên X, chủ đề [X] đang hot gì?" | `/x-pulse [X]` |
| Research web | "Research giúp tôi về [chủ đề]" | `/research [chủ đề]` |
| Research sâu, biết vault | "Research sâu [chủ đề], xem vault tôi đã biết gì rồi và chỉ tìm phần thiếu" | `/research-deep [chủ đề]` |
| Tóm tắt YouTube | "Tóm tắt video YouTube này: [URL]" | `/youtube [URL]` |

## Bảo trì vault

| Nhu cầu | Câu nói tự nhiên VN | Slash tương đương |
|---|---|---|
| Audit vault | "Vault có vấn đề gì không, mâu thuẫn ở đâu?" | `/obsidian-health` |
| Hòa giải mâu thuẫn | "Tìm các thông tin trái ngược trong vault và xử lý" | `/obsidian-reconcile` |
| Tổng hợp tự động | "Quét vault và tự viết trang tổng hợp pattern mới" | `/obsidian-synthesize` |
| Visualize vault | "Tạo canvas map cho vault tôi xem hình dạng" | `/obsidian-visualize` |
| Xuất snapshot | "Export vault dạng JSON cho tôi" | `/obsidian-export` |

## Khởi tạo / setup

| Nhu cầu | Câu nói tự nhiên VN | Slash tương đương |
|---|---|---|
| Tạo _CLAUDE.md cho vault | "Quét vault tôi và tạo sổ tay vận hành" | `/obsidian-init` |
| Tạo ADR (decision record) | "Ghi ADR cho quyết định cấu trúc vừa rồi" | `/obsidian-adr` |
| Rà bài học | "Bài học vault tôi cái nào còn đúng, cái nào hết hạn?" | `/obsidian-learn` |

---

## Mẹo dùng phrasebook

1. **Không cần thuộc lòng** — câu cột giữa chỉ là gợi ý. Claude hiểu nhiều cách diễn đạt.
2. **Càng cụ thể càng tốt** — "lưu quyết định về ngân sách Q3 vào dự án X" tốt hơn "lưu cái này".
3. **Nếu Claude làm sai** — nói "không, ý tôi là [làm rõ]". Claude sửa.
4. **Slash command vẫn nhanh hơn** — khi đã quen, gõ `/obsidian-save` nhanh hơn nói cả câu.
5. **Vẫn được trộn** — "lưu cuộc trò chuyện này, tập trung vào quyết định về Q3" — Claude tự gọi `/obsidian-save` với context bạn vừa cho.

---

## Lệnh tổng hợp (gộp nhiều bước)

Một số kịch bản phổ biến — bạn có thể nói trong 1 câu:

**Sau cuộc họp:**
> "Lưu cuộc trò chuyện này, tạo daily note hôm nay nếu chưa có, và liệt kê 3 task cần làm tiếp."

**Đầu tuần:**
> "Cho tôi xem tuần trước đã làm gì, tuần này có project nào active, và task nào trễ hạn."

**Trước cuộc họp lớn:**
> "Tôi sắp họp với anh Minh — load mọi thứ vault biết về anh ấy + lịch sử tương tác."

**Brainstorm sản phẩm mới:**
> "Tôi đang nghĩ làm [sản phẩm X]. Phản biện giúp tôi bằng vault, rồi nếu vẫn ổn thì graduate ý tưởng thành project."

Claude tự chia thành nhiều bước (chạy `/obsidian-save`, `/obsidian-daily`, `/obsidian-find`, vv) và báo cáo cuối.
