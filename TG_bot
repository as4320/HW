import telebot
from config import TOKEN
from extensions import ConvertionException, Converter, show_all

bot = telebot.TeleBot(TOKEN)
data = show_all()

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = f'Чтобы  начать работу введите команду боту в следующем формате(через пробел):\n \
<валюта 1> <валюта 2> <кол-во конвертируемой валюты>\n Пример: USD RUB 100 \n {"-" * 96}\
Для получение списка поддерживаемых валют, введите /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):

    print(data)
    
    text = ' Доступные валюты:'
    for key in data.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Неверное число значений!')
        
        quote, base, amount = values
        total_base = Converter.convert1(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        bot.send_message(message.chat.id, f'{"%.2f" % total_base} {base}')

bot.polling(non_stop=True)
