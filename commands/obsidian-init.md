---
description: Quét vault và tạo _CLAUDE.md (sổ tay vận hành), index.md (mục lục), log.md (nhật ký)
---

Use the ces-second-brain skill. Execute `/obsidian-init`:

1. Call `list_files_in_vault()` to map the full vault structure
2. Spawn parallel subagents to discover vault context simultaneously:
   - **Dashboard agent**: read `Home.md` or equivalent dashboard
   - **Templates agent**: read all files in `Templates/`
   - **Boards agent**: read all files in `Boards/`
   - **Samples agent**: read one existing note per major folder to capture naming conventions and frontmatter patterns
3. Merge all agent results into a complete picture of the vault
4. Generate a complete `_CLAUDE.md` using the template in `~/.claude/skills/ces-second-brain/references/claude-md-template.md`, filled with real values from the vault
5. Generate `index.md` at the vault root — a catalog of all pages organized by category:
   - List every note in the vault grouped by folder (Projects, People, Ideas, etc.)
   - Include a one-line description for each note (from frontmatter or first paragraph)
   - Claude reads this file FIRST when navigating the vault — cheaper and faster than searching
   - Format: `- [[Note Name]] — brief description`
6. Generate `log.md` at the vault root — a chronological activity log:
   - Start with a header explaining the format
   - Add an entry for this init: `## [YYYY-MM-DD] init | Vault initialized with _CLAUDE.md, index.md, log.md`
   - Future commands append to this file: every ingest, save, health check, and structural change gets a timestamped entry
   - Format: `## [YYYY-MM-DD] action | Description`
7. Write all three files to the vault root
8. Confirm what was written and tell the user to restart their Claude session so the new file takes effect

If `_CLAUDE.md` already exists: show a diff of what would change and ask before overwriting.
If `index.md` already exists: regenerate it (it's always a fresh catalog of current vault state).
If `log.md` already exists: do NOT overwrite — only append the init entry.

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
