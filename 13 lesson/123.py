import telebot, wikipedia, re

bot = telebot.TeleBot('6094037697:AAHobYOlU3sxk7NgmWGiO6FvOWN60I88C3k')

wikipedia.set_lang('ru')

def getwiki(s):
    try:
        m = wikipedia.page(s)
        wikitext = m.content[:1000]
        wikidot = wikitext.split('.')
        wikiall = wikidot[:-1]
        wikitext2 = ''

        for i in wikidot:
            if not('==' in i):
                if (len((i.strip()))>3):
                    wikitext2 = wikitext2+i+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return "Все операторы заняты, перезвоните попозже..."

@bot.message_handler(commands=['start'])
def start(m,res=False):
    bot.send_message(m.chat.id, 'Позолоти ручку, всю правду расскажу')

@bot.message_handler(content_types=['text'])
def hand_t(message):
    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(non_stop=True, interval=0)

# AFKSTRAFKSTR=[ 
#     "Я вернусь через несколько минут, и если меня не будет..., подождите дольше.",
#     "Меня сейчас здесь нет, так что, вероятно, я где-то в другом месте.",
#     "В данный момент я не за клавиатурой, но если ты будешь достаточно громко кричать на свой экран, я, возможно, просто услышу тебя.",
#     "Пожалуйста, оставьте сообщение и дайте мне почувствовать себя еще более важным, чем я уже есть.",
#     "Меня здесь нет, так что прекрати мне писать,в противном случае вы обнаружите, что экран заполнен вашими собственными сообщениями.",
#     "Я сейчас недоступен, поэтому, пожалуйста, оставьте свое имя, номер и адрес, и я свяжусь с вами позже.",
#     "Извините, меня сейчас здесь нет. Не стесняйтесь общаться с моим пользовательским ботом столько, сколько захотите. Я свяжусь с dfvb позже.",
# ]


# @bot.message_handler(commands=['start'])
# def start(m,res=False):
#     bot.send_message(m.chat.id, 'Чо как?!')


# @bot.message_handler(content_types=['text'])
# def hend_t(message):
#     bot.send_message(message.chat.id, 'Ты говоришь ' + message.text +'?')

# bot.polling(non_stop=True, interval=0)

