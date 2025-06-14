from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import OWNER


class TEXT:
    START = """
<b>Hi {}, I'm Forward Tag Remover.\n\nForward me some messages, i will remove forward tag from them.\n\nAlso can do it in channels </b>[ <i>Just Make Me Admin</i> ].
"""

class INLINE:
    START_BTN = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(TEXT.DEVELOPER, url=f"tg://user?id={OWNER.ID}"),
            ],
            [
                InlineKeyboardButton(
                    TEXT.UPDATES_CHANNEL, url="https://t.me/+aBVhHRwV_O9jMTc1"
                ),
            ],
            [
                InlineKeyboardButton(
                    TEXT.SOURCE_CODE,
                    url="https://t.me/+aBVhHRwV_O9jMTc1",
                ),
            ],
        ]
    )
