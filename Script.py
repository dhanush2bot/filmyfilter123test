class script(object):
    
    START_TXT = """<b>ʜᴇʟʟᴏ  {}, <i>{}</i>
    
I ᴀᴍ ᴀ ᴅʏɴᴀᴍɪᴄ ʙᴏᴛ ᴛʜᴀᴛ ᴇɴʀɪᴄʜᴇs ʏᴏᴜʀ ᴡᴏʀʟᴅ ᴡɪᴛʜ ᴍᴏᴠɪᴇs. Usᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴅɪsᴄᴏᴠᴇʀ ᴀɴᴅ sʜᴀʀᴇ ᴄɪɴᴇᴍᴀᴛɪᴄ ᴡᴏɴᴅᴇʀs. Sɪᴍᴘʟʏ ᴀᴅᴅ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ, ᴀɴᴅ ʟᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ᴍᴀɢɪᴄ ʙᴇɢɪɴ! 🎥✨</b>"""

    MY_ABOUT_TXT = """<b>⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟
 ✯ ᴍʏ ɴᴀᴍᴇ : ғɪʟᴍʏ ғɪʟᴛᴇʀ ᴘʀᴇᴍɪᴜᴍ ʙᴏᴛ
 ✯ ᴅᴇᴠᴇʟᴏᴘᴇʀ : ᴍᴏɴsᴛᴇʀ x
 ✯ ʙᴏᴛ sᴇʀᴠᴇʀ : ᴘʀɪᴠᴀᴛᴇ
 ✯ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]</b>"""

    SUPPORT_TXT = """<b>⍟ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs Mᴏᴅᴜʟᴇ ⍟
🎬 Cᴏᴍᴘʟᴇᴛᴇ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛɪɴɢ Gʀᴏᴜᴘ.
🚦 Aʟʟ Lᴀɴɢᴜᴀɢᴇs Mᴏᴠɪᴇs & Sᴇʀɪᴇs.
🗣️ Bᴏᴛ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ.
📢 Bᴏᴛ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ.</b>"""

    MY_OWNER_TXT = """<b>⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟
 ✯ ᴍʏ ɴᴀᴍᴇ : ғɪʟᴍʏ ғɪʟᴛᴇʀ ᴘʀᴇᴍɪᴜᴍ ʙᴏᴛ
 ✯ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/FilmySpotSupport_bot'>ᴍᴏɴsᴛᴇʀ x</a>🕷
 ✯ ʙᴏᴛ sᴇʀᴠᴇʀ : ᴘʀɪᴠᴀᴛᴇ
 ✯ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]</b>"""

    STATUS_TXT = """🗂 Total Files: <code>{}</code>
👤 Total Users: <code>{}</code>
👥 Total Chats: <code>{}</code>
✨ Storage: <code>{}</code> / <code>{}</code>
🚀 Uptime: <code>{}</code>"""

    NEW_GROUP_TXT = """#NewGroup
Title - {}
ID - <code>{}</code>
Username - {}
Total - <code>{}</code>"""

    NEW_USER_TXT = """#NewUser
★ Name: {}
★ ID: <code>{}</code>"""

    NO_RESULT_TXT = """#NoResult
★ Group Name: {}
★ Group ID: <code>{}</code>
★ Name: {}

★ Message: {}"""

    REQUEST_TXT = """★ Name: {}
★ ID: <code>{}</code>

★ Message: {}"""

    NOT_FILE_TXT = """👋 Hello {},

➥ Aᴘᴏʟᴏɢɪᴇꜱ, I ᴄᴏᴜʟᴅɴ'ᴛ ғɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇꜱ ᴏʀ ꜱᴇʀɪᴇꜱ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴇ ᴡᴏʀᴅ <b>{}</b> 🥲

➥ Pʟᴇᴀꜱᴇ ᴅᴏᴜʙʟᴇ-ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴘᴇʟʟɪɴɢ ᴜꜱɪɴɢ Gᴏᴏɢʟᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ 😃
➥ Fᴏʀ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛꜱ, ᴜꜱᴇ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ғᴏʀᴍᴀᴛ 👇
➥ Exᴀᴍᴘʟᴇ: 𝐁𝐡𝐞𝐝𝐢𝐲𝐚 𝐨𝐫 𝐁𝐡𝐞𝐝𝐢𝐲𝐚 𝟐𝟎𝟐𝟐 𝐨𝐫 𝐀𝐯𝐚𝐭𝐚𝐫 𝟐𝟎𝟎𝟗 𝐇𝐢𝐧𝐝𝐢
➥ Fᴏʀ ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛꜱ, ᴜꜱᴇ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ғᴏʀᴍᴀᴛ 👇
➥ Exᴀᴍᴘʟᴇ: 𝐀𝐬𝐮𝐫 𝐒𝟎𝟐 𝐨𝐫 𝐀𝐬𝐮𝐫 𝐒𝟎𝟏𝐄𝟎𝟒 𝐨𝐫 𝐀𝐬𝐮𝐫 𝐒𝟎𝟑𝐄𝟐𝟒
➥ 🚯 Aᴠᴏɪᴅ ᴜꜱɪɴɢ ➠ ':(!,./)
"""
    
    EARN_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ꜰʀᴏᴍ ᴛʜɪs ʙᴏᴛ

