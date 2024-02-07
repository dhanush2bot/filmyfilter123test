from pyrogram import Client, filters

@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message and message.reply_to_message.sticker:
        sticker = message.reply_to_message.sticker
        await message.reply(
            f"**Sticker ID:** `{sticker.file_id}`\n\n"
            f"**Unique ID:** `{sticker.file_unique_id}`\n\n"
            f"**Dimensions:** {sticker.width}x{sticker.height}\n\n"
            f"**File Size:** {sticker.file_size} bytes",
            quote=True
        )
    elif message.reply_to_message:
        await message.reply("<b>Oops! The replied message is not a sticker.</b>")
    else:
        await message.reply("<b>Please reply to a sticker to get its ID.</b>")
