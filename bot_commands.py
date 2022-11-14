from webbrowser import open_new
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy_log import *

operation = 0
operands = []
def start_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Привет, {update.effective_user.first_name}! Это калькулятор рациональных и комплексных чисел!')
    res_str = ""
    res_str += "ПРОГРАММА КАЛЬКУЛЯТОРA, /program\n"
    res_str += "ЗАВЕРШИТЬ РАБОТУ КАЛЬКУЛЯТОРA, /cancel\n"
    update.message.reply_text(res_str)

def program_command(update: Update, context: CallbackContext):
    
    global operation 
    operation = 0

    res_str = ""
    res_str += "Выберите действие и введите операнды:\n"
    res_str += "Сложение /sum\n"
    res_str += "Вычитание /sub\n"
    res_str += "Умножение /mul\n"
    res_str += "Деление /div\n"
    res_str += "Посмотреть log /log\n"
    res_str += "Завершить работу калькутлятора /cancel\n"
    res_str += "Комплексное число следует записывать через пробел Real Imag, перед вводом второго числа нажмите Enter" 
    update.message.reply_text(res_str)


def sum_command(update: Update, context: CallbackContext):
    global operation
    operation = 1

def sub_command(update: Update, context: CallbackContext):
    global operation
    operation = 2

def mul_command(update: Update, context: CallbackContext):
    global operation
    operation = 3

def div_command(update: Update, context: CallbackContext):
    global operation
    operation = 4
  

def analize_command(update: Update, context: CallbackContext):
    global operation, operands
    res_str = ""

    if operation:
        if len(operands)<2:
            msg = update.message.text
            
            if " " in msg and msg.split(" ")[0].isdigit() and msg.split(" ")[1].isdigit():
                operands.append(complex(float(msg.split(" ")[0]), float(msg.split(" ")[1])))
                update.message.reply_text(f"Комплексное число {operands[-1]}")
            elif msg.isdigit():
                operands.append(float(msg))
            else:
                update.message.reply_text("Введённые данные не являются числом. Повторите ввод")
        if len(operands) == 2:
            match operation:
                case 1:
                    res_str = f"{operands[0]} + {operands[1]} = {operands[0]+operands[1]}"
                case 2:
                    res_str = f"{operands[0]} - {operands[1]} = {operands[0]-operands[1]}"
                case 3:
                    res_str = f"{operands[0]} * {operands[1]} = {operands[0]*operands[1]}"
                case 4:
                    res_str = f"{operands[0]} / {operands[1]} = {operands[0]/operands[1]}"
        
                        
            
            log_command(update,context,res_str)
            res_str += "\n\nЕщё пример? /program, завершить работу /cancel"
            update.message.reply_text(res_str)
            operands=[]
            operation=0

def read_data(update: Update, context: CallbackContext):
    res_str = ""
    with open('C:\\Users\\vasil\\Documents\\репозитории\\python_10_seminar_dz\\db.csv', 'r', encoding='UTF-8') as f:
        data = f.read()
        update.message.reply_text(f"{data}")
        res_str += "\n\nЕщё пример? /program, завершить работу /cancel"
        update.message.reply_text(res_str)

def cancel_command(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться') 
