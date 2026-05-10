---
name: obsidian-challenge
description: "Phản biện ý tưởng hiện tại bằng lịch sử vault của chính bạn — tìm mâu thuẫn, thất bại quá khứ, giả định sai"
---

Use the ces-second-brain skill. Execute `/obsidian-challenge $ARGUMENTS`:

The optional argument is the idea, belief, or plan to challenge. If not provided, infer the user's current position from conversation context.

1. Read `_CLAUDE.md` first if it exists in the vault root
2. Identify the user's current claim, plan, or assumption — either from the argument or from recent conversation
3. Extract the key premises behind that position
4. Search the vault for counter-evidence — spawn parallel subagents:
   - **Decisions agent**: search Key Decisions sections in project notes for past decisions that contradicted or reversed similar thinking
   - **Failures agent**: search dev logs, daily notes, and archives for past failures, regrets, or lessons learned related to this topic
   - **Contradictions agent**: search for notes where the user held the opposite position or flagged risks about this exact approach
5. Synthesize a structured "Red Team" analysis:
   - **Your position**: restate the claim clearly
   - **Counter-evidence from your vault**: cite specific notes, dates, and quotes
   - **Blind spots**: what the user might be ignoring based on their own history
   - **Verdict**: is this position consistent with past experience, or does the vault suggest caution?
6. Log the challenge in today's daily note under a Thinking section

Do not be agreeable. The entire point is to pressure-test. Cite specific vault files. If you find nothing contradictory, say so honestly — but search thoroughly first.

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
