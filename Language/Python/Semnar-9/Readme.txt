Сночало настраиваеться глобальные переменые в поиске набрать Изменения системных переменых -> параметры среды -> системные переменные
-> Path -> добовляем -> C:\Program Files\Windows\Apps\Python\Python.3.10.\Scripts\ -> C:\Program Files\Windows\Apps\Python\
Python.3.10.\Scripts\ -> ok 
                                ПОСЛЕ ЭТОГО:
Создаем папку в даном случае Lession-9 Open integrated Terminal (Открытый интегрированный терминал) прописываем И пропишем следущую
команду (python -m venv venv). Активируем вертуальное окружения через терминал ((cd.\venv\) если будет ошибка можно в папке venv
Open integrated Terminal (Открытый интегрированный терминал)) -> ((cd.\Scripts\) если будет ошибка можно в папке Scripts Open
integrated Terminal (Открытый интегрированный терминал) -> ((.\activate) (Instal Extension) в первый раз выходит такое сообшениу
нажимаем (Instal) -> появиться вот что ((venv) PS C:\Users\User\Desktop\study\Language\Python\Semnar-9\venv\Scripts>) а, было так
(PS C:\Users\User\Desktop\study\Language\Python\Semnar-9\venv\Scripts>) это имя папки с нашим виртуальным окружением что бы запускать
скрепты через терминал мы наработались и не хотим больше работать есть команда (exit) или просто закрыть.

                                ИЛИ ТАК:

Создаем папку в даном случае Lession-9 Open integrated Terminal (Открытый интегрированный терминал) переходим Галочка возле + (нижний
правый угол) -> Разделить терминал -> Command Prompt -> cd.\venv\ -> cd.\Scripts -> activate -> появиться вот что ((venv)
C:\Users\User\Desktop\study\Language\Python\Semnar-9\venv\Scripts>) а, было так (C:\Users\User\Desktop\study\Language\Python\Secriots
venv\Scripts>activate)


Виртуалку поставили попробуем устоновить библеотеку набераем команду pip install isOdd открывае папку venv и Lid смотрим что isOdd
появился -> создали папку main.py -> этой командой вернулся cd.. в папку venv> и еше раз cd.. оказаться в папки Semnar-9> ->
python main.py (этой командой запускаем скрипт через терминал)


                        














 folder - папка где будет хрониться наши скаченые библеотеки. Надо опять открыть Open integrated
Terminal только из папки .folder в терминаль должна пояаиться следушее (PS C:\Users\User\Desktop\study\Language\Python\Lession-5\pipPy\.folder>)
.folder можно называть как мне нравиться необязательно делаеться это при следушей команде pip install isOdd только для этой
библеотеки. Далее ее можн проверит есть демо версия (Usage). Качаем библеотеку progress (показывает процес скачивания файла или чтения)
и добоаляем. Есть библеотеки которые дбовляют смайлики это (emoji).Мы хотим нарисовать какой небудь график матиматической функции
matplotlib для рисования функции он супер избыточный но полезен для аналитики даных (библеотека очень сложная для изучения ее она
находиться Homepage -> examples (документация с примерами) для димонстрации бирем любую вставляе код и наблюдаем какойто график).