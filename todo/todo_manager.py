from collections import UserDict
from datetime import datetime
import json


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
        self.tags = []
        self.tasks = []
        
    def add_task(self, task, date, status, tags):
        self.tasks.append({'task': task, 'date': date, 'status': status, 'tags': tags})
        print(f'You had added "{task}" for your to do list.')

# adding tags while creating ToDoRecord class instance
    def add_tags(self, tag):
        if not isinstance(tag, Fields):
            tag = Fields(tag)
        self.tags.append(tag)

# adding tags to existing task
    def add_tags_to_existing_task(self, search_word, tags):
        if not search_word:
            print("Please enter word from task description")
        elif not tags:
            print("Please enter at least one tag")
        else:
            for i in self.tasks:
                if search_word.lower() in i['task'].lower():
                    i['tags'].append(tags)
                    return i
                
# possibility of editing the tag if the user made a mistake
    def edit_tags(self, wrong_tag, right_tag):
        if not wrong_tag:
            print("Please enter tag to edit")
        elif not right_tag:
            print("Please enter a new tag")
        else:
            for i in self.tasks:
                if wrong_tag in i['tags']:
                    i['tags'].remove(wrong_tag)
                    i['tags'].append(right_tag)
                    return i
            
# removing unnecessary tag
    def delete_tags(todo_list, tag_to_delete):
        if not tag_to_delete:
            print("Please enter tag to delete")
        else:
            for i in todo_list:
                if tag_to_delete in i['tags']:
                    i['tags'].remove(tag_to_delete)
                    return i

# searcing by one or two literal
    def search_by_part_word(self, part_word):
        searching_tasks = []
        for task in self.tasks:
            if part_word.lower() in task["task"].lower():
                searching_tasks.append(task)

        self._search_results(searching_tasks, "Name", part_word)

    # searcing by date
    def search_by_date(self, date):
        pass

    # searcing by status
    def search_by_status(self, status):
        pass


class ToDoBook(UserDict):
    def add_to_do_record(self, record: ToDoRecord):
        self.data[record.task.value] = record
        return self.data


class ToDoList_Save(ToDoRecord):
    def save_list(self):
        with open(self.file, "w ", encoding="utf-8") as f:
            json.dump((self.date, self.task), f)

        
