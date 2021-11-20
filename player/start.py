from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from config import SOURCE_CODE, ASSISTANT_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, BOT_USERNAME
from plugins.tr import *
from pyrogram.errors import MessageNotModified

@Client.on_message(filters.command("start"))
async def start(client, message):
   buttons = [
               [
                               InlineKeyboardButton("📚Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", callback_data="help"),
                                           ],
                                                       [
                                                                       InlineKeyboardButton("📂Sᴏᴜʀᴄᴇ", url=f"https://{SOURCE_CODE}"),
                                                                                       InlineKeyboardButton("⏫Cʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                                                                                                   ],
                                                                                                               [
                                                                                                                               InlineKeyboardButton("ℹ️Aʙᴏᴜᴛ", callback_data="about"),
                                                                                                                                               InlineKeyboardButton("🦄Pegasus Network ", url ="t.me/PegasusXteam"),
                                                                                                                                                           ],
                                                                                                                                                                       [
                                                                                                                                                                                      InlineKeyboardButton("[•➕Sᴜᴍᴍᴏɴ Mᴇ•]", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                                                                                                                                                                                                  ]
                                                                                                                                                                                                              ]
                                                                                                                                                                                                                 reply_markup = InlineKeyboardMarkup(buttons)
                                                                                                                                                                                                                    if message.chat.type == 'private':
                                                                                                                                                                                                                           await message.reply_text(
                                                                                                                                                                                                                                     START_TEXT,
                                                                                                                                                                                                                                               reply_markup=reply_markup
                                                                                                                                                                                                                                                      )
                                                                                                                                                                                                                                                         else:
                                                                                                                                                                                                                                                               await message.reply(f"**@{ASSISTANT_NAME} is Here to Make your VC amazing With me[✨](https://telegra.ph/file/1db9b30f34796d8df26b8.jpg)**")
@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
            buttons = [
                        [
                                        InlineKeyboardButton("[•Bᴀᴄᴋ•]", callback_data="start"),
                                                        InlineKeyboardButton ("❣️Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}"),
                                                                    ]
                                                                                ]
                                                                                        reply_markup = InlineKeyboardMarkup(buttons)
                                                                                                try:
                                                                                                            await query.edit_message_text(
                                                                                                                            HELP_TEXT,
                                                                                                                                            reply_markup=reply_markup
                                                                                                                                                        )
                                                                                                                                                                except MessageNotModified:
                                                                                                                                                                            pass
    elif query.data=="about":
            buttons = [
                        [
                                        InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start"),
                                                        InlineKeyboardButton ("Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}"),
                                                                    ]
                                                                                ]
                                                                                        reply_markup = InlineKeyboardMarkup(buttons)
                                                                                                try:
                                                                                                            await query.edit_message_text(
                                                                                                                            ABOUT_TEXT,
                                                                                                                                            reply_markup=reply_markup
                                                                                                                                                        )
                                                                                                                                                                except MessageNotModified:
                                                                                                                                                                            pass
    elif query.data=="devs":
            buttons = [
                        [
                                        InlineKeyboardButton("Lᴏᴜɪꜱ", url="https://t.me/DeeCodeBots"),
                                                        InlineKeyboardButton("Eʀʀᴏʀ", url="https://t.me/ProErrorXD"),
                                                                    ],
                                                                                [
                                                                                                InlineKeyboardButton("Bʟᴀᴢᴇ", url="https://t.me/piroXpower"),
                                                                                                                InlineKeyboardButton("Pʀɪɴᴄᴇ", url="https://t.me/DEVILDAD_PRINCE"),
                                                                                                                            ],
                                                                                                                                        [
                                                                                                                                                        InlineKeyboardButton("Hʏᴏᴋᴀ", url="https://t.me/Pratheek_XD"),
                                                                                                                                                                        InlineKeyboardButton("Zᴀʟɪᴍ", url="https://t.me/Jalim_Munda"),
                                                                                                                                                                                    ],
                                                                                                                                                                                                [
                                                                                                                                                                                                                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start"),
                                                                                                                                                                                                                            ]
                                                                                                                                                                                                                                        ]
                                                                                                                                                                                                                                                reply_markup = InlineKeyboardMarkup(buttons)
                                                                                                                                                                                                                                                        try:
                                                                                                                                                                                                                                                                    await query.edit_message_text(
                                                                                                                                                                                                                                                                                    DEVS_TEXT,
                                                                                                                                                                                                                                                                                                    reply_markup=reply_markup
                                                                                                                                                                                                                                                                                                                )
                                                                                                                                                                                                                                                                                                                        except MessageNotModified:
                                                                                                                                                                                                                                                                                                                                    pass
    elif query.data=="start":
            buttons = [
                        [
                                        InlineKeyboardButton("Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", callback_data="help"),
                                                    ],
                                                                [
                                                                                InlineKeyboardButton("Sᴏᴜʀᴄᴇ", url=f"https://{SOURCE_CODE}"),
                                                                                                InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                                                                                                            ],
                                                                                                                        [
                                                                                                                                        InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about"),
                                                                                                                                                        InlineKeyboardButton("Dᴇᴠꜱ", callback_data="devs"),
                                                                                                                                                                    ],
                                                                                                                                                                                [
                                                                                                                                                                                               InlineKeyboardButton("Sᴜᴍᴍᴏɴ Mᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                                                                                                                                                                                                           ]
                                                                                                                                                                                                                       ]
                                                                                                                                                                                                                               reply_markup = InlineKeyboardMarkup(buttons)
                                                                                                                                                                                                                                       try:
                                                                                                                                                                                                                                                   await query.edit_message_text(
                                                                                                                                                                                                                                                                   START_TEXT,
                                                                                                                                                                                                                                                                                   reply_markup=reply_markup
                                                                                                                                                                                                                                                                                               )
                                                                                                                                                                                                                                                                                                       except MessageNotModified:
                                                                                                                                                                                                                                                                                                                   pass
