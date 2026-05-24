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

# =========================
# TOKEN
# =========================
TOKEN = "YOUR_NEW_BOT_TOKEN"


# =========================
# DATA
# =========================
DATA = {

    "alpha": {
        "title": "🔥1. COMBO 🔥",

        "images": [
            "images/alpha1.jpg",
            "images/alpha2.jpg",
            "images/alpha3.jpg",
            "images/alpha4.jpg",
            "images/alpha5.jpg",
            "images/alpha6.jpg",
            "images/alpha7.jpg"
        ],

        "caption": """
🔥 𝐀𝐋𝐏𝐇𝐀 𝐋𝐈𝐍𝐊𝐒 🔥

✅ 50+ 𝐙𝐢𝐩 𝐟𝐢𝐥𝐞𝐬
✅ 100+ 𝐆𝐫𝐨𝐮𝐩𝐬 𝐥𝐢𝐧𝐤𝐬
✅ 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐚𝐜𝐜𝐞𝐬𝐬

💰 𝐏𝐫𝐢𝐜𝐞 : 199₹

👑 𝐒𝐞𝐥𝐥𝐞𝐫 : @itsmeBBeee
"""
    },

    "beta": {
        "title": "🔥2. COMBO 🔥",

        "images": [
            "images/beta1.jpg",
            "images/beta2.jpg",
            "images/beta3.jpg",
            "images/beta4.jpg",
            "images/beta5.jpg",
            "images/beta6.jpg",
            "images/beta7.jpg"
        ],

        "caption": """
🔥 𝐁𝐄𝐓𝐀 𝐋𝐈𝐍𝐊𝐒 🔥

✅ 100+ 𝐙𝐢𝐩 𝐟𝐢𝐥𝐞𝐬
✅ 200+ 𝐆𝐫𝐨𝐮𝐩𝐬 𝐥𝐢𝐧𝐤𝐬
✅ 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐚𝐜𝐜𝐞𝐬𝐬

💰 𝐏𝐫𝐢𝐜𝐞 : 299₹

👑 𝐒𝐞𝐥𝐥𝐞𝐫 : @itsmeBBeee
"""
    },

    "gamma": {
        "title": "🔥3. COMBO 🔥",

        "images": [
            "images/gamma1.jpg",
            "images/gamma2.jpg",
            "images/gamma3.jpg",
            "images/gamma4.jpg",
            "images/gamma5.jpg",
            "images/gamma6.jpg",
            "images/gamma7.jpg",
            "images/gamma8.jpg",
            "images/gamma9.jpg",
            "images/gamma10.jpg"
        ],

        "caption": """
🔥 𝐆𝐀𝐌𝐌𝐀 𝐋𝐈𝐍𝐊𝐒 🔥

✅ 200+ 𝐙𝐢𝐩 𝐟𝐢𝐥𝐞𝐬
✅ 300+ 𝐆𝐫𝐨𝐮𝐩𝐬 𝐥𝐢𝐧𝐤𝐬
✅ 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐚𝐜𝐜𝐞𝐬𝐬

💰 𝐏𝐫𝐢𝐜𝐞 : 499₹

👑 𝐒𝐞𝐥𝐥𝐞𝐫 : @itsmeBBeee
"""
    },

    "delta": {
        "title": "🔥4. COMBO 🔥",

        "images": [
            "images/delta1.jpg",
            "images/delta2.jpg",
            "images/delta3.jpg",
            "images/delta4.jpg",
            "images/delta5.jpg",
            "images/delta6.jpg",
            "images/delta7.jpg",
            "images/delta8.jpg",
            "images/delta9.jpg",
            "images/delta10.jpg"
        ],

        "caption": """
🔥 𝐒𝐈𝐆𝐌𝐀 𝐋𝐈𝐍𝐊𝐒 🔥

✅ 250+ 𝐙𝐢𝐩 𝐟𝐢𝐥𝐞𝐬
✅ 400+ 𝐆𝐫𝐨𝐮𝐩𝐬 𝐥𝐢𝐧𝐤𝐬
✅ 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐚𝐜𝐜𝐞𝐬𝐬

💰 𝐏𝐫𝐢𝐜𝐞 : 699₹

👑 𝐒𝐞𝐥𝐥𝐞𝐫 : @itsmeBBeee
"""
    }

}


# =========================
# START COMMAND
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = []

    for key, value in DATA.items():

        keyboard.append([
            InlineKeyboardButton(
                value["title"],
                callback_data=key
            )
        ])

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 WELCOME TO BULK LINKS HUB 🔥\n\nChoose Your Package:",
        reply_markup=reply_markup
    )


# =========================
# BUTTON CLICK
# =========================
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

        opened_files = []

        for index, image_path in enumerate(data["images"]):

            if not os.path.exists(image_path):

                await query.message.reply_text(
                    f"Image not found:\n{image_path}"
                )

                return

            photo = open(image_path, "rb")

            opened_files.append(photo)

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

        # close files
        for file in opened_files:
            file.close()

    except Exception as e:

        print("ERROR:", e)

        await query.message.reply_text(
            f"Something went wrong:\n{e}"
        )


# =========================
# MAIN
# =========================
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
