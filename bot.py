import openai_secret_manager
import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

6099115467:AAEpmb-FsKIcBmUqc8RY021PdfboJ7qZ88o = openai_secret_manager.get_secret("telegram_chatbot_token")["api_key"]
openai.api_key = openai_secret_manager.get_secret("openai")["api_key"]

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я готов отвечать на твои вопросы.")

def echo(update, context):
    user_message = update.message.text
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    bot_response = response.choices[0].text.strip()
    context.bot.send_message(chat_id=update.effective_chat.id, text=bot_response)

def main():
    updater = Updater(token=6099115467:AAEpmb-FsKIcBmUqc8RY021PdfboJ7qZ88o, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(Filters.text & ~Filters.command, echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
