from datetime import date
from datetime import datetime


class Task:
    total_number = 0

    def __init__(self, name, desc="", stat="backlog", due=datetime.today(), exec=None):
        self.set_name(name)
        self.set_desc(desc)
        self.set_stat(stat)
        self.set_due(due)
        self.set_exec(exec)
        self.id = Task.total_number
        Task.total_number += 1

    def get_name(self):
        return self.name

    def get_desc(self):
        return self.desc

    def get_stat(self):
        return self.stat

    def get_due(self):
        return self.due

    def get_exec(self):
        return self.exec

    def set_name(self, value):
        self.name = value

    def set_desc(self, value):
        self.desc = value

    def set_stat(self, value):
        value = value.lower()
        if value in {'backlog', 'in progress', 'in review', 'done'}:
            self.stat = value
        else:
            print("Ошибка! Такого статуса не существует(")
            raise ValueError

    def set_due(self, value):
        if isinstance(value, datetime) or isinstance(value, date):
            self.due = value
        else:
            self.due = datetime.strptime(value, '%d.%m.%y')

    def set_exec(self, value):
        self.exec = value

    def __str__(self):
        if self.desc:
            s = f"Задача:\n{self.name}\n\nОписание:\n{self.desc}\n_______________________________________"
        else:
            s = f"Задача:\n{self.name}\n_______________________________________"
        return s
