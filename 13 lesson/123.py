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
        return "Пока не придумал, приходите попозже"

@bot.message_handler(commands=['start'])
def start(m,res=False):
    bot.send_message(m.chat.id, 'Позолоти ручку, всю правду расскажу')

@bot.message_handler(content_types=['text'])
def hand_t(message):
    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(non_stop=True, interval=0)


# @bot.message_handler(commands=['start'])
# def start(m,res=False):
#     bot.send_message(m.chat.id, 'Чо как?!')


# @bot.message_handler(content_types=['text'])
# def hend_t(message):
#     bot.send_message(message.chat.id, 'Ты говоришь ' + message.text +'?')

# bot.polling(non_stop=True, interval=0)

