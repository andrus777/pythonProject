# ssp_game - stone, scissors, paper
# Игра камень, ножницы, бумага

import tkinter as tk # подключаем библиотеку с графическим интерфейсом
import random

selection_items = ['камень', 'ножницы', 'бумага'] # список допустимых значений для выбора
score = {'Бот':0, 'Игрок':0} # в этом словаре будем вести счет


def new_game(): # если нужнобудет обнулить счет и начать игру заново
    play()

def quit_game(): # если надоело и нужно завершить приложение
    window.quit()

# создаем окно
window = tk.Tk()
# создаем виджеты надписей и кнопок
score_current = tk.Label(window, text=f'Текущий счет: {score}'  , font=("Arial", 14))

select_bot = tk.Label(window, text="", font=("Arial", 14))
select_user = tk.Label(window, text="Выберите жест", font=("Arial", 14))
result_win = tk.Label(window, text="", font=("Arial", 14))

button_stone = tk.Button(window, text="Камень", width=10, height=2, command=lambda: user_select("камень", select_user))
button_scissors = tk.Button(window, text="Ножницы", width=10, height=2, command=lambda: user_select("ножницы", select_user))
button_paper = tk.Button(window, text="Бумага", width=10, height=2, command=lambda: user_select("бумага", select_user))

button_new = tk.Button(window, text="Заново", width=10, height=2, command=new_game)
button_quit = tk.Button(window, text="Хватит", width=10, height=2, command=quit_game)


def init_game(): # функция инициализирует начальные значения игры и отрисовывает виджеты
    score.update({'Бот': 0, 'Игрок': 0})
    score_current['text'] = f'Текущий счет: {score}'
    window.title('Камень, Ножницы, Бумага')
    window.geometry("380x350")
    window.resizable(False, False)

    select_user['text']="Выберите жест"
    select_bot['text']=""
    result_win['text'] = ""

    score_current.pack(anchor="n")
    select_bot.place(x=120, y=60)
    result_win.place(x=120, y=90)
    select_user.place(x=120, y=140)

    button_stone.place(x=50, y=200)
    button_scissors.place(x=150, y=200)
    button_paper.place(x=250, y=200)

    button_new.place(x=100, y=300)
    button_quit.place(x=200, y=300)

def bot_select(): # в этой функции бот выбирает жест
    result = selection_items[random.randint(0,2)]
    select_bot['text'] = f'Бот выбрал: {result}'
    return result

def user_select(item, label): # в этой функции отображается выбор игрока, запрашивается выбор бота и вызывается функция проверки победителя
    label['text'] = f'Вы выбрали: {item}'
    bot_item = bot_select()
    win_result = who_is_win(item, bot_item)
    result_win['text'] = win_result
    score_current['text'] = current_score


def who_is_win(user_sel, bot_sel): # в этой функции происходит проверка победителя и начисление очков за выигрыш победителю
    global current_score
    if user_sel == bot_sel:
        return 'Ничья!'
    elif ((user_sel == 'камень' and bot_sel == 'ножницы') or
          (user_sel == 'ножницы' and bot_sel == 'бумага') or
          (user_sel == 'бумага' and bot_sel == 'камень')):
        score.update({'Игрок': score.get('Игрок') + 1})
        current_score = f'Текущий счет: {score}'
        return 'Победил Игрок!!!'
    elif ((user_sel == 'камень' and bot_sel == 'бумага') or
          (user_sel == 'ножницы' and bot_sel == 'камень') or
          (user_sel == 'бумага' and bot_sel == 'ножницы')):
        score.update({'Бот': score.get('Бот') + 1})
        current_score = f'Текущий счет: {score}'
        return 'Победил Бот!'

def play(): # запуск игрового процесса сначала
    init_game()
    window.mainloop()

play() # Погнали!





