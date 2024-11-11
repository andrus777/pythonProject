def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    # Проверка на корректность e-mail отправителя и получателя
    if not is_correct_mail(recipient) or not is_correct_mail(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    # Проверка на отправку самому себе
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')

    # Проверка на отправителя по умолчанию
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


def is_correct_mail(mail):
    result = True
    if not('@' in mail):
        result = False
    if not (mail.endswith('.com') or mail.endswith('.ru') or mail.endswith('.net')):
        result = False
    return result


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')