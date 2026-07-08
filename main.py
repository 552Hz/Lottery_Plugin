from __future__ import annotations

from pathlib import Path

from astrbot.api import logger
from astrbot.api.event import AstrMessageEvent, filter
from astrbot.api.star import Context, Star

from .fortune_card import FortuneCardGenerator


class IdolFortunePlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.generator = FortuneCardGenerator(Path(__file__).parent / "cache")

    @filter.command("抽签")
    async def draw_fortune(self, event: AstrMessageEvent):
        """@机器人后发送 /抽签，返回当天固定的地下偶像运势图。"""
        if not _is_private_message(event) and not _is_at_bot(event):
            yield event.plain_result("请先 @ 我，再发送 /抽签。")
            return

        user_id = str(event.get_sender_id())
        try:
            image_path = self.generator.get_or_create(user_id)
        except Exception as exc:  # pragma: no cover - runtime guard for bot stability.
            logger.exception("生成抽签图片失败: %s", exc)
            yield event.plain_result("抽签图片生成失败了，请稍后再试。")
            return

        yield event.image_result(str(image_path))
        event.stop_event()

    async def terminate(self):
        """插件卸载/停用时调用。"""


def _is_private_message(event: AstrMessageEvent) -> bool:
    message_obj = getattr(event, "message_obj", None)
    group_id = getattr(message_obj, "group_id", "")
    return not group_id


def _is_at_bot(event: AstrMessageEvent) -> bool:
    message_obj = getattr(event, "message_obj", None)
    if message_obj is None:
        return False

    self_id = str(getattr(message_obj, "self_id", "") or "")
    for segment in getattr(message_obj, "message", []) or []:
        segment_type = str(getattr(segment, "type", "") or getattr(segment, "type_", "")).lower()
        qq = getattr(segment, "qq", None)
        if segment_type == "at" and (not self_id or str(qq) == self_id or str(qq).lower() == "all"):
            return True
    return False
