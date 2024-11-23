import tkinter as tk
import random

from select import select

select_values = ['камень', 'ножницы', 'бумага']
score_table = {'Бот':0, 'Вы':0}

def get_user_values():
    user_val = None
    while 1:
        user_val = input(f'Введите одно из значений {select_values}:')
        if user_val.lower() in select_values:
            return user_val
        else:
            print('Введенное значение не корректно!')

def get_user_value_gi():
    val = button_add
    user_sel_val.insert(0, val)


def get_bot_values():
    random_val = random.randint(0, 2)
    return select_values[random_val]

def how_is_win(user_case, bot_case):
    result = None
    if user_case == bot_case:
        result = 'Ничья'
    elif (user_case == 'камень' and bot_case == 'ножницы') or (user_case == 'ножницы' and bot_case == 'бумага') or (user_case == 'бумага' and bot_case == 'камень'):
        result = 'Вы победили!'
        new_value = score_table.get('Вы') + 1
        score_table.update({'Вы': new_value})
    elif (user_case == 'бумага' and bot_case == 'ножницы') or (user_case == 'ножницы' and bot_case == 'камень') or (user_case == 'камень' and bot_case == 'бумага'):
        result = 'Вы проиграли!'
        new_value = score_table.get('Бот') + 1
        score_table.update({'Бот': new_value})
    return result

def play():
    result_win = None
    while 1:
        print(score_table)
        user_case_val = get_user_values()
        print(f'Вы ввели {user_case_val}')
        bot_case_val = get_bot_values()
        print(f'Бот выбрал {bot_case_val}')
        result_win = how_is_win(user_case_val, bot_case_val)
        print(result_win)
        print(score_table)
        game_over=''
        while game_over !='ДА' and game_over !='НЕТ':
            game_over = input('Для повторения введите Да, для окончания введите Нет:').upper()

        if game_over =='НЕТ':
            break

# play()

window = tk.Tk()
window.title('Камень ножницы бумага')
window.geometry("350x350")
window.resizable(False, False)

button_add = tk.Button(window, text="Камень", width=6, height=2, command=get_user_value_gi)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text="Ножницы", width=6, height=2, command=get_user_value_gi)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text="Бумага", width=6, height=2, command=get_user_value_gi)
button_mul.place(x=200, y=200)

user_sel_val = tk.Entry(window, width=28)
user_sel_val.place(x=100, y=75)

bot_sel_val = tk.Entry(window, width=28)
bot_sel_val.place(x=100, y=150)

result_entry = tk.Entry(window, width=28)
result_entry.place(x=100, y=300)

user_sel = tk.Label(window, text="Введите первое число:")
user_sel.place(x=100, y=50)

bot_sel = tk.Label(window, text="Введите второе число:")
bot_sel.place(x=100, y=125)

answer = tk.Label(window, text="Ответ:")
answer.place(x=100, y=275)


window.mainloop()