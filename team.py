from datetime import datetime

from task import Task


class Team:
    class Employee:
        def __init__(self, name):
            self.set_name(name)

        def set_name(self, value):
            self.name = value

        def get_name(self):
            return self.name

    class TaskManager:
        def __init__(self, task_list=None):
            if task_list is None:
                task_list = []
            self.task_list = task_list

        def new_task(self, *args, **kwargs):
            if isinstance(args[0], Task):
                t = args[0]
            else:
                t = Task(*args, **kwargs)
            self.task_list.append(t)

        def del_task(self, t):
            self.task_list.remove(t)

        def show_all(self):
            for x in self.task_list:
                print(x)

        def show_due_today(self):
            for x in self.task_list:
                if x.due.date() <= datetime.today().date():
                    print(x)

        def show_by_status(self, status):
            for x in self.task_list:
                if x.stat == status:
                    print(x)

    def __init__(self, name, desc="", lst=[]):
        self.set_name(name)
        self.set_desc(desc)
        self.set_lst(lst)
        self.task_mgr = Team.TaskManager()

    def get_name(self):
        return self.name

    def get_desc(self):
        return self.desc

    def get_lst(self):
        return self.lst

    def get_name(self):
        return self.name

    def get_task_mgr(self):
        return self.task_mgr

    def set_name(self, value):
        self.name = value

    def set_desc(self, value):
        self.desc = value

    def set_lst(self, lst):
        self.lst = []
        for x in lst:
            if isinstance(x, Team.Employee):
                self.add_employee(x)
            else:
                raise ValueError("Вы пытаетесь создать команду, где есть НЕ сотрудник")

    def add_employee(self, employee):
        self.lst.append(employee)

    def remove_employee(self, employee):
        self.lst.remove(employee)

    def new_task(self, *args, **kwargs):
        tm = self.get_task_mgr()
        tm.new_task(*args, **kwargs)

    def del_task(self, id):
        tm = self.get_task_mgr()
        tm.del_task(id)
