from telethon import TelegramClient, events

# ===== إعدادات البوت =====
api_id =19544986                 # ضع هنا API ID
api_hash = '83d3621e6be385938ba3618fa0f0b543'       # ضع هنا API Hash
bot_token = '8426678140:AAG3721Hak7V0u_ACZOl2pQHzMgY7Udxk4k'     # ضع هنا توكن البوت إذا تستخدم بوت
channel_username = 'sutazz'  # قناة الاشتراك الإلزامي

# إنشاء العميل
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# دالة التحقق من الاشتراك
async def is_subscribed(user_id):
    try:
        member = await client.get_participant(channel_username, user_id)
        return True
    except:
        return False

# استقبال كل الرسائل في المجموعات
@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    chat = await event.get_chat()

    # تحقق من أن الرسالة ليست من القناة نفسها أو من المشرفين
    if event.is_group or event.is_channel:
        subscribed = await is_subscribed(sender.id)
        if not subscribed:
            # حذف الرسالة
            try:
                await event.delete()
            except:
                pass
            # إرسال تنبيه الاشتراك
            await client.send_message(chat.id,
                f"عزيزي {sender.first_name}، يرجى الاشتراك أولاً في قناتنا: {channel_username}"
            )

# تشغيل البوت
print("Bot is running...")
client.run_until_disconnected()