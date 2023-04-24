import asyncio
import re
import os
import random
import requests
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from typing import Union
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from X2RZ7WX import app
from strings.filters import command

def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"",
            ),
            InlineKeyboardButton(
                text=_["S_B_S"], callback_data="amm"
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], callback_data="settings_helper"
            ),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                ),
                InlineKeyboardButton(

                    text=_["S_B_9"], url=f"https://t.me/so_alfaa"

                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                    )
                ]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_8"], callback_data="settings_back_helper"
            )
        ]
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                    )
                ]
            )
    if GITHUB_REPO and OWNER:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_7"], user_id=OWNER),
                InlineKeyboardButton(
                    text=_["S_B_6"], url=f"{GITHUB_REPO}"
                ),
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_6"], url=f"{GITHUB_REPO}"
                    ),
                ]
            )
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_11"], url=f"https://t.me/ApplicationsANTER"
                    ),
                    InlineKeyboardButton(

                        text=_["S_B_12"], url=f"https://t.me/ApplicationsANTER"

                    ),
                ]
            )
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_7"], user_id=OWNER
                    ),
                    InlineKeyboardButton(

                        text=_["S_B_10"], url=f"https://t.me/ApplicationsANTER"

                    ),
                ]
            )
    buttons.append(
        [InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG")]
    )
    return buttons





  
  
REPLY_MESSAGE = "- اهلين ياعيني عندك الازرار تحت استمتع"

REPLY_MESSAGE_BUTTONS = [
         [
             ("طريقة تشغيل ميرا"),                   
             ("اوامر ميرا")

          ],
          [
             ("المطور"),
             ("السورس")
          ],
          [
             ("اخفاء الازرار")
          ]
]

  
@app.on_message(filters.private & filters.command("commandsejie8"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



@app.on_message(filters.regex("kekeoei3") & filters.private)
async def down(client, message):
          m = await message.reply("**- ابشر عيني تم اخفاء الازرار بنجاح\n- لو تبي تطلعها مرة ثانية ارسل**-› /commands", reply_markup= ReplyKeyboardRemove(selective=True))
########رسائل الستارت########

@app.on_message(filters.private & command("keeii3i3e"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""- **هلا والله ياعيني عشان تفعل بوت ميرا اتبع الخطوات الي بالاسفل**

1 • ضيف البوت لقروبك 
2 • ارفعه مشرف بكل الصلاحيات 
3 • لو تبي تشوف الاوامر اكتب [ م الاوامر ] ولو تبي تشغل على طول اكتب ميرا شغلي + اسم المقطع الصوتي

• مثال : ميرا شغلي واتنسيت

- لو واجهت مشكله او ما فهمت خطوة كلم مطور البوت ~ @ApplicationsANTER""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.private & command("ekeiei3ek"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""**- اهلين فيك بسورس ميرا ياحلو
• لو تبي تنصب مثل هالبوت تواصل مع مطور السورس
• عندك استفسار او اقتراح بخصوص البوت تواصل مع مطور البوت**

مطور السورس -› [Khaled](t.me/ApplicationsANTER)
قناة السورس -› [𝑺𝒐𝒖𝒓𝒄𝒆 𝑴𝒊𝒓𝒂](t.me/ApplicationsANTER)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

###################new lian#############

REPLY_MESSAGEE = "- هلا فيك في قسم الاوامر"

REPLY_MESSAGE_BUTTONSS = [
         [
             ("شرح التشغيل بمنصات الاغاني")
          ],
          [
             ("اوامر المجموعة"),
             ("اوامر القنوات")
          ],
          [
             ("طريقة البحث"),
             ("ربط القنوات")
          ],
          [
             ("حفظ التشغيل")             
          ],
          [
             ("رجوع")
          ],
          [
            ("اخفاء الازرار")
          ]
]

  
@app.on_message(filters.private & command("ekkeo33"))
async def com(_, message: Message):             
        text = REPLY_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONSS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



@app.on_message(filters.private & command("kekeoeie"))
async def bask(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


@app.on_message(filters.private & command("ekieo3i3"))
async def mnsat(client: Client, message: Message):
    await message.reply_text(f"""** اهلين فيك في قسم تشغيل المنصات
- المنصات المدعومة هي ↓

• Telegram
• Youtube
• SoundCloud
• AppleMusic
• Spotify

- بتلقى شرح لكل هالمنصات في المجموعة اكتب فقط م الاوامر**

- [𝑺𝒐𝒖𝒓𝒄𝒆 𝑴𝒊𝒓𝒂](t.me/ApplicationsANTER)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),

                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.private & command("jejejei3i3"))
async def laksk(client: Client, message: Message):
    await message.reply_text(f"""\n\n\n╭── • [𝗠𝗶𝗿𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/ApplicationsANTER) • ──╮\n\n ✧ **اوامر التشغيل بالمجموعة**\n\n• **ميرا شغلي + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني فالمجموعة\n\n• **ميرا طفيها** او ** ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **ميرا الي بعده** او **تخطي**\n-› لتشغيل التالي بالانتظار\n\n • **ميرا اص** او **اسكتي**\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n• **ميرا تكلمي**\n-› لالغاء الكتم واكمال التشغيل\n\n• **ميرا ايقاف مؤقت** او **ايقاف مؤقت**\n -› لايقاف التشغيل بشكل مؤقت\n\n• **ميرا كملي** او **استئناف**\n -› لاكمال التشغيل بعد الايقاف المؤقت\n\n╰── • [𝗠𝗶𝗿𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/ApplicationsANTER) • ──╯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )


@app.on_message(filters.private & command("jejeeii3"))
async def channvom(client: Client, message: Message):
    await message.reply_text(f"""\n\n╭── • [𝗠𝗶𝗿𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/ApplicationsANTER) • ──╮\n\n ✧ **اوامر التشغيل بالقنوات**\n\n• **ق تشغيل + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني بالقناة\n\n• **ق ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **ق تخطي**\n-› لتشغيل التالي بالانتظار\n\n • **ق اص**\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n• **ق كملي**\n-› لالغاء الكتم واكمال التشغيل\n\n• **ق ايقاف مؤقت**\n -› لايقاف التشغيل بشكل مؤقت\n\n• **ق استئناف**\n -› لاكمال التشغيل بعد الايقاف المؤقت\n\n╰── • [𝗠𝗶𝗿𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/ApplicationsANTER) • ──╯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.private & command("ejeie83"))
async def dowmmr(client: Client, message: Message):
    await message.reply_text(f"""اهلين فيك في قسم التحميل ♪
للبحث عن اغنية او فيديو استخدم الامر التالي ↓

[ بحث + اسم المطلوب ..]

مثال -› بحث بحبك وحشتني

- الامر يشتغل بخاص البوت والمجموعة ايضا .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
@app.on_message(filters.private & command("jejejeen"))
async def dowhmr(client: Client, message: Message):
    await message.reply_text(f"""✧ **اهلين فيك في قسم حفظ التشغيل**\n\n- **حفظ التشغيل هو حفظ الاغاني الي اشتغلت بالمجموعة وحفظها يعني انك تقدر تشغلها بدون ما ترجع تبحث عنها مرة ثانية وتبقى محفوظة لك فقط**\n\n- عشان تحفظ الاغنية او المُشغل الحالي بالمكالمة لازم تضغط على زر -› ( **حفظ التشغيل** )\n\n- عشان تشوف الاغاني او الصوتيات الي حفظتها اكتب امر -› ( **قائمة تشغيلي** )\n\n- وطريقة تشغيل قائمتك تكتب فقط امر -› ( **تشغيل قائمتي** )\n\n- طريقة حذف اغنية او مقطع من محفوظاتك تكتب امر -› ( **حذف تشغيلي** ) وتكمل الخطوات بخاص البوت ..\n\n✶ **ملاحظة : اذا حفظت اغنية بتكون محفوظة عندك فقط يعني كل شخص عنده قائمة تشغيل خاصة فيه ومحد يقدر يحفظ اغنية عندك والعكس ايضا\n✶ لو ما فهمت تابع الفيديو الي فوق عشان تفهم اكثر ❤️**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.private & command("ekwkw9"))
async def dowhmo(client: Client, message: Message):
    await message.reply_text("""- هلا والله\n◌**عشان تشغل بالقنوات لازم تسوي بعض الخطوات وهي◌** :\n\n1 -› تدخل البوت قناتك وترفعه مشرف\n2 -› ترجع للقروب وتكتب { **ربط + يوزر القناة** }\n3 -› **اضغط على زر اوامر التشغيل عشان تعرف كيف تشغل**..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
