from datetime import datetime
import time
from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP, StartTime
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.keping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**『⍟ᴘᴀɴᴛᴇᴋ』**")
    await pong.edit("**◆◈sᴘᴀᴄᴇ-ʙᴏᴛ◈◆**")
    await pong.edit("**ʟᴇɴʏᴀᴘᴋᴀɴ ᴊᴀᴍᴇᴛ ᴘᴀɴᴛᴇᴋ**")
    await pong.edit("**☬sɪᴀᴘ ᴍᴇᴍʙᴀsᴍɪ ᴘᴀɴᴛᴇᴋ ᴘᴇᴏᴘʟᴇ ᴀsᴜ☬**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**✲ 🅂🄿🄰🄲🄴-🄿🄸🄽🄶** "
                    f"\n ⫸ ᴾᴵᴺᴳᴬˢᵁ `%sms` \n"
                    f"**✲ 🅂🄿🄰🄲🄴-🄽🄰🄼🄴** "

                    f"\n ⫸ ᴱᴷˢᴱᴷᵁᵀᴼᴿ『`{ALIVE_NAME}`』 \n" % (duration))


@register(outgoing=True, pattern='^\\.kntl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**WOY! JAMET KONTOLLL**")
    sleep(3)
    await typew.edit("`KERJAAN CAPER AJA TOLOL!!!`")
    sleep(3)
    await typew.edit("`DASAR JAMET LU KONTOL!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^\\.G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**SI ANGKASA BAWA BOTOL**")
    sleep(3)
    await typew.edit("`KALIAN SEMUA BOCAH TOLOLLL!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^ass(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**sᴀʟᴀᴍ ᴅᴜʟᴜ, ʙɪᴀʀ sᴏᴘᴀɴ ㋛**")
    sleep(3)
    await typew.edit("**ASSALAMUALAIKUM CALON MAYAT**")
# Owner @mixiologist


@register(outgoing=True, pattern='^\\.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**HALO BABUUU! GUA {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`PUNTENNNNN.....`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.usange(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Mendapatkan Informasi...`")
    sleep(1)
    await typew.edit("**PENGGUNAAN SPACE-BOT 🚀**:\n\n╭━━━━━━━━━━━━━━━━━━━━╮\n" f"-> `Penggunaan Dyno ` **{ALIVE_NAME}**:\n" f" •**0 jam - " f"0 menit - 0%**" "\n ◐━─━─━─━─━──━─━─━─━─━◐\n" "-> `Sisa Penggunaan Bulan Ini`:\n" f" •**1000 jam - 0 menit " f"- 100%**\n" "╰━━━━━━━━━━━━━━━━━━━━╯"
                     )
# @mixiologist


CMD_HELP.update({
    "fakedyno":
    "`.usange`\
\nUsage: tipu tipu anjeeeng.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam."
})
