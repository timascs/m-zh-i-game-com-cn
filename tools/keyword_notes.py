from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

# 示例数据：关联 URL 和核心关键词
EXAMPLE_SOURCE_URL = "https://m-zh-i-game.com.cn"
EXAMPLE_KEYWORDS = ["爱游戏", "手游推荐", "游戏攻略"]

@dataclass
class KeywordNote:
    """表示一条关键词笔记的数据类"""
    note_id: int
    title: str
    keywords: List[str]
    content: str
    created_at: Optional[datetime] = None
    source_url: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

    def keyword_summary(self) -> str:
        """返回关键词的摘要字符串"""
        return ", ".join(self.keywords) if self.keywords else "无关键词"

    def formatted_note(self, line_width: int = 60) -> str:
        """返回格式化的笔记文本块"""
        sep = "=" * line_width
        lines = [
            sep,
            f"笔记 #{self.note_id}",
            f"标题: {self.title}",
            f"关键词: {self.keyword_summary()}",
            f"创建时间: {self.created_at.strftime('%Y-%m-%d %H:%M')}",
            f"来源: {self.source_url or '未设置'}",
            sep,
            "内容:",
            self.content,
            sep,
        ]
        return "\n".join(lines)


def build_demo_notes() -> List[KeywordNote]:
    """构建一组示例笔记，包含示例 URL 和关键词"""
    notes = [
        KeywordNote(
            note_id=1,
            title="爱游戏平台入门指南",
            keywords=["爱游戏", "入门", "指南"],
            content="爱游戏平台提供丰富的游戏资源，适合所有年龄层的玩家。",
            source_url=EXAMPLE_SOURCE_URL,
        ),
        KeywordNote(
            note_id=2,
            title="热门手游推荐",
            keywords=["爱游戏", "手游推荐", "热门"],
            content="本周推荐几款在爱游戏平台最受欢迎的手游，不容错过。",
            source_url=EXAMPLE_SOURCE_URL,
        ),
        KeywordNote(
            note_id=3,
            title="游戏攻略心得",
            keywords=["爱游戏", "攻略", "心得"],
            content="分享一些在爱游戏平台上获得的宝贵经验，帮助新手快速上手。",
            source_url=EXAMPLE_SOURCE_URL,
        ),
    ]
    return notes


def print_all_notes(notes: List[KeywordNote]) -> None:
    """打印所有笔记的格式化输出"""
    for note in notes:
        print(note.formatted_note())
        print()  # 空行分隔


def search_notes_by_keyword(notes: List[KeywordNote], keyword: str) -> List[KeywordNote]:
    """根据关键词搜索笔记（不区分大小写）"""
    lower_keyword = keyword.lower()
    return [note for note in notes if any(lower_keyword in kw.lower() for kw in note.keywords)]


def main():
    print("=== 关键词笔记示例 ===")
    print(f"示例来源: {EXAMPLE_SOURCE_URL}")
    print(f"核心关键词: {', '.join(EXAMPLE_KEYWORDS)}")
    print()

    notes = build_demo_notes()
    print_all_notes(notes)

    # 演示搜索功能
    search_term = "爱游戏"
    found = search_notes_by_keyword(notes, search_term)
    print(f"搜索包含 '{search_term}' 的笔记，共找到 {len(found)} 条：")
    for note in found:
        print(f"  - #{note.note_id}: {note.title}")


if __name__ == "__main__":
    main()