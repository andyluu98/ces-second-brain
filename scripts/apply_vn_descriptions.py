#!/usr/bin/env python3
"""
apply_vn_descriptions.py — Việt hóa frontmatter description + append VN directive
cho 31 file trong commands/.

Chạy: python scripts/apply_vn_descriptions.py
Idempotent: chạy nhiều lần không nhân bản directive.
"""

from __future__ import annotations
from pathlib import Path
import re

# Map filename -> Vietnamese description
VN_DESCRIPTIONS: dict[str, str] = {
    "obsidian-adr.md": "Tạo bản ghi quyết định (ADR) khi cấu trúc vault thay đổi — vault biết vì sao nó được tổ chức như vậy",
    "obsidian-board.md": "Hiển thị hoặc cập nhật bảng kanban — đánh dấu việc trễ hạn, cập nhật từ ngữ cảnh trò chuyện",
    "obsidian-capture.md": "Ghi nhanh ý tưởng — không ma sát, lưu vào Ideas/ và nhắc trong daily note",
    "obsidian-challenge.md": "Phản biện ý tưởng hiện tại bằng lịch sử vault của chính bạn — tìm mâu thuẫn, thất bại quá khứ, giả định sai",
    "obsidian-connect.md": "Bắc cầu hai chủ đề không liên quan qua link graph vault — kích thích tư duy sáng tạo cho ý tưởng mới",
    "obsidian-daily.md": "Tạo hoặc cập nhật daily note hôm nay — kéo lịch, việc trễ hạn, ngữ cảnh trò chuyện vào",
    "obsidian-decide.md": "Trích xuất quyết định từ cuộc trò chuyện này và ghi vào project note phù hợp",
    "obsidian-emerge.md": "Phát hiện pattern chưa được đặt tên trong note gần đây — chủ đề lặp lại, kết nối ẩn, kết luận chưa nói thành lời",
    "obsidian-export.md": "Xuất snapshot vault có cấu trúc — JSON hoặc markdown phẳng để agent/tool khác đọc được",
    "obsidian-find.md": "Tìm kiếm thông minh trong vault — trả về kết quả kèm ngữ cảnh, không chỉ tên file",
    "obsidian-graduate.md": "Nâng cấp ý tưởng phôi thai thành project hoàn chỉnh — tasks, kanban, cấu trúc đầy đủ",
    "obsidian-health.md": "Kiểm tra sức khỏe vault — phân nhóm theo mức độ, tìm mâu thuẫn, thiếu khái niệm, claim cũ, lỗi cấu trúc",
    "obsidian-ingest.md": "Nạp một nguồn vào vault — vault tự viết lại quanh kiến thức mới: cập nhật entity, viết lại claim cũ, tổng hợp khái niệm mới, hòa giải mâu thuẫn",
    "obsidian-init.md": "Quét vault và tạo _CLAUDE.md (sổ tay vận hành), index.md (mục lục), log.md (nhật ký)",
    "obsidian-learn.md": "Rà bài học trong vault, cắt bớt cái cũ, làm nổi pattern đang sống — bài học vault tự cộng dồn hoặc hết hạn",
    "obsidian-log.md": "Ghi log phiên làm việc/dev vào vault — tự suy ra project từ ngữ cảnh",
    "obsidian-person.md": "Tạo hoặc cập nhật note người từ ngữ cảnh trò chuyện",
    "obsidian-project.md": "Tạo hoặc cập nhật project note — tự thêm vào kanban và daily note",
    "obsidian-recap.md": "Tóm tắt khoảng thời gian từ vault — hôm nay, tuần, hoặc tháng",
    "obsidian-reconcile.md": "Tìm và giải quyết mâu thuẫn trong vault — vault tự duy trì sự thật của nó",
    "obsidian-review.md": "Tạo note tổng kết tuần hoặc tháng có cấu trúc từ lịch sử vault",
    "obsidian-save.md": "Lưu mọi thứ đáng giữ từ cuộc trò chuyện này vào vault",
    "obsidian-synthesize.md": "Tổng hợp tự động — quét vault tìm pattern chưa đặt tên và viết trang tổng hợp mà không cần nhờ",
    "obsidian-task.md": "Thêm task vào đúng bảng kanban — tự suy ra mức ưu tiên và hạn chót",
    "obsidian-visualize.md": "Tạo canvas map vault — nhìn thấy hình dạng second brain và cách kiến thức liên kết",
    "obsidian-world.md": "Nạp danh tính, giá trị, ưu tiên, trạng thái hiện tại trong một lần — có cấp độ ngữ cảnh tăng dần để tiết kiệm token",
    "research.md": "Nghiên cứu web có trích dẫn qua Perplexity Sonar — báo cáo sâu: tóm tắt, sự kiện, timeline, nhân vật, phản biện, câu hỏi mở",
    "research-deep.md": "Nghiên cứu sâu ưu tiên vault — quét vault, tìm thiếu sót, lấp qua Perplexity + Grok, tổng hợp delta, lan tỏa cập nhật khắp People/Projects/Ideas qua /obsidian-save",
    "x-pulse.md": "Quét X xem chủ đề đang hot — themes, voices, hooks, ý tưởng post (Grok + Live Search)",
    "x-read.md": "Đọc sâu post X (Twitter) qua Grok + Live Search — post nguyên văn, thread, TL;DR, luận điểm, sentiment phản hồi, voices đáng theo dõi",
    "youtube.md": "Trích transcript, metadata, top comments từ video YouTube — tổng hợp qua Grok rồi lưu vào vault",
}

