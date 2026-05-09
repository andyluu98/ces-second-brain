---
description: Hiển thị hoặc cập nhật bảng kanban — đánh dấu việc trễ hạn, cập nhật từ ngữ cảnh trò chuyện
---

Use the obsidian-second-brain skill. Execute `/obsidian-board $ARGUMENTS`:

The optional argument is a board name. Handle typos and partial matches.

1. Read `_CLAUDE.md` first if it exists in the vault root
2. If a board name is given, search `Boards/` for it (fuzzy match)
3. If no name given, list available boards and ask which one
4. Read and display the current board state: columns, item counts, overdue items (past `@{date}`)
5. Ask if the user wants to make updates — if yes, infer changes from conversation context
6. Move completed items to ✅ Done with strikethrough, add new items in the right column
7. Flag any items that are overdue or have been in the same column for more than a week

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` — `## For future Claude` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, mandatory `[[wikilinks]]` for every person/project/concept referenced, sources preserved verbatim with URLs inline, and confidence levels where applicable. The vault is for future-Claude retrieval — not human reading.

---

<!-- vn-directive:v1 -->

**Ngôn ngữ — Vietnamese mode:**

- Trả lời người dùng bằng **tiếng Việt** (kể cả lúc xin xác nhận, báo cáo kết quả, đặt câu hỏi).
- Ghi note vào vault bằng **tiếng Việt**: heading, body, mô tả, tóm tắt.
- Tag values dùng tiếng Việt không dấu, kebab-case (vd: `quyet-dinh`, `du-an`, `nguoi`, `y-tuong`, `bai-hoc`).
- Preamble dùng `## Cho Claude tương lai` thay cho `## For future Claude`.
- Recency marker dạng VN: `(tính đến 2026-05, source.com)` thay cho `(as of 2026-05, source.com)`.
- **Giữ nguyên (KHÔNG dịch):** tên file đã tồn tại, frontmatter keys (`date`, `tags`, `type`, `ai-first`, `status`, `timeline`), target của `[[wikilinks]]` đã có sẵn, URL nguồn nguyên văn, code block, command name (`/obsidian-save`), tên skill (`obsidian-second-brain`).
- Khi tạo wikilink mới: tên hiển thị có thể VN (vd: `[[Anh Minh]]`, `[[Dự án X]]`).
- Status values khi tạo mới: vẫn dùng giá trị chuẩn (`active`, `planning`, `completed`, `archived`, `on-hold`) để tương thích Dataview.
