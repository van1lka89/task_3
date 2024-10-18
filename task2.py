
def send_email(message,recipient,sender="university.help@gmail.com"):
    proverka = (".ru")
    proverka_2 = (".com")
    if ("@" not in recipient) or ("@" not in sender) or((sender.endswith((".com",".ru"))==False) or (recipient.endswith((".com",".ru"))==False)):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
        return True
    if sender==recipient:
        print( "Нельзя отправить письмо самому себе!")
        return True
    if sender=="university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender ,"на адрес",recipient)
        return True
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender ,"на адрес",recipient)
        return True
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

