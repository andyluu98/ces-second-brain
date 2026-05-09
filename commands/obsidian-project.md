---
description: Tạo hoặc cập nhật project note — tự thêm vào kanban và daily note
---

Use the ces-second-brain skill. Execute `/obsidian-project $ARGUMENTS`:

The argument is a project name. Handle typos and partial matches.

1. Read `_CLAUDE.md` first if it exists in the vault root
2. Search the vault for an existing project matching the name (fuzzy — handle typos)
3. If found: show what was found, confirm with user, then update with new info from conversation
4. If not found: create `Projects/Project Name.md` with full frontmatter schema (`date`, `tags: [project]`, `status: active`, `job`)
5. Fill in everything inferable from the conversation: description, goals, key people, current status
6. Add a card to the relevant kanban board in the `📥 Backlog` or `🔨 In Progress` column
7. Link from today's daily note

If the name has a typo or is approximate, search the vault, show what was found, and confirm before proceeding. Never silently create a note with a misspelled name.

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
- **Giữ nguyên (KHÔNG dịch):** tên file đã tồn tại, frontmatter keys (`date`, `tags`, `type`, `ai-first`, `status`, `timeline`), target của `[[wikilinks]]` đã có sẵn, URL nguồn nguyên văn, code block, command name (`/obsidian-save`), tên skill (`ces-second-brain`).
- Khi tạo wikilink mới: tên hiển thị có thể VN (vd: `[[Anh Minh]]`, `[[Dự án X]]`).
- Status values khi tạo mới: vẫn dùng giá trị chuẩn (`active`, `planning`, `completed`, `archived`, `on-hold`) để tương thích Dataview.
