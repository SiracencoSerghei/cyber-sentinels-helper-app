from collections import UserDict
from datetime import datetime
import json
from contacts.classes.Field import Field
from contacts.classes.Birthday import Birthday


class ToDoRecord:
    def __init__(self, task, begin, end, status=None):
        self.task = task
        self.begin = begin
        self.end = end
        self.status = status
        self.tags = []

    # {'task def add_task(self, task, date, status, tags):
    #     #     self.tasks.append(': task, 'date': date, 'status': status, 'tags': tags})
    #     print(f'You had added "{task}" for your to do list.')

    # adding tags while creating ToDoRecord class instance
    def add_tags(self, tag):
        if not isinstance(tag, Field):
            tag = Field(tag)
        self.tags.append(tag)

    # possibility of editing the tag if the user made a mistake
    def edit_tags(self, wrong_tag, right_tag):
        if not wrong_tag:
            print("Please enter tag to edit")
        elif not right_tag:
            print("Please enter a new tag")
        else:
            for i, p in enumerate(self.tags):
                if p.value == wrong_tag:
                    self.tags[i] = Field(right_tag)

# removing unnecessary tag
    def delete_tags(self, tag_to_delete):
        if not tag_to_delete:
            print("Please enter tag to delete")
        else:
            for i, p in enumerate(self.tags):
                if p.value == tag_to_delete:
                    self.tags.remove(p)

    # searching by tag
    #     def search_by_tag(self, tag_to_find):
    #         search_result = []
    #         if not tag_to_find:
    #             print("Please enter tag to find")
    #         else:
    #             for i in self.tasks:
    #                 if tag_to_find in i['tags']:
    #                     search_result.append(i)
    #         if not search_result:
    #             return f"Sorry, task with that tag is absent in your To Do List"
    #         else:
    #             return search_result

    # searching by one or two literal
    def search_by_part_word(self, part_word):
        searching_tasks = []
        for task in self.tasks:
            if part_word.lower() in task["task"].lower():
                searching_tasks.append(task)

        self._search_results(searching_tasks, "Name", part_word)

    # searching by date
    def search_by_date(self, date):
        searching_tasks = []
        for task in self.tasks:
            if task['date'] in date:
                searching_tasks.append(task)

        self._search_results(searching_tasks, "Date", date)

        # It can also work by this
        # searching_tasks = [task for task in self.tasks if task['date'] == date]
        # self._search_results(searching_tasks, 'Date', date)

    # searching by status
    def search_by_status(self, status):
        searching_tasks = []
        for task in self.tasks:
            if task['status'].lower() in status.lower():
                searching_tasks.append(task)

        self._search_results(searching_tasks, "Status", status)

        # It can also work by this
        # esarching_tasks = [task for task in self.tasks if task['status'].lower() == status.lower()]
        # self._search_results(searching_tasks, 'Status', status)

    # completely change the task
    def change_task(self, new_task):
        self.task = new_task

    # partially modify task
    def edit_task(self, wrong_part, new_part):
        part_of_task = self.task.find(wrong_part)
        if part_of_task == -1:
            print(f'Task has no letters {wrong_part}. Please try again.')
        else:
            new_task = self.task.replace(wrong_part, new_part)
            self.task = new_task

    # changing begin date
    def edit_begin_date(self, new_date):
        if not isinstance(new_date, Birthday):
            new_date = Birthday(new_date)
        self.begin = new_date

    # changing end date
    def edit_end_date(self, new_date):
        if not isinstance(new_date, Birthday):
            new_date = Birthday(new_date)
        self.end = new_date

    # changing task status
    def edit_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"{self.task}: start - {self.begin}, end - {self.end}, current status is {self.status}, tags: {', '.join(p.value for p in self.tags)}"


class ToDoBook(UserDict):
    def add_to_do_record(self, record: ToDoRecord):
        self.data[record.task] = record
        return self.data

    # I think "self.data[record.task] = record" will be correct

    def search_task(self):
        search_info = input().lower()
        for task in self.data.values():
            search_by_task = task.task.lower().find(search_info)
            search_by_date1 = str(task.begin).find(search_info)
            search_by_date2 = str(task.end).find(search_info)
            search_by_status = task.status.lower().find(search_info)
            search_by_tags = str([tag.value.lower() for tag in task.tags]).find(search_info)
            if search_by_task > -1 or search_by_date1 > -1 or search_by_date2 > -1 or search_by_status > -1 or search_by_tags > -1:
                print(task.task)

    # we can change return info

    def delete_task(self):
        delete_info = input().lower()
        result_list = []
        for task in self.data.values():
            search_by_task = task.task.lower().find(delete_info)
            search_by_date1 = str(task.begin).find(delete_info)
            search_by_date2 = str(task.end).find(delete_info)
            search_by_status = task.status.lower().find(delete_info)
            search_by_tags = str([tag.value.lower() for tag in task.tags]).find(delete_info)
            if search_by_task > -1 or search_by_date1 > -1 or search_by_date2 > -1 or search_by_status > -1 or search_by_tags > -1:
                result_list.append(task)
        dict_with_number = dict(zip([i + 1 for i in range(len(result_list))], [i.task for i in result_list]))
        print(dict_with_number)
        print('Please choose task number?')
        delete_i = int(input())
        for key, value in dict_with_number.items():
            if key == delete_i:
                del self.data[value]


class ToDoListSave(ToDoRecord):
    def save_list(self):
        with open(self.file, "w ", encoding="utf-8") as f:
            json.dump((self.date, self.task), f)


if __name__ == '__main__':
    to_do_list = ToDoBook()

    task1 = ToDoRecord("Buy some food", "13.12.2023", "17.12.2023", "Done")
    task1.add_tags("food")
    task1.add_tags("store")
    to_do_list.add_to_do_record(task1)

    task2 = ToDoRecord("Buy shampoo", "16.12.2023", "20.12.2023", "In progress")
    task2.add_tags("beauty")
    task2.add_tags("store")
    to_do_list.add_to_do_record(task2)

    task3 = ToDoRecord("Get my nails done", "17.12.2023", "28.12.2023", "In progress")
    task3.add_tags("beauty")
    to_do_list.add_to_do_record(task3)

    task3.edit_tags('beauty', 'salon')
    task2.delete_tags('beauty')
    for name, record in to_do_list.data.items():
        print(record)
