# В качестве ответа добавьте ссылку на git-репозиторий.

# Приложение может иметь частичную реализацию, при это в каждом классе должны быть описаны:

# - поля (свойства) (с комментарием к каждому полю);
# - конструкторы;
# - методы (можно без реализации, но с подробным комментарием, что данный метод делает).


'''
Приложение "Календарь" при запуске показывает:
текущую дату, день недели,  время,
праздник (если есть)
напоминание (если есть).

Праздник имеет название, назначается на определенную дату.

Напоминание не только имеет название и дату (как праздник), но и задается на определенное время.

В приложении реализован следующий функционал:

- задать, отредактировать и удалить напоминание или праздник.
- просмотреть список всех напоминаний и праздников.


'''
from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
import locale


class Holiday:
    def __init__(self):


        self.all_holidays_dict = {"Праздники": []}

    def editHoliday(self):  # редактировать праздник
        global showMenu

        choice1 = input("Введите название праздника, который хотите редактировать:")

        choice2 = input("Какую информацию вы хотите редактировать?:"
                        "1. Дата_год\n"
                        "2. Дата_месяц\n"
                        "3. Дата_число\n")
        choice3 = input("Введите новое значение:")

        for hol in self.all_holidays_dict["Праздники"]:
            if choice1 == hol["Название праздника"]:
                hol[choice2] = choice3

        showMenu()

    def getAllHolidays(self):  # показать все праздники
        global showMenu
        if len(self.all_holidays_dict) != 0:
            print(self.all_holidays_dict)
        showMenu()

    def showTodayHoliday(self):  # показать праздник

        global showMenu

        today_date = str(date.today())
        today_year = today_date[:4]
        today_month = today_date[5:7]
        today_date = today_date[8:]

        for holi in self.all_holidays_dict["Праздники"]:
            if holi["Дата_год"] == today_year and holi["Дата_месяц"] == today_month and holi["Дата_число"] == today_date:
                print(holi)

        showMenu()

    def setNewHolidays(self):  # установить праздник
        global showMenu


        name_of_holidy = input("Введите название праздника\n")
        data_god = input("Введите год праздника в формате dddd, например, 2023\n")
        data_mes = input("Введите месяц праздника в формате от 01 до 12\n")
        data_chislo = input("Введите число праздника в формате от 01 до 31\n")

        new_holiday = {"Название праздника": name_of_holidy,
                       "Дата_год": data_god,
                       "Дата_месяц": data_mes,
                       "Дата_число": data_chislo
                       }

        self.all_holidays_dict["Праздники"].append(new_holiday)

        showMenu()

    def delHoliday(self):  # удалить праздник
        global showMenu
        choice = input("Введите название праздника, который хотите удалить")
        for hol in self.all_holidays_dict["Праздники"]:
            if choice == hol["Название праздника"]:
                self.all_holidays_dict["Праздники"].remove(hol)
        showMenu()


class Notification:
    def __init__(self):


        self.description_dict = {"Напоминания": []}


    def getDescription(self):  # получить весь список напоминаний
        global showMenu
        if len(self.description_dict) != 0:
            print(self.description_dict)
        showMenu()

    def showTodayNotification(self):  # получить напоминание за сегодня
        global showMenu

        today_date = str(date.today())
        today_year = today_date[:4]
        today_month = today_date[5:7]
        today_date = today_date[8:]

        for hol in self.description_dict["Напоминания"]:
            if hol["Дата_год"] == today_year and hol["Дата_месяц"] == today_month and hol["Дата_число"] == today_date:
                print(hol)

        showMenu()

    def setNotification(self):  # установить напоминание
        global showMenu

        name_of_not = input("Введите название напоминания\n")
        year_of_not = input("Введите год напоминания в формате dddd, например, 2023\n")
        month_of_not = input("Введите месяц напоминания в формате от 01 до 12\n")
        date_of_not = input("Введите число напоминания в формате от 01 до 31\n")
        hour_of_not = input("Введите час напоминания в формате от 00 до 23, например, если 9 утра, то нужно"
                            " ввести 09\n")
        min_of_not = input("Введите минуты напоминания в формате от 00 до 59\n")

        new_notification = {"Напоминание": name_of_not,
                            "Дата_год": year_of_not,
                            "Дата_месяц": month_of_not,
                            "Дата_число": date_of_not,
                            "Часы": hour_of_not,
                            "Минуты": min_of_not}

        self.description_dict["Напоминания"].append(new_notification)

        showMenu()

    def editNotification(self):  # редактировать напоминание
        global showMenu
        choice1 = input("Введите название напоминания, которое хотите редактировать:")

        choice2 = input("Какую информацию из напоминания вы хотите отредактировать? "
                        "1. Напоминание\n"
                        "2. Дата_год\n"
                        "3. Дата_месяц\n"
                        "4. Дата_число\n"
                        "5. Часы\n"
                        "6. Минуты\n"
                        )
        choice3 = input("Введите новое значение:")

        for notif in self.description_dict["Напоминания"]:
            if choice1 == notif["Напоминание"]:
                notif[choice2] = choice3

        showMenu()

    def delNotification(self):  # удалить напоминание
        global showMenu
        choice = input("Введите название напоминания, которое хотите удалить: ")
        for notif in self.description_dict["Напоминания"]:
            if choice == notif["Напоминание"]:
                self.description_dict["Напоминания"].remove(notif)
        showMenu()

    def getToDInformation(self):

        # В этом методе мы последовательно обращаемся к методам, отвечающим за отображение праздника сегодня и напоминания сегодня
        # выводим информацию об этом и дополнительно отобржаем текущие дату/время
hol = Holiday()
notif = Notification()



def showMenu():  # показать общее меню
    choice = input("Выберите необходимую цифру:\n"
                   "1. Показать праздник\n"
                   "2. Показать напоминание\n"
                   "3. Задать напоминание\n"
                   "4. Задать праздник\n"
                   "5. Отредактировать напоминание\n"
                   "6. Отредактировать праздник\n"
                   "7. Удалить напоминание\n"
                   "8. Удалить праздник\n"
                   "9. Просмотреть список всех напоминаний\n"
                   "10. Просмотреть список всех праздников\n"
                   "11. Информация о сегодняшнем дне\n"
                   )
    if choice == "1":
        hol.showTodayHoliday()
    if choice == "2":
        notif.showTodayNotification()
    if choice == "3":
        notif.setNotification()
    if choice == "4":
        hol.setNewHolidays()
    if choice == "5":
        notif.editNotification()
    if choice == "6":
        hol.editHoliday()
    if choice == "7":
        notif.delNotification()
    if choice == "8":
        hol.delHoliday()
    if choice == "9":
        notif.getDescription()
    if choice == "10":
        hol.getAllHolidays()
    if choice == "11":
        notif.getToDInformation()

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
datetime_now = datetime.now()
print("Сегодня:", datetime_now.strftime('%A %d, %B %Y'))
print(datetime_now.strftime('%H:%M:%S'))
showMenu()

