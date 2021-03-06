"""
✘ Commands Available -

•`{i}schedule <text/reply to msg> <time>`
    In time u can use second as number, or like 1h or 1m
    eg. `{i}schedule Hello 100` It deliver msg after 100 sec.
    eg. `{i}schedule Hello 1h` It deliver msg after an hour.
"""
from datetime import timedelta

from cython.functions.admins import ban_time

from . import eor, ultroid_cmd


@ultroid_cmd(pattern="schedule ?(.*)", fullsudo=True)
async def _(e):
    x = e.pattern_match.group(1)
    xx = await e.get_reply_message()
    if x and not xx:
        y = x.split(" ")[-1]
        k = x.replace(y, "")
        if y.isdigit():
            await e.client.send_message(
                e.chat_id, k, schedule=timedelta(seconds=int(y))
            )
            await eor(e, get_string("schdl_1"), time=5)
        else:
            try:
                z = await ban_time(e, y)
                await e.client.send_message(e.chat_id, k, schedule=z)
                await eor(e, get_string("schdl_1"), time=5)
            except BaseException:
                await eor(e, get_string("schdl_2"), time=5)
    elif xx and x:
        if x.isdigit():
            await e.client.send_message(
                e.chat_id, xx, schedule=timedelta(seconds=int(x))
            )
            await eor(e, get_string("schdl_1"), time=5)
        else:
            try:
                z = await ban_time(e, x)
                await e.client.send_message(e.chat_id, xx, schedule=z)
                await eor(e, get_string("schdl_1"), time=5)
            except BaseException:
                await eor(e, get_string("schdl_2"), time=5)
    else:
        return await eor(e, get_string("schdl_2"), time=5)
