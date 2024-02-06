import os
import logging
import random, string
import asyncio
import time
import datetime
from Script import script
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired, FloodWait, ButtonDataInvalid
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id, delete_files
from database.users_chats_db import db
from pyrogram.types import CallbackQuery
from pyrogram.types import Message
from database.connections_mdb import active_connection
from info import INDEX_CHANNELS, ADMINS, IS_VERIFY, VERIFY_TUTORIAL, VERIFY_EXPIRE, TUTORIAL, SHORTLINK_API, SHORTLINK_URL, AUTH_CHANNEL, DELETE_TIME, SUPPORT_LINK, UPDATES_LINK, LOG_CHANNEL, PICS, PROTECT_CONTENT, DATABASE_URL
from utils import get_settings, get_size, is_subscribed, is_check_admin, get_shortlink, get_verify_status, update_verify_status, save_group_settings, temp, get_readable_time, get_wish, get_seconds
import re
import json
import base64
import sys
from shortzy import Shortzy
from telegraph import upload_file


@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        if not await db.get_chat(message.chat.id):
            total = await client.get_chat_members_count(message.chat.id)
            username = f'@{message.chat.username}' if message.chat.username else 'Private'
            await client.send_message(LOG_CHANNEL, script.NEW_GROUP_TXT.format(message.chat.title, message.chat.id, username, total))       
            await db.add_chat(message.chat.id, message.chat.title)
        wish = get_wish()
        btn = [[
            InlineKeyboardButton('• ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ •', url=UPDATES_LINK)
        ],[
            InlineKeyboardButton('• Support Group •', url=SUPPORT_LINK)
        ]]
        await message.reply(text=f"<b>ʜᴇʏ {message.from_user.mention}, <i>{wish}</i>\nʜᴏᴡ ᴄᴀɴ ɪ ʜᴇʟᴘ ʏᴏᴜ??</b>", reply_markup=InlineKeyboardMarkup(btn))
        return 
        
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.NEW_USER_TXT.format(message.from_user.mention, message.from_user.id))

    verify_status = await get_verify_status(message.from_user.id)
    if verify_status['is_verified'] and VERIFY_EXPIRE < (time.time() - verify_status['verified_time']):
        await update_verify_status(message.from_user.id, is_verified=False)
    
    if (len(message.command) != 2) or (len(message.command) == 2 and message.command[1] == 'start'):
        buttons = [[
            InlineKeyboardButton('◈ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ◈', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
                ],[
                    InlineKeyboardButton('• ꜱᴜᴘᴘᴏʀᴛ ', callback_data="my_about"),
                    InlineKeyboardButton('ᴀʙᴏᴜᴛ •', callback_data='about')
                ],[
                    InlineKeyboardButton('• ʜᴇʟᴘ', callback_data='help'),
                    InlineKeyboardButton('ᴇᴀʀɴ ᴍᴏɴᴇʏ •', callback_data='earn')
                ],[
                    InlineKeyboardButton('• Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ •', url=UPDATES_LINK)
                ],[
                    InlineKeyboardButton('💳 ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ : ʀᴇᴍᴏᴠᴇ ᴀᴅs 💳', callback_data='show_plans')
                  ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        m=await message.reply_sticker("CAACAgIAAxkBAAISdmW_9zmwLSbYb-Z7jGvhC_mPSB9qAAK8AAMw1J0Rd5meEIvSc6IeBA") 
        await asyncio.sleep(1)
        await m.delete()
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, get_wish()),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return

    btn = await is_subscribed(client, message) # This func is for AUTH_CHANNEL
    mc = message.command[1]
    if btn:
        if mc != 'subscribe':
            try:
                btn.append(
                    [InlineKeyboardButton("🔁 Try Again 🔁", callback_data=f"pm_checksub#{mc}")]
                )
            except ButtonDataInvalid:
                btn.append(
                    [InlineKeyboardButton("🔁 Try Again 🔁", url=f"https://t.me/{temp.U_NAME}?start={mc}")]
                )
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=f"👋 Hello {message.from_user.mention},\n\nPlease join my 'Updates Channel' and request again. 😇",
            reply_markup=InlineKeyboardMarkup(btn)
        )
        return

    if mc.startswith('verify'):
        _, token = mc.split("_", 1)
        verify_status = await get_verify_status(message.from_user.id)
        if verify_status['verify_token'] != token:
            return await message.reply("Your verify token is invalid.")
        await update_verify_status(message.from_user.id, is_verified=True, verified_time=time.time())
        if verify_status["link"] == "":
            reply_markup = None
        else:
            btn = [[
                InlineKeyboardButton("📌 Get File 📌", url=f'https://t.me/{temp.U_NAME}?start={verify_status["link"]}')
            ]]
            reply_markup = InlineKeyboardMarkup(btn)
        await message.reply_photo(
            photo = "https://telegra.ph//file/14702e8bff87388acc340.jpg",
            caption = f"**✅ Congratulations on Your Successful Verification! Enjoy Unlimited Access to Movies and Series!{get_readable_time(VERIFY_EXPIRE)} \n\n ✅ ನಿಮ್ಮ ಯಶಸ್ವಿ ಪರಿಶೀಲನೆಗೆ ಅಭಿನಂದನೆಗಳು! ಚಿತ್ರಗಳು ಮತ್ತು ಸಿರಿಸ್ ಗಳಿಗೆ ಅನಂತ ಪ್ರವೇಶವನ್ನು ಆನಂದಿಸಿ! {get_readable_time(VERIFY_EXPIRE)} \n\n ✅ आपकी सफलतापूर्वक सत्यापन पर बधाई! फिल्मों और सीरीज का अनलिमिटेड एक्सेस का आनंद लें! {get_readable_time(VERIFY_EXPIRE)}\n**", 
            reply_markup=reply_markup
        )
        return
    
    verify_status = await get_verify_status(message.from_user.id)
    if not await db.has_premium_access(message.from_user.id):
        if IS_VERIFY and not verify_status['is_verified']:
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            await update_verify_status(message.from_user.id, verify_token=token, link="" if mc == 'inline_verify' else mc)
            loading_msg1 = await message.reply("⏳ 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐲𝐨𝐮𝐫 𝐯𝐞𝐫𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐬𝐭𝐚𝐭𝐮𝐬...")
            await asyncio.sleep(0.9)
            loading_msg2 = await message.reply("🔗 𝐒𝐞𝐧𝐝𝐢𝐧𝐠 𝐯𝐞𝐫𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐥𝐢𝐧𝐤...")
            await asyncio.sleep(1)
            await loading_msg1.delete()
            await loading_msg2.delete()
            link = await get_shortlink(SHORTLINK_URL, SHORTLINK_API, f'https://t.me/{temp.U_NAME}?start=verify_{token}')
            btn = [[
                InlineKeyboardButton("Click Here To Verify ✓", url=link)
            ],[
                InlineKeyboardButton('How To Verify ❓', url=VERIFY_TUTORIAL)
            ]]
            await message.reply_photo(
                photo = "https://telegra.ph//file/c9f2933c392a9b3a58854.jpg",
                caption = "❌ You Are Not Verified For Today ! Kindly Verify Now For Access To Your Movie \n\n ❌ ನೀವು ಇಂದಿನ ಪರಿಶೀಲಿಸಲ್ಪಡದಿದ್ದೀರಿ! ದಯವಿಟ್ಟು ಈಗ ನಿಮ್ಮ ಚಿತ್ರಗಳಿಗೆ ಪ್ರವೇಶಿಸಲು ಪರಿಶೀಲಿಸಿ \n\n ❌ आप आज के लिए सत्यापित नहीं हैं! कृपया अब अपनी मूवी के लिए सत्यापित करें\n",
                reply_markup=InlineKeyboardMarkup(btn)                
            )
            return
 
    if mc.startswith('all'):
        type_, grp_id, key = mc.split("_", 2)
        files = temp.FILES.get(key)
        if not files:
            return await message.reply('No Such All Files Exist!')
        settings = await get_settings(int(grp_id))
        if not await db.has_premium_access(message.from_user.id):            
            if type_ != 'all-file' and settings['shortlink']:
                link = await get_shortlink(settings['url'], settings['api'], f"https://t.me/{temp.U_NAME}?start=all-file_{grp_id}_{key}")
                btn = [[
                    InlineKeyboardButton("♻️ Get File ♻️", url=link)
                ],[
                    InlineKeyboardButton("📍 ʜᴏᴡ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ 📍", url=settings['tutorial'])
                ]]
                await message.reply(f"ALL Your File Is Ready, Please Get Using This Link. 👍", reply_markup=InlineKeyboardMarkup(btn), protect_content=True)
                return
            else:
                pass 
        for file in files:
            CAPTION = settings['caption']
            f_caption = CAPTION.format(
                file_name = file.file_name,
                file_size = get_size(file.file_size),
                file_caption=file.caption
            )   
            btn = [[
                InlineKeyboardButton("ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 👀 / ꜰᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ 🗂️", callback_data="stream_button")
            ],[
                InlineKeyboardButton('⁉️ ᴄʟᴏsᴇ ⁉️', callback_data='close_data')
            ]]
            await client.send_cached_media(
                chat_id=message.from_user.id,
                file_id=file.file_id,
                caption=f_caption,
                protect_content=settings['file_secure'],
                reply_markup=InlineKeyboardMarkup(btn)
            )
        return

    type_, grp_id, file_id = mc.split("_", 2)
    files_ = await get_file_details(file_id)
    if not files_:
        return await message.reply('No Such File Exist!')
    files = files_[0]
    settings = await get_settings(int(grp_id))
    if not await db.has_premium_access(message.from_user.id):        
        if type_ != 'shortlink' and settings['shortlink']:
            link = await get_shortlink(settings['url'], settings['api'], f"https://t.me/{temp.U_NAME}?start=shortlink_{grp_id}_{file_id}")
            btn = [[
                InlineKeyboardButton("♻️ ʏᴏᴜʀ ꜰɪʟᴇ ♻️", url=link)
            ],[
                InlineKeyboardButton("❓ ʜᴏᴡ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ ❓", url=settings['tutorial'])
            ]]
            await message.reply(f"**[{get_size(files.file_size)}] {files.file_name}**\n\n**𝚈𝚘𝚞𝚛 𝙵𝚒𝚕𝚎 𝙸𝚜 𝚁𝚎𝚊𝚍𝚢, 𝙿𝚕𝚎𝚊𝚜𝚎 𝙶𝚎𝚝 𝚄𝚜𝚒𝚗𝚐 𝚃𝚑𝚒𝚜 𝙻𝚒𝚗𝚔.** 👍", reply_markup=InlineKeyboardMarkup(btn), protect_content=True)
            return            
        else:
            pass
    CAPTION = settings['caption']
    f_caption = CAPTION.format(
        file_name = files.file_name,
        file_size = get_size(files.file_size),
        file_caption=files.caption
    )
    btn = [[
        InlineKeyboardButton("ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 👀 / ꜰᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ 🗂️", callback_data="stream_button")
    ],[
        InlineKeyboardButton('⁉️ ᴄʟᴏsᴇ ⁉️', callback_data='close_data')
    ]]
    await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        protect_content=settings['file_secure'],
        reply_markup=InlineKeyboardMarkup(btn)
    )

