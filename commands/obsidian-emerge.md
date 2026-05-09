---
description: Phát hiện pattern chưa được đặt tên trong note gần đây — chủ đề lặp lại, kết nối ẩn, kết luận chưa nói thành lời
---

Use the ces-second-brain skill. Execute `/obsidian-emerge $ARGUMENTS`:

The optional argument is a timeframe (e.g., "2 weeks", "this month"). Default: last 30 days.

1. Read `_CLAUDE.md` first if it exists in the vault root
2. Determine the date range from the argument (default: last 30 days)
3. Spawn parallel subagents to read vault content from the period:
   - **Daily notes agent**: read all daily notes in the date range, extract recurring topics, complaints, observations, and energy patterns
   - **Dev logs agent**: read all dev logs in the range, extract repeated blockers, tools mentioned, architectural patterns
   - **Decisions agent**: read Key Decisions sections across project notes, look for directional trends
   - **Ideas agent**: read Ideas/ notes created in the range, look for thematic clusters
4. Merge results and identify:
   - **Recurring themes**: topics that appeared 3+ times without being named as a priority
   - **Emotional patterns**: what energizes vs. drains the user (based on language and context)
   - **Unnamed conclusions**: things the notes imply but never state outright (e.g., "you've mentioned onboarding friction in 4 different projects — this is a systemic issue, not a project-specific one")
   - **Emerging directions**: where the vault suggests the user is heading, even if they haven't committed to it
5. Present findings as a structured "Pattern Report" — each pattern gets: the evidence (cited notes), the interpretation, and a suggested action
6. Offer to save the pattern report to `Ideas/` or a relevant project note
7. Log a brief summary in today's daily note

The goal is insight the user cannot see themselves. Do not restate what they already know — surface what they haven't named yet.

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
