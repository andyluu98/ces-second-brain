---
description: Bắc cầu hai chủ đề không liên quan qua link graph vault — kích thích tư duy sáng tạo cho ý tưởng mới
---

Use the obsidian-second-brain skill. Execute `/obsidian-connect $ARGUMENTS`:

Two arguments required: the two topics, domains, or note names to connect. If only one is given or none, ask the user for both.

1. Read `_CLAUDE.md` first if it exists in the vault root
2. Parse the two domains from arguments (e.g., `/obsidian-connect "distributed systems" "cooking"`)
3. For each domain, search the vault:
   - Find all notes related to that domain (by title, tags, content)
   - Map their backlinks and outgoing links to build a local cluster
4. Find the bridge:
   - Look for shared links, shared tags, or shared people between the two clusters
   - If a direct path exists in the link graph, trace it and explain each hop
   - If no direct path exists, find the closest semantic overlap — concepts, metaphors, or structural similarities
5. Generate creative connections:
   - **Structural analogy**: how a pattern in domain A maps to domain B (e.g., "load balancing is like mise en place — both are about distributing work before the rush")
   - **Transfer opportunities**: what works in A that could be applied to B
   - **Collision ideas**: new concepts that only exist at the intersection of both
6. Present 3-5 specific, actionable connections — not vague analogies but concrete ideas the user could act on
7. Offer to save the best connections to `Ideas/` with links to both source domains
8. Log the connection exercise in today's daily note

The value is in unexpected links. If the connection is obvious, dig deeper. The best output makes the user say "I never thought of it that way."

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