➥ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴜsɪɴɢ ᴛʜɪꜱ ʙᴏᴛ.

» sᴛᴇᴘ 1:- ғɪʀsᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ.

» sᴛᴇᴘ 2:- ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ <a href=https://t.me/filmyspotupdate/72>ᴜʀʟʟɪɴᴋsʜᴏʀᴛ.ɪɴ</a> [ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴏᴛʜᴇʀ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ]

» sᴛᴇᴘ 3:- ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.

➥ ᴛʜɪꜱ ʙᴏᴛ ɪs ꜰʀᴇᴇ ꜰᴏʀ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғᴏʀ ꜰʀᴇᴇ ᴏꜰ ᴄᴏꜱᴛ.

⚠ ɴᴏᴛᴇ ⚠

➥ Iғ ʏᴏᴜ'ʀᴇ sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ᴛʜᴇ ʙᴇsᴛ ᴀɴᴅ ʜɪɢʜᴇsᴛ-ᴘᴀʏɪɴɢ URL sʜᴏʀᴛᴇɴᴇʀ, ɪᴜsᴛ ᴛᴀᴘ ᴏɴ /shortener_list ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ᴛᴏᴘ URL sʜᴏʀᴛᴇɴᴇʀ ᴏᴘᴛɪᴏɴs.</b>"""

    HOW_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ‼️

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ᴛʜᴇɴ ᴊᴜsᴛ sᴇɴᴅ ᴛʜᴇ ɢɪᴠᴇɴ ᴅᴇᴛᴀɪʟs ɪɴ ᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

➥ ғᴏʀᴍᴀᴛ ↓↓↓

<code>/set_shortlink sʜᴏʀᴛɴᴇʀ sɪᴛᴇ sʜᴏʀᴛɴᴇʀ ᴀᴘɪ</code>

➥ ᴇxᴀᴍᴘʟᴇ ↓↓↓

<code>/set_shortlink urllinkshort.in f5df853fb17ef7b3de7b0ddd4359405106fe5116</code>

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴇᴄᴋ ᴡʜɪᴄʜ sʜᴏʀᴛᴇɴᴇʀ ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ /get_shortlink

📝 ɴᴏᴛᴇ:- ʏᴏᴜ sʜᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘ. sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜᴏᴜᴛ ʙᴇɪɴɢ ᴀɴ ᴀɴᴏɴʏᴍᴜs ᴀᴅᴍɪɴ.</b>"""

    IMDB_TEMPLATE = """✅ I Found: <code>{query}</code>

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating} / 10</a>
☀️ Languages: {languages}
📀 RunTime: {runtime} Minutes

🗣 Requested by: {message.from_user.mention}
©️ Powered by: <b>{message.chat.title}</b>"""

    FILE_CAPTION = """<b>ɴᴀᴍᴇ:</b> <code>{file_name}</code>