@Client.on_message(filters.command('index_channels') & filters.user(ADMINS))
async def channels_info(bot, message):
    """Send basic information of index channels"""
    ids = INDEX_CHANNELS
    if not ids:
        return await message.reply("Not set INDEX_CHANNELS")

    text = '**Indexed Channels:**\n\n'
    for id in ids:
        chat = await bot.get_chat(id)
        text += f'{chat.title}\n'
    text += f'\n**Total:** {len(ids)}'
    await message.reply(text)

@Client.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot, message):
    msg = await message.reply('Please Wait...')
    files = await Media.count_documents()
    users = await db.total_users_count()
    chats = await db.total_chat_count()
    size = await db.get_db_size()
    free = 536870912 - size
    uptime = get_readable_time(time.time() - temp.START_TIME)
    size = get_size(size)
    free = get_size(free)
    await msg.edit(script.STATUS_TXT.format(files, users, chats, size, free, uptime))    
    
@Client.on_message(filters.command('settings'))
async def settings(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b>You are Anonymous admin you can't use this command !</b>")
    chat_type = message.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            if not await is_check_admin(client, grp_id, message.from_user.id):             
                return await message.reply_text('You not admin in this group.')
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("Make sure I'm present in your group!!", quote=True)
                return
        else:
            await message.reply_text("I'm not connected to any groups!", quote=True)
            return


    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:               
        grp_id = message.chat.id
        if not await is_check_admin(client, grp_id, message.from_user.id):
            return await message.reply_text('You not admin in this group.')
    settings = await get_settings(grp_id)
    if settings is not None:
        buttons = [[
            InlineKeyboardButton('Auto Filter', callback_data=f'setgs#auto_filter#{settings["auto_filter"]}#{grp_id}'),
            InlineKeyboardButton('✅ Yes' if settings["auto_filter"] else '❌ No', callback_data=f'setgs#auto_filter#{settings["auto_filter"]}#{grp_id}')
        ],[
            InlineKeyboardButton('File Secure', callback_data=f'setgs#file_secure#{settings["file_secure"]}#{grp_id}'),
            InlineKeyboardButton('✅ Yes' if settings["file_secure"] else '❌ No', callback_data=f'setgs#file_secure#{settings["file_secure"]}#{grp_id}')
        ],[
            InlineKeyboardButton('IMDb Poster', callback_data=f'setgs#imdb#{settings["imdb"]}#{grp_id}'),
            InlineKeyboardButton('✅ Yes' if settings["imdb"] else '❌ No', callback_data=f'setgs#imdb#{settings["imdb"]}#{grp_id}')
        ],[
            InlineKeyboardButton('Spelling Check', callback_data=f'setgs#spell_check#{settings["spell_check"]}#{grp_id}'),
            InlineKeyboardButton('✅ Yes' if settings["spell_check"] else '❌ No', callback_data=f'setgs#spell_check#{settings["spell_check"]}#{grp_id}')
        ],[
            InlineKeyboardButton('Auto Delete', callback_data=f'setgs#auto_delete#{settings["auto_delete"]}#{grp_id}'),
            InlineKeyboardButton(f'{get_readable_time(DELETE_TIME)}' if settings["auto_delete"] else '❌ No', callback_data=f'setgs#auto_delete#{settings["auto_delete"]}#{grp_id}')
        ],[
            InlineKeyboardButton('Welcome', callback_data=f'setgs#welcome#{settings["welcome"]}#{grp_id}',),
            InlineKeyboardButton('✅ Yes' if settings["welcome"] else '❌ No', callback_data=f'setgs#welcome#{settings["welcome"]}#{grp_id}'),
        ],[
            InlineKeyboardButton('Shortlink', callback_data=f'setgs#shortlink#{settings["shortlink"]}#{grp_id}'),
            InlineKeyboardButton('✅ Yes' if settings["shortlink"] else '❌ No', callback_data=f'setgs#shortlink#{settings["shortlink"]}#{grp_id}'),
        ],[
            InlineKeyboardButton('Result Page', callback_data=f'setgs#links#{settings["links"]}#{str(grp_id)}'),
            InlineKeyboardButton('⛓ Link' if settings["links"] else '🧲 Button', callback_data=f'setgs#links#{settings["links"]}#{str(grp_id)}')
        ],[
            InlineKeyboardButton('❌ Close ❌', callback_data='close_data')
        ]]
        await message.reply_text(
            text=f"Change your settings for <b>'{message.chat.title}'</b> as your wish. ⚙",
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=enums.ParseMode.HTML
        )
    else:
        await message.reply_text('Something went wrong!')

@Client.on_message(filters.command('set_template'))
async def save_template(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b>You are Anonymous admin you can't use this command !</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("Use this command in group.")      
    grp_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('You not admin in this group.')
    try:
        template = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text("Command Incomplete!")   
    await save_group_settings(grp_id, 'template', template)
    await message.reply_text(f"Successfully changed template for {title} to\n\n{template}")  
    
@Client.on_message(filters.command('set_caption'))
async def save_caption(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b>You are Anonymous admin you can't use this command !</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("Use this command in group.")      
    grp_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('You not admin in this group.')
    try:
        caption = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text("Command Incomplete!") 
    await save_group_settings(grp_id, 'caption', caption)
    await message.reply_text(f"Successfully changed caption for {title} to\n\n{caption}")
        
@Client.on_message(filters.command('set_shortlink'))
async def save_shortlink(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b>You are Anonymous admin you can't use this command !</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("Use this command in group.")    
    grp_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('You not admin in this group.')
    try:
        _, url, api = message.text.split(" ", 2)
    except:
        return await message.reply_text("<b>Command Incomplete:-\n\ngive me a shortlink & api along with the command...\n\nEx:- <code>/shortlink mdisklink.link 5843c3cc645f5077b2200a2c77e0344879880b3e</code>")   
    try:
        await get_shortlink(url, api, f'https://t.me/{temp.U_NAME}')
    except:
        return await message.reply_text("Your shortlink API or URL invalid, Please Check again!")   
    await save_group_settings(grp_id, 'url', url)
    await save_group_settings(grp_id, 'api', api)
    await message.reply_text(f"Successfully changed shortlink for {title} to\n\nURL - {url}\nAPI - {api}")
    
@Client.on_message(filters.command('get_custom_settings'))
async def get_custom_settings(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b>You are Anonymous admin you can't use this command !</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("Use this command in group.")
    grp_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('You not admin in this group...')    
    settings = await get_settings(grp_id)
    text = f"""Custom settings for: {title}

Shortlink URL: {settings["url"]}
Shortlink API: {settings["api"]}

IMDb Template: {settings['template']}

File Caption: {settings['caption']}

Welcome Text: {settings['welcome_text']}

Tutorial Link: {settings['tutorial']}

Force Channels: {str(settings['fsub'])[1:-1] if settings['fsub'] else 'Not Set'}"""

    btn = [[
        InlineKeyboardButton(text="Close", callback_data="close_data")
    ]]
    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True)

@Client.on_message(filters.command('set_welcome'))
async def save_welcome(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b>You are Anonymous admin you can't use this command !</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("Use this command in group.")      
    grp_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('You not admin in this group.')
    try:
        welcome = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text("Command Incomplete!")    
    await save_group_settings(grp_id, 'welcome_text', welcome)
    await message.reply_text(f"Successfully changed welcome for {title} to\n\n{welcome}")
        
@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete_file(bot, message):
    try:
        query = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text("Command Incomplete!\nUsage: /delete query")
    msg = await message.reply_text('Searching...')
    total, files = await delete_files(query)
    if int(total) == 0:
        return await msg.edit('Not have files in your query')
    btn = [[
        InlineKeyboardButton("YES", callback_data=f"delete_{query}")
    ],[
        InlineKeyboardButton("CLOSE", callback_data="close_data")
    ]]
    await msg.edit(f"Total {total} files found in your query {query}.\n\nDo you want to delete?", reply_markup=InlineKeyboardMarkup(btn))
 
@Client.on_message(filters.command('delete_all') & filters.user(ADMINS))
async def delete_all_index(bot, message):
    btn = [[
        InlineKeyboardButton(text="YES", callback_data="delete_all")
    ],[
        InlineKeyboardButton(text="CLOSE", callback_data="close_data")
    ]]
    files = await Media.count_documents()
    if int(files) == 0:
        return await message.reply_text('Not have files to delete')
    await message.reply_text(f'Total {files} files have.\nDo you want to delete all?', reply_markup=InlineKeyboardMarkup(btn))

@Client.on_message(filters.command('set_tutorial'))
async def set_tutorial(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b>You are Anonymous admin you can't use this command !</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("Use this command in group.")       
    grp_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('You not admin in this group.')
    try:
        tutorial = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text("Command Incomplete!")   
    await save_group_settings(grp_id, 'tutorial', tutorial)
    await message.reply_text(f"Successfully changed tutorial for {title} to\n\n{tutorial}")

@Client.on_message(filters.command('set_fsub'))
async def set_fsub(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b>You are Anonymous admin you can't use this command !</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("Use this command in group.")      
    grp_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('You not admin in this group.')
    try:
        ids = message.text.split(" ", 1)[1]
        fsub_ids = list(map(int, ids.split()))
    except IndexError:
        return await message.reply_text("Command Incomplete!\n\nCan multiple channel add separate by spaces. Like: /set_fsub id1 id2 id3")
    except ValueError:
        return await message.reply_text('Make sure ids is integer.')        
    channels = "Channels:\n"
    for id in fsub_ids:
        try:
            chat = await client.get_chat(id)
        except Exception as e:
            return await message.reply_text(f"{id} is invalid!\nMake sure this bot admin in that channel.\n\nError - {e}")
        if chat.type != enums.ChatType.CHANNEL:
            return await message.reply_text(f"{id} is not channel.")
        channels += f'{chat.title}\n'
        if not await db.has_premium_access(message.from_user.id):
            await message.reply_text("<b>You don't have access to use this command!buy premium ship check /plans</b>")
            return
        else:
            pass
    await save_group_settings(grp_id, 'fsub', fsub_ids)
    await message.reply_text(f"Successfully set force channels for {title} to\n\n{channels}")

@Client.on_message(filters.command('telegraph'))
async def telegraph(bot, message):
    reply_to_message = message.reply_to_message
    if not reply_to_message:
        return await message.reply('Reply to any photo or video.')
    file = reply_to_message.photo or reply_to_message.video or None
    if file is None:
        return await message.reply('Invalid media.')
    if file.file_size >= 5242880:
        await message.reply_text(text="Send less than 5MB")   
        return
    text = await message.reply_text(text="ᴘʀᴏᴄᴇssɪɴɢ....")   
    media = await reply_to_message.download()  
    try:
        response = upload_file(media)
    except Exception as e:
        await text.edit_text(text=f"Error - {e}")
        return    
    try:
        os.remove(media)
    except:
        pass
    await text.edit_text(f"<b>❤️ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴄᴏᴍᴘʟᴇᴛᴇᴅ 👇</b>\n\n<code>https://telegra.ph/{response[0]}</code></b>")

@Client.on_message(filters.command('ping'))
async def ping(client, message):
    start_time = time.monotonic()
    msg = await message.reply("👀")
    end_time = time.monotonic()
    await msg.edit(f'{round((end_time - start_time) * 1000)} ms')

@Client.on_message(filters.command("add_premium") & filters.user(ADMINS))
async def give_premium_cmd_handler(client, message):
    if len(message.command) == 3:
        try:
            user_id = int(message.command[1])  # Convert the user_id to an integer
            time_str = message.command[2]
            seconds = await get_seconds(time_str)
            if seconds > 0:
                expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
                user_data = {"id": user_id, "expiry_time": expiry_time}  # Using "id" instead of "user_id"
                await db.update_user(user_data)  # Use the update_user method to update or insert user data
                
                # Create an inline keyboard with a button
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [ 
                         InlineKeyboardButton(text="• ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ɢʀᴏᴜᴘ •", url="https://t.me/+o_VcAI8GRQ8zYzA9")
                    ],[
                         InlineKeyboardButton(text="• Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ •", url="https://t.me/filmyspot_support")
                    ]
                        ])
                # Send the message with the inline keyboard
                await client.send_message(
                    chat_id=user_id,
                    text=f"<b>𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐚𝐝𝐝𝐞𝐝 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐚𝐜𝐜𝐨𝐮𝐧𝐭 𝐟𝐨𝐫 {time_str} 🌟. 𝐄𝐧𝐣𝐨𝐲 𝐲𝐨𝐮𝐫 𝐞𝐱𝐜𝐥𝐮𝐬𝐢𝐯𝐞 𝐚𝐜𝐜𝐞𝐬𝐬 𝐭𝐨 𝐨𝐮𝐫 𝐦𝐨𝐯𝐢𝐞 𝐜𝐨𝐥𝐥𝐞𝐜𝐭𝐢𝐨𝐧!\n</b>",
                    reply_markup=keyboard
                )
                
                await message.reply_text("Premium access added to the user.")
            else:
                await message.reply_text("Invalid time format. Please use '1day for days', '1hour for hours', '1min for minutes', '1month for months', or '1year for year'")
        except ValueError:
            await message.reply_text("Invalid user ID. Please provide a valid user ID.")
        except Exception as e:
            await message.reply_text(f"An error occurred: {str(e)}")
    else:
        await message.reply_text("Usage: /add_premium user_id time (e.g., '1day for days', '1hour for hours', '1min for minutes', '1month for months', or '1year for year')")
            
        
@Client.on_message(filters.command("remove_premium") & filters.user(ADMINS))
async def remove_premium_cmd_handler(client, message):
    if len(message.command) == 2:
        user_id = int(message.command[1])  # Convert the user_id to integer
      #  time = message.command[2]
        time = "1s"
        seconds = await get_seconds(time)
        if seconds > 0:
            expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
            user_data = {"id": user_id, "expiry_time": expiry_time}  # Using "id" instead of "user_id"
            await db.update_user(user_data)  # Use the update_user method to update or insert user data
            await message.reply_text("Premium access removed to the user.")
            await client.send_message(
                chat_id=user_id,
                text=f"<b>premium removed by admins \n\n Contact Admin if this is mistake \n\n 👮 Admin : @Rk_botowner \n</b>",                
            )
        else:
            await message.reply_text("Invalid time format.'")
    else:
        await message.reply_text("Usage: /remove_premium user_id")
        
@Client.on_message(filters.command("plans"))
async def plans_cmd_handler(client, message):                
    btn = [   
        [InlineKeyboardButton("🆙 ᴄʟɪᴄᴋ ᴛᴏ ʙᴜʏ 🆙", url="https://cosmofeed.com/vig/65ae01464009dd001dc656d8")],         
        [InlineKeyboardButton("⚠️ᴄʟᴏsᴇ / ᴅᴇʟᴇᴛᴇ⚠️", callback_data="close_data")]
    ]
    reply_markup = InlineKeyboardMarkup(btn)
    await message.reply_photo(
        photo="https://graph.org/file/775165057a97fb4393a80.jpg",
        caption="※──[ 🔥 ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs 🔥 ]──※\n│⇛ ₹15 -  1 Wᴇᴇᴋ\n│⇛ ₹39 -  1 Mᴏɴᴛʜ\n│⇛ ₹69 -  2 Mᴏɴᴛʜs\n│⇛ ₹99 -  3 Mᴏɴᴛʜs\n│⇛ ₹179 - 6 Mᴏɴᴛʜs\n│⇛ ₹299 - 1 Yᴇᴀʀ\n│⇛ Custom Plan - Contact Owner\n※───────────────────※\n\n╭──🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁──╮\n│ • ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ\n│ • ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n│ • ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n│ • ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ\n│ • ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs\n│ • ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs\n│ • ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴀᴠᴀɪʟᴀʙʟᴇ\n│ • ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ\n│ • ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1 ʜᴏᴜʀ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ\n╰──────────────────╯\n\n𝐁𝐔𝐘 𝐍𝐎𝐖 ➢ [🅲🅻🅸🅲🅺 🅷🅴🆁🅴](https://cosmofeed.com/vig/65ae01464009dd001dc656d8)\n\n➥ Iғ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ꜱᴜʀᴇ ʜᴏᴡ ᴛᴏ ʙᴜʏ, ɪᴜꜱᴛ ᴡᴀᴛᴄʜ ᴛʜᴇ ᴛᴜᴛᴏʀɪᴀʟ. /plantutorial\n\n➥ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan\n\n➥ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ\n\n⚠️ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐚𝐥𝐥𝐨𝐰 𝐬𝐨𝐦𝐞 𝐭𝐢𝐦𝐞 𝐚𝐟𝐭𝐞𝐫 𝐬𝐞𝐧𝐝𝐢𝐧𝐠 𝐭𝐡𝐞 𝐬𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭 𝐟𝐨𝐫 𝐭𝐡𝐞 𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝐚𝐜𝐜𝐞𝐬𝐬 𝐭𝐨 𝐭𝐚𝐤𝐞 𝐞𝐟𝐟𝐞𝐜𝐭.",
        reply_markup=reply_markup
    )
        
@Client.on_message(filters.command("my_plan"))
async def check_plans_cmd(client, message):
    user_id  = message.from_user.id
    if await db.has_premium_access(user_id):         
        remaining_time = await db.check_remaining_uasge(user_id)             
        expiry_time = remaining_time + datetime.datetime.now()
        await message.reply_text(f"**Your plans details are :\n\nRemaining Time : {remaining_time}\n\nExpirytime : {expiry_time}**")
    else:
        btn = [                                
            [InlineKeyboardButton("ʙᴜʏ sᴜʙsᴄʀɪᴘᴛɪᴏɴ : ʀᴇᴍᴏᴠᴇ ᴀᴅs", callback_data="buy_premium")],
            [InlineKeyboardButton("⚠️ ᴄʟᴏsᴇ / ᴅᴇʟᴇᴛᴇ ⚠️", callback_data="close_data")]
        ]
        reply_markup = InlineKeyboardMarkup(btn)
        m=await message.reply_sticker("CAACAgIAAxkBAAIBTGVjQbHuhOiboQsDm35brLGyLQ28AAJ-GgACglXYSXgCrotQHjibHgQ")         
        await message.reply_text(f"**😢 You Don't Have Any Premium Subscription.\n\n Check Out Our Premium /plans**",reply_markup=reply_markup)
        await asyncio.sleep(2)
        await m.delete()

@Client.on_callback_query(filters.regex("show_plans"))
async def show_plans_callback_handler(client, callback_query):
    # Send the plans message using the logic from the plans command
    btn = [   
        [InlineKeyboardButton("• ɢᴇᴛ 𝟻 ᴍɪɴ ғʀᴇᴇ ᴛʀɪᴀʟ •", callback_data="get_trail")],
        [InlineKeyboardButton("🆙 ᴄʟɪᴄᴋ ᴛᴏ ʙᴜʏ 🆙", url="https://cosmofeed.com/vig/65ae01464009dd001dc656d8")],         
        [InlineKeyboardButton("⚠️ᴄʟᴏsᴇ / ᴅᴇʟᴇᴛᴇ⚠️", callback_data="close_data")]
    ]
    reply_markup = InlineKeyboardMarkup(btn)
    await callback_query.message.reply_photo(
        photo="https://graph.org/file/775165057a97fb4393a80.jpg",
        caption="※──[ 🔥 ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs 🔥 ]──※\n│⇛ ₹15 -  1 Wᴇᴇᴋ\n│⇛ ₹39 -  1 Mᴏɴᴛʜ\n│⇛ ₹69 -  2 Mᴏɴᴛʜs\n│⇛ ₹99 -  3 Mᴏɴᴛʜs\n│⇛ ₹179 - 6 Mᴏɴᴛʜs\n│⇛ ₹299 - 1 Yᴇᴀʀ\n│⇛ Custom Plan - Contact Owner\n※───────────────────※\n\n╭──🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁──╮\n│ • ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ\n│ • ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n│ • ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n│ • ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ\n│ • ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs\n│ • ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs\n│ • ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴀᴠᴀɪʟᴀʙʟᴇ\n│ • ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ\n│ • ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1 ʜᴏᴜʀ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ\n╰──────────────────╯\n\n𝐁𝐔𝐘 𝐍𝐎𝐖 ➢ [🅲🅻🅸🅲🅺 🅷🅴🆁🅴](https://cosmofeed.com/vig/65ae01464009dd001dc656d8)\n\n➥ Iғ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ꜱᴜʀᴇ ʜᴏᴡ ᴛᴏ ʙᴜʏ, ɪᴜꜱᴛ ᴡᴀᴛᴄʜ ᴛʜᴇ ᴛᴜᴛᴏʀɪᴀʟ. /plantutorial\n\n➥ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /my_plan\n\n➥ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ\n\n⚠️ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐚𝐥𝐥𝐨𝐰 𝐬𝐨𝐦𝐞 𝐭𝐢𝐦𝐞 𝐚𝐟𝐭𝐞𝐫 𝐬𝐞𝐧𝐝𝐢𝐧𝐠 𝐭𝐡𝐞 𝐬𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭 𝐟𝐨𝐫 𝐭𝐡𝐞 𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝐚𝐜𝐜𝐞𝐬𝐬 𝐭𝐨 𝐭𝐚𝐤𝐞 𝐞𝐟𝐟𝐞𝐜𝐭.",
        reply_markup=reply_markup
    )

@Client.on_message(filters.command("shortener_list"))
async def shortener_list_handler(client, message):
    # Define the inline keyboard buttons
    buttons = [
        [
            InlineKeyboardButton("📞 ᴄᴏɴᴛᴀᴄᴛ ", url="t.me/FilmySpotSupport_bot"),
            InlineKeyboardButton("ᴅᴇʟᴇᴛᴇ", callback_data="close_data")
        ]
    ]
    # Create an InlineKeyboardMarkup object with the buttons
    reply_markup = InlineKeyboardMarkup(buttons)
    # Send the photo with the caption and inline keyboard markup
    await message.reply_text(
        text="╭━━━❰ 𝗶𝗻𝘀𝘁𝗮𝗻𝘁𝗲𝗮𝗿𝗻 ❱━━━☆\n┣⪼📄 𝗣𝗮𝗴𝗲𝘀: 𝟰\n┣⪼💵 𝗙𝗶𝘅𝗲𝗱 𝗖𝗣𝗠: $𝟭𝟬 / ₹𝟴𝟬𝟬\n┣⪼💳 𝗪𝗶𝘁𝗵𝗱𝗿𝗮𝘄𝗮𝗹: $𝟮 / ₹𝟭𝟲𝟬\n┣⪼🌐 𝗥𝗲𝗳𝗲𝗿𝗿𝗮𝗹 𝗟𝗶𝗻𝗸: [𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗮𝗿](https://bit.ly/instantearn0)\n┣⪼📎 𝗗𝗲𝗺𝗼 𝗟𝗶𝗻𝗸: [𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗮𝗿](http://instantearn.in/instantearn)\n╰━━━━━━━━━━━━━☆\n\n╭━━━❰ 𝗼𝗻𝗲𝗽𝗮𝗴𝗲𝗹𝗶𝗻𝗸 ❱━━━☆\n┣⪼📄 𝗣𝗮𝗴𝗲𝘀: 𝟭\n┣⪼💵 𝗔𝘃𝗲𝗿𝗮𝗴𝗲 𝗖𝗣𝗠: ₹𝟮𝟱𝟬\n┣⪼💳 𝗪𝗶𝘁𝗵𝗱𝗿𝗮𝘄𝗮𝗹: $𝟮.𝟰𝟭 / ₹𝟮𝟬𝟬\n┣⪼🌐 𝗥𝗲𝗳𝗲𝗿𝗿𝗮𝗹 𝗟𝗶𝗻𝗸: [𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗮𝗿](https://bit.ly/onepagelink)\n┣⪼📎 𝗗𝗲𝗺𝗼: [𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗮𝗿](http://onepagelink.in/onepagelink)\n╰━━━━━━━━━━━━━☆\n\n╭━━❰ 𝗺𝗼𝗻𝗲𝘆𝗸𝗮𝗺𝗮𝗹𝗼 ❱━━━☆\n┣⪼📄 𝗣𝗮𝗴𝗲𝘀: 𝟮\n┣⪼💵 𝗔𝘃𝗲𝗿𝗮𝗴𝗲 𝗖𝗣𝗠: ₹𝟰𝟬𝟬\n┣⪼💳 𝗪𝗶𝘁𝗵𝗱𝗿𝗮𝘄𝗮𝗹: $𝟯.𝟲𝟭 / ₹𝟯𝟬𝟬\n┣⪼🌐 𝗥𝗲𝗳𝗲𝗿𝗿𝗮𝗹 𝗟𝗶𝗻𝗸: [𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗮𝗿](https://bit.ly/moneykamalo)\n┣⪼📎 𝗗𝗲𝗺𝗼: [𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗮𝗿](http://earn.moneykamalo.com/FASmBFJ8)\n╰━━━━━━━━━━━━━☆\n\n╭━━━━❰ 𝘇𝗶𝗽𝘀𝗵𝗼𝗿𝘁 ❱━━━━☆\n┣⪼📄 𝗣𝗮𝗴𝗲𝘀: 𝟮\n┣⪼💵 𝗔𝘃𝗲𝗿𝗮𝗴𝗲 𝗖𝗣𝗠: ₹𝟰𝟮𝟬 \n┣⪼💳 𝗪𝗶𝘁𝗵𝗱𝗿𝗮𝘄𝗮𝗹: ₹𝟭𝟱𝟬\n┣⪼🌐 𝗥𝗲𝗳𝗲𝗿𝗿𝗮𝗹 𝗟𝗶𝗻𝗸: [𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗮𝗿](https://bit.ly/zipshort)\n┣⪼📎 𝗗𝗲𝗺𝗼: [𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗮𝗿](https://zipshort.net/IRfy)\n╰━━━━━━━━━━━━━☆",
        reply_markup=reply_markup
    )

@Client.on_message(filters.command("plantutorial"))
async def forward_video(client, message: Message):
    try:
        # Replace this with the actual link of the video you want to forward
        video_link = "https://t.me/filmyspotupdate/76"  # Replace with the actual video link
        btn = InlineKeyboardMarkup(
            [[
                    InlineKeyboardButton("💳 ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ : ʀᴇᴍᴏᴠᴇ ᴀᴅs 💳", url="https://cosmofeed.com/vig/65ae01464009dd001dc656d8")
                ],[
                    InlineKeyboardButton("ᴅᴇʟᴇᴛᴇ", callback_data="close_data")
                ]]
        )
        await client.send_video(
            chat_id=message.chat.id,
            video=video_link,
            caption="Here's the tutorial video you requested.",
            reply_markup=btn
        )
    except Exception as e:
        print(f"An error occurred: {e}")

