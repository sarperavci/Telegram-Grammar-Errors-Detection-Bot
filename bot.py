from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
import openai,base64,telegram


TOKEN = "<YOUR_TELEGRAM_BOT_TOKEN>"
openai.api_key = "<YOUR_OPENAI_API_KEY>"



def create(text):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[

              {"role": "user", "content": f"""
  Find critical grammar errors in this text: {text} """},
          ]
  )

    result = ''
    for choice in response.choices:
        result += choice.message.content
        print(choice.message.content)
    return result



def process_message(update, context):
    user_id = update.effective_chat.id
    word = update.message.text
    response = create(word)
    context.bot.send_message(chat_id=user_id, text=response
                ,  parse_mode=telegram.ParseMode.HTML)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_message))


    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