➥ Jᴏɪɴ ᴜs : <a href=https://t.me/+6WzgVuPbFxs4NWQ1>ғɪʟᴍʏ sᴘᴏᴛ ᴍᴏᴠɪᴇs
➥ Jᴏɪɴ ᴜs : <a href=https://t.me/filmyspotupdate>ғɪʟᴍʏ sᴘᴏᴛ ᴜᴘᴅᴀᴛᴇs</a></a>
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"""

    WELCOME_TEXT = """👋 Hᴇʟʟᴏ {mention}, Wᴇʟᴄᴏᴍᴇ ᴛᴏ {title} ɢʀᴏᴜᴘ! 💞

    Fᴇᴇʟ ғʀᴇᴇ ᴛᴏ ʀᴇǫᴜᴇsᴛ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ ᴍᴏᴠɪᴇs ʜᴇʀᴇ ᴀɴᴅ ᴇɴɢᴀɢᴇ ɪɴ ᴅɪsᴄᴜssɪᴏɴs ᴀʙᴏᴜᴛ ғɪʟᴍs ᴀɴᴅ sᴇʀɪᴇs. Eɴɪᴏʏ ʏᴏᴜʀ sᴛᴀʏ!"""

    HELP_TXT = """<b>📚 Exᴘʟᴏʀᴇ ᴛʜᴇ Usᴇʀs sᴇᴄᴛɪᴏɴ ɪɴ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴅɪsᴄᴏᴠᴇʀ ᴀ ᴠᴀʀɪᴇᴛʏ ᴏғ ᴄᴏᴍᴍᴀɴᴅs. Sɪᴍᴘʟʏ ᴜsᴇ ᴇᴀᴄʜ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴀʀɢᴜᴍᴇɴᴛs ᴛᴏ sᴇᴇ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs ᴀɴᴅ ʜᴏᴡ ᴛʜᴇʏ ᴄᴀɴ ᴇɴʜᴀɴᴄᴇ ʏᴏᴜʀ ᴇxᴘᴇʀɪᴇɴᴄᴇ. Hᴀᴘᴘʏ ᴇxᴘʟᴏʀɪɴɢ!</b>"""
    
    ADMIN_COMMAND_TXT = """<b>ʜᴇʀᴇ ɪs ʙᴏᴛ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs 👇

➥ /index_channels - ᴛᴏ ᴄʜᴇᴄᴋ ʜᴏᴡ ᴍᴀɴʏ ɪɴᴅᴇx ᴄʜᴀɴɴᴇʟ ɪᴅ ᴀᴅᴅᴇᴅ
➥ /stats - ᴛᴏ ɢᴇᴛ ʙᴏᴛ sᴛᴀᴛᴜs
➥ /delete - ᴛᴏ ᴅᴇʟᴇᴛᴇ ғɪʟᴇs ᴜsɪɴɢ ϙᴜᴇʀʏ
➥ /delete_all - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɪɴᴅᴇxᴇᴅ ғɪʟᴇ
➥ /broadcast - ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ʙᴏᴛ ᴜsᴇʀs
➥ /grp_broadcast - ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ɢʀᴏᴜᴘs
➥ /restart - ᴛᴏ ʀᴇsᴛᴀʀᴛ ʙᴏᴛ
➥ /leave - ᴛᴏ ʟᴇᴀᴠᴇ ʏᴏᴜʀ ʙᴏᴛ ғʀᴏᴍ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʀᴏᴜᴘ
➥ /unban_grp - ᴛᴏ ᴇɴᴀʙʟᴇ ɢʀᴏᴜᴘ
➥ /ban_grp - ᴛᴏ ᴅɪsᴀʙʟᴇ ɢʀᴏᴜᴘ
➥ /ban_user - ᴛᴏ ʙᴀɴ ᴀ ᴜsᴇʀs ғʀᴏᴍ ʙᴏᴛ
➥ /unban_user - ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜsᴇʀs ғʀᴏᴍ ʙᴏᴛ
➥ /users - ᴛᴏ ɢᴇᴛ ᴀʟʟ ᴜsᴇʀs ᴅᴇᴛᴀɪʟs
➥ /chats - ᴛᴏ ɢᴇᴛ ᴀʟʟ ɢʀᴏᴜᴘs
➥ /invite_link - ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ɪɴᴠɪᴛᴇ ʟɪɴᴋ
➥ /index - ᴛᴏ ɪɴᴅᴇx ʙᴏᴛ ᴀᴄᴄᴇssɪʙʟᴇ ᴄʜᴀɴɴᴇʟs</b>"""
    
    USER_COMMAND_TXT = """<b>ʜᴇʀᴇ ɪs ʙᴏᴛ ᴜsᴇʀ ᴄᴏᴍᴍᴀɴᴅs 👇

