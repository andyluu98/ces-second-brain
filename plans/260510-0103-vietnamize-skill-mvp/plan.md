# Plan: Việt hóa ces-second-brain (MVP)

**Date:** 2026-05-10
**Branch:** main
**Target user:** Người dùng phổ thông VN, không rành tech
**Primary surface:** Claude Desktop (Claude Code phụ)

## Quyết định scope (đã chốt với user)

| Câu hỏi | Quyết định |
|---|---|
| App Claude | Claude Desktop chính, Claude Code phụ |
| Đối tượng | Người dùng phổ thông VN, không rành tech |
| Cách ra lệnh | Slash commands (Desktop hỗ trợ skills) |
| Tên slash | EN giữ nguyên, mô tả VN |
| Ngôn ngữ note | Tiếng Việt hoàn toàn |
| MVP gồm | (1) README-vi.md (2) Hướng dẫn cài đặt VN (3) Phrasebook VN (4) Dịch 31 command descriptions + chỉ thị VN |
| MVP KHÔNG gồm | Setup wizard Python (skip lần này) |

## Phases

- **Phase 1:** Dịch 31 command frontmatter description + thêm chỉ thị "trả lời VN, ghi note VN" vào mỗi command
- **Phase 2:** README-vi.md ở root (link từ README chính)
- **Phase 3:** docs/HUONG-DAN-CAI-DAT.md — hướng dẫn từng bước cài Obsidian + Claude Desktop + mcp-obsidian + skill
- **Phase 4:** docs/PHRASEBOOK-VN.md — 30 câu mẫu user gọi slash bằng VN tự nhiên

## Files được sửa/tạo

```
commands/*.md                           [31 files] description VN + directive VN
README-vi.md                            [new]
docs/HUONG-DAN-CAI-DAT.md               [new]
docs/PHRASEBOOK-VN.md                   [new]
scripts/apply_vn_descriptions.py        [new] one-shot script áp dụng dịch
```

## Nguyên tắc

- KHÔNG sửa SKILL.md, references/, scripts/bootstrap_vault.py — giữ EN cho Claude
- KHÔNG đổi tên file commands/*.md
- KHÔNG xóa nội dung EN gốc trong command body — chỉ APPEND directive VN
- README-vi.md ở root để dễ tìm

## Success criteria

1. User VN gõ `/` trên Claude Desktop → menu hiển thị 31 mô tả VN
2. Sau khi chạy lệnh, Claude trả lời VN, ghi note VN vào vault
3. Người mới hoàn toàn đọc docs/HUONG-DAN-CAI-DAT.md → cài được từ A→Z mà không cần hỏi
4. Phrasebook giúp user gọi lệnh không cần nhớ slash chính xác

## Open questions (nếu có)

- (resolved) Push GitHub PR upstream? → Chưa quyết, làm local trước
