from collections import UserDict
from datetime import datetime

class Fields:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)




class ToDoRecord:

    def __init__(self, task, date, status=None):
        self.task = task
        self.date = date
        self.status = status # ???
        self.tasks = []

    def add_task(self, task, date, status):
        self.tasks.append({'task': task, 'date': date, 'status': status})
        print(f'You had added "{task}" for your to do list.')

# searcing by one or two literal
    def search_by_part_word(self, part_word):
        searching_tasks = []
        for task in self.tasks:
            if part_word.lower() in task['task'].lower():
                searching_tasks.append(task)

        self._search_results(searching_tasks, 'Name', part_word)

#searcing by date
    def search_by_date(self, date):
        pass
#searcing by status
    def search_by_status(self, status):
        pass
        

class ToDoBook(UserDict):
    def add_to_do_record(self, record:ToDoRecord):
        self.data[record.task.value] = record
