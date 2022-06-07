import os
import smtplib
from dotenv import load_dotenv

# Сохраняем все изменяемые данные в переменные
web_adrress = "https://dvmn.org/referrals/a0CrgaQsT8dZkyBadQ1xRjQu8NBgs4CEpCtysnMT/"
friend_name = "Саша"
my_name = "Ашот"
mail_from = "ashotabazyan@yandex.ru"
mail_to = "a.abazyan@bk.ru"
letter_subject = "Приглашение!"
content_type = '''text/plain; charset="UTF-8"'''
letter = f"""\
From: {mail_from}
To: {mail_to}
Subject: {letter_subject}
Content-Type: {content_type}

Привет, {friend_name}! {my_name} приглашает тебя на сайт {web_adrress}!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {web_adrress}  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

# Устанавливаем кодировку письма для корректного отображения
letter = letter.encode("UTF-8")

# Подгружаем переменные окруженя
load_dotenv()
my_secret_login = os.environ['YANDEX_LOGIN']
my_secret_password = os.environ['YANDEX_PASSWORD']

# Отправляем письмо и закрываем сессию
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(my_secret_login, my_secret_password)
server.sendmail(mail_from, mail_to, letter)
server.quit()