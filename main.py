from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7671868658:AAGg5sxvTZvU-hRLnl6_HvG4yONlzUG_Aiw"

# Function to generate the main inline keyboard
def get_main_buttons():
    keyboard = [
        [InlineKeyboardButton("💎 Join VIP Signals", callback_data='vip_signals')],
        [InlineKeyboardButton("🎁 Benefits of Joining VIP", callback_data='vip_benefits')],
        [InlineKeyboardButton("📚 Learn Price Action", url="http://yt.openinapp.co/cqznx")],  # Direct YouTube link
        [InlineKeyboardButton("👨‍💼 Admin (Support)", url="https://t.me/WayneAdmin01")]  # Direct Telegram Chat
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.message.from_user.first_name  # Get user's first name

    # Step 1: Send an Image
    chat_id = update.message.chat_id
    with open("wayne.jpg", "rb") as image_file:  # Replace with your image file
        await context.bot.send_photo(chat_id=chat_id, photo=image_file)

    # Step 2: Send a text response with buttons
    message_text = f"👋 Hello {user_first_name}!\n\n" \
                   "**Welcome To 'Wayne Traders'** 🔥\n" \
                   "📊 Real Price Action Trading Without Indicators!\n\n" \
                   "🎯 Now You Have Joined a Good Telegram Channel.\n" \
                   "🍀 It's Your Luck That You Found Us!\n\n" \
                   "📌 Select an option below to proceed:"

    await update.message.reply_text(message_text, reply_markup=get_main_buttons())

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_first_name = query.from_user.first_name  # Fix: Get first name from callback query

    if query.data == "vip_signals":
        vip_message = f"Hey {user_first_name}👋\n\n" \
                      "**Welcome To 'Wayne Traders'** 🔥\n" \
                      "📊 Real Price Action Trading Without Indicators\n\n" \
                      "🎯 Now You Have Joined a Good Telegram Channel.\n" \
                      "🍀 It's Your Luck That You Found Us...\n\n" \
                      "**On This Channel You Will Get:**\n" \
                      "✅ Non-Martingale 99% Accurate Price Action-Based Signals **FOR FREE!** 🎯\n\n" \
                      "🔥 **IF You Want To Join Our VIP GROUP, Then Follow These Steps:**\n\n" \
                      "1️⃣ **CREATE A NEW ACCOUNT**\n" \
                      "👉 [CLICK HERE TO REGISTER](https://bit.ly/WayneFreeSignals)\n\n" \
                      "2️⃣ **DEPOSIT $40 or Above** 💰\n\n" \
                      "3️⃣ **AFTER DEPOSIT, SEND YOUR TRADER ID TO THIS BOT** 📩\n\n" \
                      "✅ **THEN, THE BOT WILL AUTOMATICALLY ADD YOU TO OUR VIP GROUP!** 🚀"

        await query.message.reply_text(vip_message, reply_markup=get_main_buttons(), parse_mode="Markdown", disable_web_page_preview=True)

    elif query.data == "vip_benefits":
        benefits_message = "🔥 **NOW YOU ARE ON THE RIGHT PATH!** 🔥\n\n" \
                           "🎯 **YOU DECIDED TO JOIN OUR VIP FOR FREE!** 🚀\n\n" \
                           "💡 **SO, WHAT ARE THE BENEFITS OF JOINING OUR VIP GROUP?** 💡\n\n" \
                           "📌 **WHAT WILL YOU GET AFTER REGISTRATION AND MAKING A DEPOSIT?**\n\n" \
                           "1️⃣ **YOU WILL GET 8-9 HIGHLY ACCURATE SIGNALS** FOR POCKET OPTION 📊\n\n" \
                           "2️⃣ **SIGNALS WILL BE BASED ON TRUE PRICE ACTION WITH NON-MARTINGALE** 🎯\n\n" \
                           "3️⃣ **YOU WILL GET EXCLUSIVE PDFs & PREMIUM VIDEOS ON TRADING** 🎥📖\n\n" \
                           "4️⃣ **OUR SUPPORT TEAM WILL GUIDE YOU WITH THE BEST MONEY MANAGEMENT STRATEGIES** 💰✅\n\n" \
                           "🚀 **THESE ARE ALL THE BENEFITS YOU WILL GET AFTER REGISTRATION & JOINING OUR VIP!** 🚀"

        await query.message.reply_text(benefits_message, reply_markup=get_main_buttons(), parse_mode="Markdown")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
