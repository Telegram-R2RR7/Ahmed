#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/X2RZ7WXBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/X2RZ7WXBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from X2RZ7WX import LOGGER, app, userbot
from X2RZ7WX.core.call import Yukki
from X2RZ7WX.plugins import ALL_MODULES
from X2RZ7WX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("X2RZ7WX").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("X2RZ7WX").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("X2RZ7WX.plugins" + all_module)
    LOGGER("X2RZ7WX.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Yukki.start()
    try:
        await Yukki.stream_call(
            "http://king4k.one/play/live.php?mac=00:1a:79:00:00:55&stream=677337&extension=m3u8&play_token=BCyc0keDpi"
        )
    except NoActiveGroupCall:
        LOGGER("X2RZ7WX").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Yukki.decorators()
    LOGGER("X2RZ7WX").info("Yukki Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("X2RZ7WX").info("Stopping Yukki Music Bot! GoodBye")
