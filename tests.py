from datetime import datetime

from task import Task
from team import Team


def test_task():
    t = Task(name="Починить всё", desc="Подробное описание таски", due='14.08.15', stat='backlog',
             exec=Team.Employee("Кар-Карыч"))
    assert t.name == 'Починить всё'
    assert t.desc == "Подробное описание таски"
    assert t.stat == 'backlog'
    assert t.due == datetime.strptime('14.08.15', '%d.%m.%y')
    assert t.exec.name == "Кар-Карыч"


def test_team():
    for _ in range(10):
        bar = Team.Employee("Бараш")
        los = Team.Employee("Лосяш")
        kro = Team.Employee("Крош")
        my_team = Team("Смешарики", "Лучшая команда на свете", [bar, los, kro])
        assert my_team.name == "Смешарики"
        assert my_team.desc == "Лучшая команда на свете"
        assert len(my_team.lst) == 3
        assert len(my_team.task_mgr.task_list) == 0
        test_employee = Team.Employee('Test Test')
        my_team.add_employee(test_employee)
        assert len(my_team.lst) == 4
        my_team.remove_employee(test_employee)
        assert len(my_team.lst) == 3
        t = Task(name="Починить всё", desc="Подробное описание таски", due='14.08.15', stat='backlog',
                 exec=Team.Employee("Кар-Карыч"))
        my_team.new_task(t)
        tm = my_team.get_task_mgr()
        assert len(tm.task_list) == 1
        my_team.del_task(t)
        assert len(tm.task_list) == 0
        tm.show_all()
        tm.show_due_today()
        for statusik in ('backlog', 'in review', 'in progress', 'done'):
            tm.show_by_status(statusik)