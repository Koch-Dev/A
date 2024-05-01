from pyrogram import Client, filters
from pyrogram.types import Message

from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream

CHANNEL_ID = -1001952511944
app = Client(
    'py-tgcalls',
    api_id=21309577,
    api_hash='df2554b54a9eb9e572979b5db2d0cc79',
)
call_py = PyTgCalls(app)
call_py.start()

CHANNEL_ID = -1001952511944

@app.on_message(filters.command('live') & filters.incoming & ~filters.user(5218610039))
async def stream(client, m: Message):
    chat_id = m.chat.id
    if len(m.command) < 2:
        await m.reply("`Give A Link/LiveLink/.m3u8 URL/YTLink to Play Audio from 🎶`")
    else: 
        link = m.text.split(None, 1)[1]
        huehue = await m.reply("`Trying to Play 📻`")         
        try:
            await call_py.join_group_call(
                CHANNEL_ID,
                MediaStream(
                    link,            
                    video_flags=MediaStream.IGNORE,
                ), 
            ) 
            add_to_queue(chat_id, "Radio 📻", link, link, "Audio", 0)
            await huehue.edit(f"Started Playing **[Radio 📻]({link})** in `{chat_id}`", disable_web_page_preview=True)
        except Exception as ep:
            await huehue.edit(f"`{ep}`")

idle()
