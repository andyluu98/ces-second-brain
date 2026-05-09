---
description: Trích transcript, metadata, top comments từ video YouTube — tổng hợp qua Grok rồi lưu vào vault
---

Use the ces-second-brain skill. Execute `/youtube [url]`:

1. Resolve the YouTube URL or video ID from the user's argument. Accept any of: full URL (`https://www.youtube.com/watch?v=...`), `https://youtu.be/...`, `https://www.youtube.com/shorts/...`, or just the 11-character video ID. If no input given, ask: "Which YouTube video?"

2. Run the Python command from the repo root (`~/Projects/personal/ces-second-brain/`):
   ```bash
   uv run -m scripts.research.youtube_extract "<url-or-id>"
   ```

3. The script:
   - Extracts the transcript via `youtube-transcript-api` (free, no API key).
   - If `YOUTUBE_API_KEY` is set, also fetches title, channel, view/like counts, top comments. Otherwise skips metadata silently.
   - Sends the transcript (and optional comments) to Grok for AI-first summarization.
   - Returns: TL;DR, Key Points, Notable Quotes, Themes & Topics, Comment Sentiment, Worth Following Up On.

4. Show the script output verbatim to the user.

5. **Default save behavior: saves automatically.** AI-first note written to `Research/YouTube/YYYY-MM-DD — <video-title-slug>.md`. Frontmatter includes video ID, channel, view counts, etc. for future Dataview queries.

6. Plain English triggers: "summarize this YouTube video", "what's in this video", "extract this YouTube link", "transcribe this video", or just pasting a YouTube URL with a question about content.

7. If the video has no captions (transcript unavailable) AND no metadata (no API key), the script will fail with a clear message — surface it. Suggest the user picks a different video or provides metadata manually.

8. If the user asks to research something mentioned in the "Worth Following Up On" section, route that to `/research [topic]`.

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
