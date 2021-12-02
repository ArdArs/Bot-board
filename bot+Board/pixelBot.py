import telebot
import drawing
# import socket
# clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# clientsocket.connect(('192.168.1.86', 2000))
#https://t.me/pixelControlbot
draw = drawing.Draw(2000)
bot = telebot.TeleBot('2057090131:AAG20n8dEIht5Kj9jkAAX9cWVY44K_g4qI8')


link = ''


@bot.message_handler(commands=['start'])
def start(ms):
    bot.send_message(ms.chat.id, f'Привет! Этот бот управляет доской, которую можно увидеть в трансляции на YouTube. ССЫЛКА: {link}\nКоманда /clr [x] [y] - выключает пиксель\nКоманда /set [x] [y] - выключает пиксель\nНесколько команд в одно сообщение не РАБОТЕТ. на остальной текст бот не реагирует')


@bot.message_handler(commands=['set'])
def setCm(ms):
    #/set x y
    try:
        cm = ms.text[5:]
        x = cm.split(' ')[0]
        y = cm.split(' ')[1]
    except Exception:
        bot.send_message(ms.chat.id, 'Invalid command')
        return
    draw.set(x, y)


@bot.message_handler(commands=['clr'])
def clrCm(ms):
    #/set x y
    try:
        cm = ms.text[5:]
        x = cm.split(' ')[0]
        y = cm.split(' ')[1]
    except Exception:
        bot.send_message(ms.chat.id, 'Invalid command')
        return
    draw.clear(x, y)


@bot.message_handler(commands=['color'])
def setCl(ms):
    # /color red
    try:
        draw.setColor(drawing.Colors[ms.text[7:]])
    except KeyError:
        bot.send_message(ms.chat.id, 'Invalid color')


bot.polling()