# Marker to detect prior application
DIRECTIVE_MARKER = "<!-- vn-directive:v1 -->"

DIRECTIVE_BLOCK = f"""

---

{DIRECTIVE_MARKER}

**Ngôn ngữ — Vietnamese mode:**

- Trả lời người dùng bằng **tiếng Việt** (kể cả lúc xin xác nhận, báo cáo kết quả, đặt câu hỏi).
- Ghi note vào vault bằng **tiếng Việt**: heading, body, mô tả, tóm tắt.
- Tag values dùng tiếng Việt không dấu, kebab-case (vd: `quyet-dinh`, `du-an`, `nguoi`, `y-tuong`, `bai-hoc`).
- Preamble dùng `## Cho Claude tương lai` thay cho `## For future Claude`.
- Recency marker dạng VN: `(tính đến 2026-05, source.com)` thay cho `(as of 2026-05, source.com)`.
- **Giữ nguyên (KHÔNG dịch):** tên file đã tồn tại, frontmatter keys (`date`, `tags`, `type`, `ai-first`, `status`, `timeline`), target của `[[wikilinks]]` đã có sẵn, URL nguồn nguyên văn, code block, command name (`/obsidian-save`), tên skill (`ces-second-brain`).
- Khi tạo wikilink mới: tên hiển thị có thể VN (vd: `[[Anh Minh]]`, `[[Dự án X]]`).
- Status values khi tạo mới: vẫn dùng giá trị chuẩn (`active`, `planning`, `completed`, `archived`, `on-hold`) để tương thích Dataview.
"""


def update_file(path: Path, vn_desc: str) -> str:
    """Return status: 'updated' | 'skipped-already-vn' | 'no-change'"""
    text = path.read_text(encoding="utf-8")

    # Replace description in frontmatter (first occurrence between --- ... ---)
    new_text, n = re.subn(
        r"^(---\s*\ndescription:\s*).+?(\n---)",
        rf"\1{vn_desc}\2",
        text,
        count=1,
        flags=re.DOTALL,
    )
    desc_changed = n > 0 and new_text != text

    # Append directive if not already there
    if DIRECTIVE_MARKER not in new_text:
        new_text = new_text.rstrip() + DIRECTIVE_BLOCK
        directive_added = True
    else:
        directive_added = False

    if desc_changed or directive_added:
        path.write_text(new_text, encoding="utf-8")
        flags = []
        if desc_changed:
            flags.append("desc")
        if directive_added:
            flags.append("directive")
        return "updated (" + "+".join(flags) + ")"
    return "no-change"


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    cmd_dir = repo_root / "commands"

    if not cmd_dir.is_dir():
        raise SystemExit(f"commands/ not found at {cmd_dir}")

    print(f"Scanning {cmd_dir}\n")

    missing: list[str] = []
    for fname, vn_desc in VN_DESCRIPTIONS.items():
        fpath = cmd_dir / fname
        if not fpath.exists():
            missing.append(fname)
            print(f"  ! MISSING: {fname}")
            continue
        status = update_file(fpath, vn_desc)
        print(f"  {status:<30} {fname}")

    # Warn about command files that exist but have no VN translation
    existing = {p.name for p in cmd_dir.glob("*.md")}
    untranslated = sorted(existing - set(VN_DESCRIPTIONS.keys()))
    if untranslated:
        print("\nUntranslated command files (add VN to VN_DESCRIPTIONS):")
        for u in untranslated:
            print(f"  - {u}")

    if missing:
        print(f"\nMissing {len(missing)} expected command files.")

    print(f"\nDone. {len(VN_DESCRIPTIONS) - len(missing)} files processed.")


if __name__ == "__main__":
    main()
