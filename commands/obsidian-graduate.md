---
description: Nâng cấp ý tưởng phôi thai thành project hoàn chỉnh — tasks, kanban, cấu trúc đầy đủ
---

Use the obsidian-second-brain skill. Execute `/obsidian-graduate $ARGUMENTS`:

The optional argument is the idea title, tag, or keyword. If not provided, scan recent notes for ideas tagged `#idea` or in the `Ideas/` folder and present them for selection.

1. Read `_CLAUDE.md` first if it exists in the vault root
2. Find the idea to graduate:
   - If argument given: search `Ideas/`, daily notes, and captures for a matching idea (fuzzy match)
   - If no argument: list recent ideas (last 14 days) and ask the user to pick one
3. Read the full idea note and any linked notes for context
4. Research the vault for related content:
   - Existing projects that overlap
   - People who were mentioned in connection with this idea
   - Past decisions that relate
   - Similar ideas that were previously explored (to avoid reinventing)
5. Generate a full project spec:
   - **Project note** in `Projects/` with complete frontmatter (date, tags, status: planning, linked idea)
   - **Description**: what this project is and why it matters
   - **Goals**: 3-5 concrete outcomes
   - **Key tasks**: broken into phases with priorities
   - **Open questions**: what still needs answering
   - **Related notes**: links to everything relevant found in step 4
6. Create board entries:
   - Add a card to the relevant kanban board in `Backlog` or `This Week`
   - Add individual task cards if multiple phases
7. Update the original idea note:
   - Add `status: graduated` to frontmatter
   - Add a link to the new project note
8. Link the new project from today's daily note
9. Report: what was created, what was linked, what needs the user's input

The idea doesn't die — it evolves. The original note stays as the origin story, the project note becomes the execution plan.

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