➥ /start - ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ
➥ /settings - ᴛᴏ ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ
➥ /set_template - ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ
➥ /set_caption - ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ʙᴏᴛ ғɪʟᴇs ᴄᴀᴘᴛɪᴏɴ
➥ /set_shortlink - ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴄᴀɴ sᴇᴛ ᴄᴜsᴛᴏᴍ sʜᴏʀᴛʟɪɴᴋ
➥ /get_custom_settings - ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ sᴇᴛᴛɪɴɢs ᴅᴇᴛᴀɪʟs
➥ /set_welcome - ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ɴᴇᴡ ᴊᴏɪɴᴇᴅ ᴜsᴇʀs ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ ғᴏʀ ɢʀᴏᴜᴘ
➥ /set_tutorial - ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴛᴜᴛᴏʀɪᴀʟ ʟɪɴᴋ ɪɴ ʀᴇsᴜʟᴛ ᴘᴀɢᴇ ʙᴜᴛᴛᴏɴ
➥ /id - ᴛᴏ ᴄʜᴇᴄᴋ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ ɪᴅ
➥ /fsub - ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ғsᴜʙ
➥ /openai - ғɪɴᴅ sᴏʟᴜᴛɪᴏɴ ᴛᴏ ᴀɴʏ ϙᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ᴄʜᴀᴛɢᴘᴛ
➥ /plans - ᴛᴏ ᴠɪᴇᴡ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs
➥ /my_plan - ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ</b>"""

    SOURCE_TXT = """<b>Bᴏᴛ GɪᴛHᴜʙ Rᴇᴘᴏsɪᴛᴏʀʏ

➥ᴛʜɪs ʙᴏᴛ ɪs ᴀ ᴘʀɪᴠᴀᴛᴇ ᴘʀᴏɪᴇᴄᴛ.

➥sᴏᴜʀᴄᴇ: ᴄᴏɴᴛᴀᴄᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ

ᴛʜɪs ʙᴏᴛ ᴀʟsᴏ ᴜsᴇs 𝟾𝟶% ᴏᴘᴇɴ-sᴏᴜʀᴄᴇ ᴘʀᴏɪᴇᴄᴛs ᴀɴᴅ ᴛʜᴇ ʀᴇᴍᴀɪɴɪɴɢ ᴀʀᴇ ᴘʀɪᴠᴀᴛᴇ. ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴛʜᴇ sᴀᴍᴇ ʙᴏᴛ ᴛʜᴀɴ ᴄᴏɴᴛᴇᴛ ᴏᴡɴᴇʀ, ᴄʟɪᴋᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟʟᴏᴡ ᴛᴏ ᴄᴏɴᴛᴇᴄᴛ ᴍᴇ.</a>

