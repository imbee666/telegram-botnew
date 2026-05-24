from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

import os

TOKEN = "8480592401:AAET8X7IQeMRP8ZRrkXUmYquHhEpdAw0RIE"

DATA = {

    "alpha": {
    "title": "🔥1. COMBO 🔥",

    "images": [
        r"D:\alpha1.jpg",
        r"D:\alpha2.jpg",
        r"D:\alpha3.jpg",
        r"D:\alpha4.jpg",
        r"D:\alpha5.jpg",
        r"D:\alpha6.jpg",
        r"D:\alpha7.jpg"
    ],

    "caption": """
🔥 𝐀𝐋𝐏𝐇𝐀 𝐋𝐈𝐍𝐊𝐒 🔥

✅ 50+ 𝐙𝐢𝐩 𝐟𝐢𝐥𝐞𝐬 ,
✅ 100+ 𝐆𝐫𝐨𝐮𝐩𝐬 𝐥𝐢𝐧𝐤𝐬, 
✅ 𝐏𝐫𝐞𝐦𝐢𝐮𝐦𝐚𝐜𝐜𝐞𝐬𝐬 ,

𝐂𝐚𝐭𝐞𝐠𝐨𝐫𝐢𝐞𝐬:- 𝐭𝐚𝐦𝐢𝐥,𝐦𝐚𝐥𝐥𝐮,𝐝𝐞𝐬𝐢 𝐬𝐨𝐮𝐭𝐡,𝐛𝐫𝐨&𝐬𝐢𝐬,𝐩𝐞𝐝𝐨 𝐦0𝐦.
𝐋𝐢𝐤𝐞 𝐭𝐡𝐢𝐬 100+ 𝐠𝐫𝐨𝐮𝐩 𝐥𝐢𝐧𝐤𝐬 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝

💰 𝐏𝐫𝐢𝐜𝐞  : 199₹
👑 𝐒𝐞𝐥𝐥𝐞𝐫 𝐢𝐝 :@itsmeBBeee
👑 𝐒𝐞𝐥𝐥𝐞𝐫 𝐢𝐝 :@itsmeBBeee
1,2,3,4 𝐚𝐥𝐥 4 𝐜𝐨𝐦𝐛𝐨𝐬 𝐢𝐧 1199𝐫𝐬 𝐨𝐧𝐥𝐲
""",
},

    "beta": {
        "title": "🔥2. COMBO 🔥",

        "images": [
            r"D:\beta1.jpg",
            r"D:\beta2.jpg",
            r"D:\beta3.jpg",
            r"D:\beta4.jpg",
            r"D:\beta5.jpg",
            r"D:\beta6.jpg",
            r"D:\beta7.jpg",
        ],

        "caption": """
🔥 𝐁𝐄𝐓𝐀 𝐋𝐈𝐍𝐊𝐒 🔥

✅ 100+ 𝐙𝐢𝐩 𝐟𝐢𝐥𝐞𝐬 ,
✅ 200+ 𝐆𝐫𝐨𝐮𝐩𝐬 𝐥𝐢𝐧𝐤𝐬, 
✅ 𝐏𝐫𝐞𝐦𝐢𝐮𝐦𝐚𝐜𝐜𝐞𝐬𝐬 ,

𝐂𝐚𝐫𝐞𝐠𝐨𝐫𝐢𝐞𝐬:-𝐦𝐨𝐦&𝐬𝐨𝐧,𝐫𝐞𝐚𝐥 𝐡𝐨𝐦𝐞 𝐬𝐩𝐲 𝐢𝐧𝐜𝐞𝐬𝐭,𝐩!𝐬𝐬 𝐬𝐩𝐲 𝐛𝐭𝐡 ,𝐜𝐚𝐧𝐝𝐢𝐝 𝐜𝐥𝐢𝐜𝐤𝐬 ,𝐦𝐚𝐥𝐥𝐮 𝐥𝐞𝐚𝐤𝐬 , 𝐬𝐥𝐞𝐩𝐩𝐢𝐧𝐠 𝐦&𝐬 ,𝐭𝐚𝐦𝐢𝐥 𝐯𝐨𝐢𝐜𝐞𝐬

𝐋𝐢𝐤𝐞 𝐭𝐡𝐢𝐬 200+ 𝐠𝐫𝐨𝐮𝐩 𝐥𝐢𝐧𝐤𝐬 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝

💰 𝐏𝐫𝐢𝐜𝐞 :  299₹
👑 𝐒𝐞𝐥𝐥𝐞𝐫 𝐢𝐝 :@itsmeBBeee
👑 𝐒𝐞𝐥𝐥𝐞𝐫 𝐢𝐝 :@itsmeBBeee 
1,2,3,4 𝐚𝐥𝐥 4 𝐜𝐨𝐦𝐛𝐨𝐬 𝐢𝐧 1199𝐫𝐬 𝐨𝐧𝐥𝐲
"""
    },

    "gamma": {
        "title": "🔥3. COMBO 🔥",

        "images": [
            r"D:\gamma1.jpg",
            r"D:\gamma2.jpg",
            r"D:\gamma3.jpg",
            r"D:\gamma4.jpg",
            r"D:\gamma5.jpg",
            r"D:\gamma6.jpg",
            r"D:\gamma7.jpg",
            r"D:\gamma8.jpg",
            r"D:\gamma9.jpg",
            r"D:\gamma10.jpg",
        ],

        "caption": """
🔥 𝐆𝐀𝐌𝐌𝐀 𝐋𝐈𝐍𝐊𝐒 🔥


✅ 200+ 𝐙𝐢𝐩 𝐟𝐢𝐥𝐞𝐬 ,
✅ 300+ 𝐆𝐫𝐨𝐮𝐩𝐬 𝐥𝐢𝐧𝐤𝐬, 
✅ 𝐏𝐫𝐞𝐦𝐢𝐮𝐦𝐚𝐜𝐜𝐞𝐬𝐬 ,

𝐂𝐚𝐭𝐞𝐠𝐨𝐫𝐢𝐞𝐬:- 𝐫𝐞𝐝 𝐥𝐲𝐭 ,𝐬𝐩𝐚,𝐬𝐨𝐮𝐭𝐡 𝐭𝐚𝐦𝐢𝐥,𝐝𝐞𝐬𝐢 𝐰𝐞𝐛 𝐬𝐞𝐫𝐢𝐞𝐬,𝐓𝐚𝐦𝐢𝐥 𝐭𝐚𝐧𝐠𝐨,𝐢𝐧𝐝 𝐬𝐡𝐞𝐦𝐚𝐥𝐞,𝐨𝐮𝐭 𝐝𝐨𝐨𝐫 𝐜𝐨𝐮𝐩𝐥𝐞, 𝐥𝐚𝐭𝐞𝐬𝐭 𝐝𝐞𝐬𝐢 ,𝐬𝐭𝐫𝐢𝐩 𝐜𝐡𝐚𝐭 ,𝐟𝐥𝐚𝐬𝐡 𝐜𝐚𝐧𝐝𝐢𝐝.
𝐋𝐢𝐤𝐞 𝐭𝐡𝐢𝐬 300+ 𝐠𝐫𝐨𝐮𝐩 𝐥𝐢𝐧𝐤𝐬 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝
𝐖𝐢𝐭𝐡 𝐭𝐡𝐢𝐬 𝐲𝐨𝐮 𝐰𝐢𝐥𝐥 𝐠𝐞𝐭 𝐝𝐚𝐢𝐥𝐲 𝐮𝐩𝐝𝐚𝐭𝐞𝐬 𝐚𝐧𝐝 𝐩𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧

💰 𝐏𝐫𝐢𝐜𝐞 :  499₹
👑 𝐒𝐞𝐥𝐥𝐞𝐫 𝐢𝐝 :@itsmeBBeee
👑 𝐒𝐞𝐥𝐥𝐞𝐫 𝐢𝐝 :@itsmeBBeee
1,2,3,4 𝐚𝐥𝐥 4 𝐜𝐨𝐦𝐛𝐨𝐬 𝐢𝐧 1199𝐫𝐬 𝐨𝐧𝐥𝐲
"""
    },

    "delta": {
        "title": "🔥4. COMBO 🔥",

        "images": [
            r"D:\delta1.jpg",
            r"D:\delta2.jpg",
            r"D:\delta3.jpg",
            r"D:\delta4.jpg",
            r"D:\delta5.jpg",
            r"D:\delta6.jpg",
            r"D:\delta7.jpg",
            r"D:\delta8.jpg",
            r"D:\delta9.jpg",
            r"D:\delta10.jpg",
        ],

        "caption": """
🔥 𝐒𝐈𝐆𝐌𝐀 𝐋𝐈𝐍𝐊𝐒 🔥

✅ 250+ 𝐙𝐢𝐩 𝐟𝐢𝐥𝐞𝐬 ,
✅ 400+ 𝐆𝐫𝐨𝐮𝐩𝐬 𝐥𝐢𝐧𝐤𝐬, 
✅ 𝐏𝐫𝐞𝐦𝐢𝐮𝐦𝐚𝐜𝐜𝐞𝐬𝐬 ,

𝐂𝐚𝐭𝐞𝐠𝐨𝐫𝐢𝐞𝐬:- 𝐜𝐜𝐭𝐯 𝐥𝐞𝐚𝐤𝐬,𝐚𝐧𝐢𝐦𝐞,𝐦𝐚𝐥𝐥𝐮 𝐰𝐞𝐛 𝐬𝐞𝐫𝐢𝐞𝐬,𝐨𝐮𝐭 𝐝𝐨𝐨𝐫 𝐥𝐞𝐚𝐤𝐞𝐝,𝐜𝐡𝐢𝐧𝐚 ,𝐡𝐨𝐥𝐥𝐲𝐰𝐨𝐨𝐝 𝐜𝐞𝐥𝐞𝐛𝐫𝐢𝐭𝐲,𝐯𝐢𝐫𝐚𝐥 𝐥𝐞𝐚𝐤𝐬,𝐩0𝐫𝐧 𝐡𝐮𝐛 𝐩𝐫𝐞𝐦𝐢𝐮𝐦,𝐩𝐮𝐫𝐞 𝐭𝐮𝐫𝐛𝐨 𝐩𝐫𝐞𝐦𝐢𝐮𝐦,𝐩0𝐫𝐧𝐬𝐭𝐚𝐫𝐬,𝐢𝐧𝐝 𝐬𝐜𝐡𝐥&𝐜𝐥𝐠 𝐠𝐢𝐫𝐥𝐬 ,𝐩0𝐫𝐧 𝐦𝐨𝐯𝐢𝐞𝐬,𝐡𝐢𝐧𝐝𝐢 𝐚𝐝𝐮𝐥𝐭 𝐬𝐞𝐫𝐢𝐞𝐬
𝐋𝐢𝐤𝐞 𝐭𝐡𝐢𝐬 400+ 𝐠𝐫𝐨𝐮𝐩 𝐥𝐢𝐧𝐤𝐬 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝

𝐖𝐢𝐭𝐡 𝐭𝐡𝐢𝐬 𝐲𝐨𝐮 𝐰𝐢𝐥𝐥 𝐠𝐞𝐭 𝐩𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝐝𝐚𝐢𝐥𝐲 𝐰𝐞 𝐮𝐩𝐥𝐨𝐚𝐝 𝐧𝐞𝐰 𝐥𝐢𝐧𝐤𝐬 𝐰𝐢𝐭𝐡 𝐥𝐢𝐟𝐞 𝐭𝐲𝐦 𝐚𝐜𝐜𝐞𝐬𝐬 𝐚𝐧𝐝 𝐛𝐚𝐜𝐤𝐮𝐩 𝐮𝐩 𝐠𝐫𝐨𝐮𝐩𝐬 𝐚𝐥𝐬𝐨

💰 𝐏𝐫𝐢𝐜𝐞  : 699₹
👑 𝐒𝐞𝐥𝐥𝐞𝐫 𝐢𝐝 :@itsmeBBeee.
👑 𝐒𝐞𝐥𝐥𝐞𝐫 𝐢𝐝 :@itsmeBBeee.
1,2,3,4 𝐚𝐥𝐥 4 𝐜𝐨𝐦𝐛𝐨𝐬 𝐢𝐧 1199𝐫𝐬 𝐨𝐧𝐥𝐲
"""
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [
            InlineKeyboardButton(
                DATA["alpha"]["title"],
                callback_data="alpha"
            )
        ],

        [
            InlineKeyboardButton(
                DATA["beta"]["title"],
                callback_data="beta"
            )
        ],

        [
            InlineKeyboardButton(
                DATA["gamma"]["title"],
                callback_data="gamma"
            )
        ],

        [
            InlineKeyboardButton(
                DATA["delta"]["title"],
                callback_data="delta"
            )
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 WELCOME TO BULK LINKS HUB 🔥\n\nChoose Your Package:",
        reply_markup=reply_markup
    )


async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    try:

        data = DATA.get(query.data)

        if not data:

            await query.message.reply_text(
                "Invalid option selected."
            )

            return

        media = []

        for index, image_path in enumerate(data["images"]):

            if not os.path.exists(image_path):

                await query.message.reply_text(
                    f"Image not found:\n{image_path}"
                )

                return

            photo = open(image_path, "rb")

            if index == 0:

                media.append(
                    InputMediaPhoto(
                        media=photo,
                        caption=data["caption"]
                    )
                )

            else:

                media.append(
                    InputMediaPhoto(
                        media=photo
                    )
                )

        await query.message.reply_media_group(media)

    except Exception as e:

        print("ERROR:", e)

        await query.message.reply_text(
            f"Something went wrong:\n{e}"
        )


def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(button_click)
    )

    print("Bot running...")

    app.run_polling()


if __name__ == "__main__":
    main()