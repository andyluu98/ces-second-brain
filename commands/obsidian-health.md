---
description: Kiểm tra sức khỏe vault — phân nhóm theo mức độ, tìm mâu thuẫn, thiếu khái niệm, claim cũ, lỗi cấu trúc
---

Use the ces-second-brain skill. Execute `/obsidian-health`:

1. Read `_CLAUDE.md` first to find the vault path
2. Run: `python ~/.claude/skills/ces-second-brain/scripts/vault_health.py --path ~/path/to/vault --json`
   (replace vault path with the one from `_CLAUDE.md`)
3. Parse the JSON output and split findings into categories
4. Spawn parallel subagents to handle each category simultaneously:
   - **Links agent**: verify broken links, attempt to resolve them
   - **Duplicates agent**: confirm duplicates are truly the same concept, not just similar names
   - **Frontmatter agent**: identify notes missing required fields by type
   - **Staleness agent**: check overdue tasks and unfilled template syntax
   - **Orphans agent**: check orphaned notes and empty folders
   - **Contradictions agent**: scan Key Decisions sections and Knowledge/ notes for claims that conflict with each other or have been superseded by newer sources
   - **Concept gaps agent**: find terms mentioned 3+ times across different notes that lack a dedicated page — these are missing concepts the vault should have
   - **Stale claims agent**: compare Knowledge/ notes against their source dates — flag any note older than 6 months that references fast-moving topics (tools, APIs, pricing, team structure)
5. Merge results and group by severity:
   - 🔴 Critical: broken links, unfilled template syntax, contradictions between notes
   - 🟡 Warning: duplicates, stale tasks, missing frontmatter, stale claims, concept gaps
   - ⚪ Info: orphaned notes, empty folders
6. For safe fixes (missing frontmatter, obvious duplicates, creating pages for concept gaps), offer to fix automatically
7. For destructive fixes (archiving, merging, resolving contradictions), list them and ask for explicit confirmation first
8. Append to `log.md`: `## [YYYY-MM-DD] health | X critical, Y warnings, Z info`

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