➥ ᴅᴇᴠʟᴏᴘᴇʀ -
<a href=https://t.me/FilmySpotSupport_bot>ᴍᴏɴsᴛᴇʀ x</a></b>🕷"""

    BUY_PREMIUM = """
<b>Pʀᴇᴍɪᴜᴍ Fᴇᴀᴛᴜʀᴇs 🎁                      
○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ
○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs                                                                         
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ   

➥ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /my_plan

‼️ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄʜᴇᴄᴋ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs & ɪᴛ's ᴘʀɪᴄᴇs</b>"""

    CONNECTION_TXT = """ʜᴇʟᴘ: <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>
- ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
- ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.
<b>ɴᴏᴛᴇ:</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ <code>/ᴄᴏɴɴᴇᴄᴛ</code> ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /connect  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ</code>
• /disconnect  - <code>ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
• /connections - <code>ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</code>"""

    TELEGRAPH_TXT = """▫️Hᴇʟᴘ: ▪️ Tᴇʟᴇɢʀᴀᴘʜ ▪️
Tᴇʟᴇɢʀᴀᴘʜ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴏʀ
Usᴀɢᴇ
/telegraph - Sᴇɴᴅ Mᴇ Pʜᴏᴛᴏ Oʀ Vɪᴅᴇᴏ Uɴᴅᴇʀ(5ᴍʙ) Aɴᴅ Rᴇᴘʟʏ Wɪᴛʜ Cᴏᴍᴍᴀᴍɴᴅ"""

    MODS_TXT = """Yᴏᴜ Cᴀɴ Tʀʏ Aʟʟ Tʜᴇsᴇ Cᴏᴏʟ Fᴇᴀᴛᴜʀᴇs Fʀᴏᴍ Bᴇʟᴏᴡ Oᴘᴛɪᴏɴ..!!!"""

    OWNER_INFO = """
<b>⍟───[Oᴡɴᴇʀ Dᴇᴛᴀɪʟꜱ]───⍟ 
 ◈ ᴛɢ ɴᴀᴍᴇ : ᴍᴏɴsᴛᴇʀ x
 ◈ ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ : <spoiler> {mention} </spoiler>

<b>➥ Oɴ ᴛʜᴇ ʜᴜɴᴛ ғᴏʀ ᴛʜᴇ ᴏᴡɴᴇʀ's ɪɴғᴏ, ʜᴜʜ? Yᴏᴜ'ᴠᴇ ɢᴏᴛ ʏᴏᴜʀ sᴛᴀʀᴛᴇʀ ᴘᴀᴄᴋ ʀɪɢʜᴛ ʜᴇʀᴇ! Nᴇᴇᴅ ᴛʜᴇ ғᴜʟʟ sᴄᴏᴏᴘ? Cᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴏᴡɴᴇʀ ᴅɪʀᴇᴄᴛʟʏ. Aɴᴅ ʜᴇʏ, ᴋᴇᴇᴘ ᴛʜᴏsᴇ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇsᴛs ᴄᴏᴍɪɴɢ! 😂😅</b>"""

    DISL_TXT = """
<b>Tʜɪs ʙᴏᴛ ᴀʟsᴏ ᴜᴛɪʟɪᴢᴇs 𝟾𝟶% ᴏᴘᴇɴ-sᴏᴜʀᴄᴇ ᴘʀᴏɪᴇᴄᴛs, ᴡɪᴛʜ ᴛʜᴇ ʀᴇᴍᴀɪɴɪɴɢ ʙᴇɪɴɢ ᴘʀɪᴠᴀᴛᴇ.

Aʟʟ ᴛʜᴇ ғɪʟᴇs ɪɴ ᴛʜɪs ʙᴏᴛ ᴀʀᴇ ғʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏsᴛᴇᴅ ʙʏ sᴏᴍᴇʙᴏᴅʏ ᴇʟsᴇ. Jᴜsᴛ ғᴏʀ ᴇᴀsʏ sᴇᴀʀᴄʜɪɴɢ, ᴛʜɪs ʙᴏᴛ ɪs ɪɴᴅᴇxɪɴɢ ғɪʟᴇs ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ Tᴇʟᴇɢʀᴀᴍ. Wᴇ ʀᴇsᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡs ᴀɴᴅ ᴡᴏʀᴋs ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ DMCA ᴀɴᴅ EU Cᴏᴘʏʀɪɢʜᴛ Dɪʀᴇᴄᴛɪᴠᴇ. Iғ ᴀɴʏᴛʜɪɴɢ ɪs ᴀɢᴀɪɴsᴛ ᴛʜᴇ ʟᴀᴡ, ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ sᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀs sᴏᴏɴ ᴀs ᴘᴏssɪʙʟᴇ. Iᴛ ɪs ғᴏʀʙɪᴅᴅᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, sᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ᴏʀ ʙʏ ᴀɴʏ ᴍᴇᴀɴs, sʜᴀʀᴇ, ᴏʀ ᴄᴏɴsᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪssɪᴏɴ ғʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. Iғ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪs ʙᴏᴛ ɪs ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇsᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟs ғᴏʀ ʀᴇᴍᴏᴠᴀʟ. Tʜᴇ ʙᴏᴛ ᴅᴏᴇs ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏғ ᴛʜᴇsᴇ ᴄᴏɴᴛᴇɴᴛs; ɪᴛ ᴏɴʟʏ ɪɴᴅᴇxᴇs ᴛʜᴇ ғɪʟᴇs ғʀᴏᴍ Tᴇʟᴇɢʀᴀᴍ. 

➥ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='t.me/filmyspotupdate'>ғɪʟᴍʏ sᴘᴏᴛ</a></b>"""

    STICKER_TXT = """<b>𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳.</b>
• 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
  ⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 
◉ Reply To Any Sticker [/stickerid]"""


    FONT_TXT= """⚙️ 𝐔𝐒𝐀𝐆𝐄

𝐘𝐎𝐔 𝐂𝐀𝐍 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐌𝐎𝐃𝐔𝐋𝐄 𝐓𝐎 𝐂𝐇𝐀𝐍𝐆𝐄 𝐅𝐎𝐍𝐓 𝐒𝐓𝐘𝐋𝐄 

<b>COMMAND</b> : /font your text (optional)
        <b> Eg:- /font Hello</b>"""

    CON_TXT = """<b><u>ᴄᴏᴜɴᴛʀʏ ɪɴғᴏ</b></u>
<b>Tʜɪs ᴍᴏᴅᴜʟᴇ ɪs ᴛᴏ ғɪɴᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴄᴏᴜɴᴛʀɪᴇs</b>
• /country [𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾] 
𝖤𝗑𝖺𝗆𝗉𝗅𝖾 :- <code>/country Nepal</code>"""

    RULE_TXT = """
<b>🔥 GROUP GUIDELINES 🔥

➥ Sᴇᴀʀᴄʜ Mᴏᴠɪᴇꜱ ᴡɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴘᴇʟʟɪɴɢ:
• Uꜱᴇ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ꜱᴘᴇʟʟɪɴɢ ғᴏʀ ᴍᴏᴠɪᴇ ᴛɪᴛʟᴇꜱ.

➥Exᴀᴍᴘʟᴇ:
Aᴠᴀᴛᴀʀ 𝟸𝟶𝟶𝟿 ✓
Aᴠᴀᴛᴀʀ Hɪɴᴅɪ ✓
Aᴠᴀᴛᴀʀ ᴍᴏᴠɪᴇ ✕
Aᴠᴀᴛᴀʀ Hɪɴᴅɪ ᴅᴜʙʙᴇᴅ.. ✕

➥ Sᴇᴀʀᴄʜ Wᴇʙ Sᴇʀɪᴇꜱ ɪɴ ᴛʜᴇ Sᴘᴇᴄɪғɪᴇᴅ Fᴏʀᴍᴀᴛ:
• Fᴏʟʟᴏᴡ ᴛʜᴇ ꜱᴘᴇᴄɪғɪᴇᴅ ғᴏʀᴍᴀᴛ ғᴏʀ ᴡᴇʙ ꜱᴇʀɪᴇꜱ ᴛɪᴛʟᴇꜱ.

➥Exᴀᴍᴘʟᴇ:
Vɪᴋɪɴɢꜱ S𝟶𝟷 ✓
Vɪᴋɪɴɢꜱ S𝟶𝟷E𝟶𝟷 ✓
Vɪᴋɪɴɢꜱ S𝟶𝟷 Hɪɴᴅɪ ✓
Vɪᴋɪɴɢꜱ S𝟶𝟷 Hɪɴᴅɪ ᴅᴜʙʙᴇᴅ ✕
Vɪᴋɪɴɢꜱ ꜱᴇᴀꜱᴏɴ 𝟷 ✕
Vɪᴋɪɴɢꜱ ᴡᴇʙ ꜱᴇʀɪᴇꜱ ✕

➥ Nᴏ Sᴇʟғ-Pʀᴏᴍᴏᴛɪᴏɴ:
• Aᴠᴏɪᴅ ᴘʀᴏᴍᴏᴛɪɴɢ ʏᴏᴜʀꜱᴇʟғ ᴏʀ ᴏᴛʜᴇʀꜱ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.

➥ Nᴏ Mᴇᴅɪᴀ, Dᴏᴄᴜᴍᴇɴᴛꜱ, ᴏʀ URLꜱ:
• Dᴏ ɴᴏᴛ ꜱʜᴀʀᴇ ᴀɴʏ ᴘʜᴏᴛᴏꜱ, ᴠɪᴅᴇᴏꜱ, ᴅᴏᴄᴜᴍᴇɴᴛꜱ, ᴏʀ URLꜱ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.

➥ Rᴇǫᴜᴇꜱᴛꜱ Lɪᴍɪᴛᴇᴅ ᴛᴏ Mᴏᴠɪᴇꜱ, Sᴇʀɪᴇꜱ, ᴀɴᴅ Aᴍɪɴᴇꜱ:
• Oɴʟʏ ʀᴇǫᴜᴇꜱᴛ ᴍᴏᴠɪᴇꜱ, ꜱᴇʀɪᴇꜱ, ᴏʀ ᴀɴɪᴍᴇ-ʀᴇʟᴀᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ.

⚠️ Nᴏᴛᴇ: Aʟʟ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ᴀғᴛᴇʀ 𝟷𝟶 ᴍɪɴᴜᴛᴇꜱ ᴛᴏ ᴄᴏᴍᴘʟʏ ᴡɪᴛʜ ᴄᴏᴘʏʀɪɢʜᴛ ʀᴇɢᴜʟᴀᴛɪᴏɴꜱ.</b>"""