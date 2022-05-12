









from re import T
import string
from pyrogram import *
from pyrogram.errors import *
from time import sleep
import colorama
from colorama import *
import textwrap
import pickle
import random
import configparser
from slova import *




colorama.init()
#print(Fore.GREEN + Style.BRIGHT + ">>> Руководство по авторизации в скрипте @tgscriptss")
print(Fore.BLUE + Style.BRIGHT +'''
█░█ █▀ █▀▀ █▀█  █▄▄ █▀█ ▀█▀
█▄█ ▄█ ██▄ █▀▄  █▄█ █▄█ ░█░
''')
print(Fore.BLUE + Style.BRIGHT +'''
█▄▄ █▄█   █░█ █▀▀ █▀█ █ █▀▀ █▀█ █▄░█ █▀ █▀█ █▀█
█▄█ ░█░   ▀▄▀ ██▄ █▀▄ █ █▄▄ █▄█ █░▀█ ▄█ █▄█ ▀▀█
''')
debug_mode = True
if debug_mode:
    print(Fore.BLUE + Style.BRIGHT +'''
    ███╗░░░███╗██████╗░░░░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
    ████╗░████║██╔══██╗░░░██║░░░░░██╔══██╗██╔══██╗██║░░██║
    ██╔████╔██║██████╔╝░░░██║░░░░░███████║██║░░╚═╝███████║
    ██║╚██╔╝██║██╔══██╗░░░██║░░░░░██╔══██║██║░░██╗██╔══██║
    ██║░╚═╝░██║██║░░██║██╗███████╗██║░░██║╚█████╔╝██║░░██║
    ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
    ''')
config = configparser.ConfigParser()
config.read('settings.ini')
if "N" in config['account']['api_id'] or "N" in config['account']['api_hash']:
    config['account']['api_id'] = input("Введите api_id полученный с https://my.telegram.org \n> ").replace(' ', '')
    config['account']['api_hash'] = input("Введите api_hash полученный с https://my.telegram.org \n> ").replace(' ', '')
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)

api_id=config['account']['api_id']
api_hash=config['account']['api_hash']




print(Fore.GREEN + Style.BRIGHT + "Готово! Скрипт запущен.")



app = Client("my_account", api_id=api_id, api_hash=api_hash)










@app.on_message(filters.command("type",prefixes=".") & filters.me)
def type(_,msg):
    if debug_mode == False:
        app.send_message(msg.chat.id, f'автор: https://vm.tiktok.com/ZMLsfDqoa/')
    or_text = msg.text.split(".type ",maxsplit=1)[1]
    text = or_text
    tbp = ""
    typing_symbol = "!"
    while tbp != or_text:
            try:
                msg.edit(tbp + f"        {typing_symbol}")
            except:
                pass
            try:
                typing_symbol = text[1]
            except:
                typing_symbol = text[0]
            if typing_symbol == " ":
                typing_symbol = "!"
            sleep(0.05)
            tbp += text[0]
            text = text[1:]
            msg.edit(tbp)
            sleep(0.05)
        
    


@app.on_message(filters.command("ghoul", prefixes=".") & filters.me)
def lol(app, message):
    if debug_mode == False:
        app.send_message(message.chat.id, f'автор: https://vm.tiktok.com/ZMLsfDqoa/')
    app.send_message(message.chat.id,f'<b>Ты гуль?</b>')
    sleep(2)
    app.send_message(message.chat.id,f'<i>Я тоже</i>')
    sleep(5)
    i = 1000
    while i > 0:
        try:
            app.send_message(message.chat.id, f'{i} - 7 = {i-7}')
        except FloodWait as e:
            sleep(e.x)

        i -= 7
        sleep(0)





@app.on_message(filters.command("spam",prefixes=".") & filters.me)
def type(_, msg,):
    if debug_mode == False:
        app.send_message(msg.chat.id, f'автор: https://vm.tiktok.com/ZMLsfDqoa/')
    msgg = msg.text.split(" ")
    count = int(msgg[1])
    msgg.pop(0)
    msgg.pop(0)
    to_send = ""
    for i in range(len(msgg)):
        to_send += " " +msgg[i]
    for i in range(count):
       app.send_message(msg.chat.id,to_send)





@app.on_message(filters.command("dr", prefixes=".") & filters.me)
def lol(app, msg):
    dr(app, msg)





@app.on_message(filters.command("showdown", prefixes=".") & filters.me)
def lol(app, msg):
    showdown(app, msg,debug_mode)





app.run()
