---
name: obsidian-export
description: "Xuất snapshot vault có cấu trúc — JSON hoặc markdown phẳng để agent/tool khác đọc được"
---

Use the ces-second-brain skill. Execute `/obsidian-export $ARGUMENTS`:

The optional argument is the format: `json` (default) or `markdown`. 

1. Read `_CLAUDE.md` first if it exists in the vault root
2. Read `index.md` for the full vault catalog

3. Build a structured export by scanning the vault:

   **For each note in wiki/**, extract:
   - `path`: file path relative to vault root
   - `title`: note title (first heading or filename)
   - `type`: from frontmatter tags (entity, concept, project, daily, etc.)
   - `date`: from frontmatter
   - `status`: from frontmatter (if exists)
   - `summary`: first paragraph or first 200 characters of body
   - `links_to`: list of all outgoing `[[wikilinks]]`
   - `linked_from`: list of all incoming links (backlinks)
   - `tags`: all frontmatter tags
   - `frontmatter`: full frontmatter as key-value pairs

4. Output format:

   **JSON** (default):
   ```json
   {
     "vault": "Eugeniu's Vault",
     "exported": "2026-04-07",
     "total_notes": 238,
     "notes": [
       {
         "path": "wiki/entities/Eric Siu.md",
         "title": "Eric Siu",
         "type": "entity",
         "summary": "CEO of Single Grain...",
         "links_to": ["Single Grain", "Centralized API Gateway"],
         "tags": ["entity", "person"]
       }
     ]
   }
   ```
   Save to `_export/vault-snapshot.json`

   **Markdown**:
   A flat markdown file with every note listed with its metadata and summary.
   Save to `_export/vault-snapshot.md`

5. Append to `log.md`: `## [YYYY-MM-DD] export | Vault snapshot exported (format, N notes)`

This file is the bridge between your vault and any other AI tool, automation, or agent. They don't need to know your folder structure. They read the snapshot.

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
