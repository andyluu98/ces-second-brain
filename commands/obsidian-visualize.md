---
description: Tạo canvas map vault — nhìn thấy hình dạng second brain và cách kiến thức liên kết
---

Use the obsidian-second-brain skill. Execute `/obsidian-visualize $ARGUMENTS`:

The optional argument is a scope: a project name, entity name, topic, or "full" for the entire vault. Default: full vault.

1. Read `_CLAUDE.md` first if it exists in the vault root
2. Read `index.md` for the full vault catalog

3. Build the graph:
   - If scoped to a topic/project/entity: start from that note, follow all outgoing `[[wikilinks]]` 2 levels deep
   - If full vault: read all notes, map all links between them

4. Generate a JSON Canvas file (`.canvas`) compatible with Obsidian's native canvas viewer:

   Structure:
   ```json
   {
     "nodes": [
       {"id": "1", "type": "file", "file": "wiki/entities/Eric Siu.md", "x": 0, "y": 0, "width": 250, "height": 60},
       {"id": "2", "type": "file", "file": "wiki/projects/Centralized API Gateway.md", "x": 300, "y": 0, "width": 250, "height": 60}
     ],
     "edges": [
       {"id": "e1", "fromNode": "1", "toNode": "2"}
     ]
   }
   ```

   Layout rules:
   - **Hub nodes** (most links) go in the center, larger
   - **Cluster by type**: entities on the left, projects top-right, concepts bottom-right, daily notes bottom
   - **Color by type**: entities = blue, projects = green, concepts = purple, daily = gray, sources = orange
   - **Edge thickness** = number of connections between two nodes (thicker = stronger relationship)
   - **Orphan nodes** placed at the edges with a red border (easy to spot)

5. Save to vault root as `atlas.canvas` (or `atlas-{topic}.canvas` if scoped)

6. Also generate a text summary:
   - Total nodes and edges
   - Top 5 hub nodes (most connected)
   - Orphan nodes (no connections)
   - Clusters found (groups of tightly connected notes)
   - Bridge nodes (connect two otherwise separate clusters)

7. Append to `log.md`: `## [YYYY-MM-DD] visualize | Canvas generated — X nodes, Y edges, Z orphans`

The user can open the `.canvas` file in Obsidian to visually explore their vault's knowledge graph.

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
