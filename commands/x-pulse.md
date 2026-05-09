---
description: Quét X xem chủ đề đang hot — themes, voices, hooks, ý tưởng post (Grok + Live Search)
---

Use the ces-second-brain skill. Execute `/x-pulse [topic]`:

1. Resolve the topic from the user's argument. Multi-word topics are fine ("AI automation", "vibe coding"). If no topic was given, ask: "What topic should I scan X for?"

2. Run the Python command from the repo root (`~/Projects/personal/ces-second-brain/`):
   ```bash
   uv run -m scripts.research.x_pulse "<topic>"
   ```

3. The script returns a structured pulse: WHAT'S HOT (themes with rep posts + voices), WHAT'S UNDEREXPLORED (gaps), HOOKS THAT ARE WORKING, VOICE & TONE WORKING, POST IDEAS FOR YOU TODAY. Show the full output to the user verbatim.

4. **Default save behavior: saves automatically.** The script writes an AI-first note to `Research/X-pulse/YYYY-MM-DD — <slug>.md` with the AI-first vault rule applied (preamble, frontmatter, recency markers, sources verbatim). It also appends a one-line entry to `log.md`.

5. After printing, mention to the user the file path that was saved (the script prints this on stderr, surface it cleanly).

6. Plain English triggers that route to this command: "what's hot on X about [topic]", "X pulse on [topic]", "what should I post about [topic] today", "scan X for [topic]", "trends on X about [topic]".

7. If the script reports "No active discourse found in last 72h on this topic", offer to either broaden the topic or try `/research [topic]` instead (Perplexity for general web research).

8. If the script fails with a clear error, surface it verbatim. Auto-retry on transient errors is handled inside the script.

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
