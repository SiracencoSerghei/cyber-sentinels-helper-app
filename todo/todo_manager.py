from collections import UserDict
from datetime import datetime
import json
from contacts.classes.Field import Field
from contacts.classes.Birthday import Birthday


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
        if not isinstance(tag, Field):
            tag = Field(tag)
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
    def delete_tags(self, tag_to_delete):
        if not tag_to_delete:
            print("Please enter tag to delete")
        else:
            for i in self.tasks:
                if tag_to_delete in i['tags']:
                    i['tags'].remove(tag_to_delete)
                    return i
                
# searching by tag
    def search_by_tag(self, tag_to_find):
        search_result = []
        if not tag_to_find:
            print("Please enter tag to find")
        else:
            for i in self.tasks:
                if tag_to_find in i['tags']:
                    search_result.append(i)
        if not search_result:
            return f"Sorry, task with that tag is absent in your To Do List"
        else:
            return search_result

# searching by one or two literal
    def search_by_part_word(self, part_word):
        searching_tasks = []
        for task in self.tasks:
            if part_word.lower() in task["task"].lower():
                searching_tasks.append(task)

        self._search_results(searching_tasks, "Name", part_word)

    # searcing by date
    def search_by_date(self, date):
        searching_tasks = []
        for task in self.tasks:
            if task['date'] in date:
                searching_tasks.append(task)

        self._search_results(searching_tasks, "Date", date)

        # It can also work by this
        #searching_tasks = [task for task in self.tasks if task['date'] == date]
        #self._search_results(searching_tasks, 'Date', date)


    # searcing by status
    def search_by_status(self, status):
        searching_tasks = []
        for task in self.tasks:
            if task['status'].lower() in status.lower():
                searching_tasks.append(task)

        self._search_results(searching_tasks, "Status", status)

        #It can also work by this
        #esarching_tasks = [task for task in self.tasks if task['status'].lower() == status.lower()]
        #self._search_results(searching_tasks, 'Status', status)

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

# changing task date
    def edit_date(self, new_date):
        if not isinstance(new_date, Birthday):
            new_date = Birthday(new_date)
        self.date = new_date

# changing task status
    def edit_status(self, new_status):
        self.status = new_status
        


class ToDoBook(UserDict):
    def add_to_do_record(self, record: ToDoRecord):
        self.data[record.task.value] = record   
        return self.data
    
    # I think "self.data[record.task] = record" will be correct
    
    def search_task(self):
        search_info = input().lower()
        for task in self.data.values():
            search_by_task = task.task.lower().find(search_info)
            search_by_date = str(task.date).find(search_info)
            search_by_status = task.status.lower().find(search_info)
            search_by_tags = str([tag.value.lower() for tag in task.tags]).find(search_info)
            if search_by_task > -1 or search_by_date > -1 or search_by_status > -1 or search_by_tags > -1:
                print(task.task) 

    #we can change return info

    def delete_task(self):
        delete_info = input().lower()
        result_list = []
        for task in self.data.values():
            search_by_task = task.task.lower().find(delete_info)
            search_by_date = str(task.date).find(delete_info)
            search_by_status = task.status.lower().find(delete_info)
            search_by_tags = str([tag.value.lower() for tag in task.tags]).find(delete_info)
            if search_by_task > -1 or search_by_date > -1 or search_by_status > -1 or search_by_tags > -1:
                result_list.append(task)
        dict_with_number = dict(zip([i+1 for i in range(len(result_list))], [i.task for i in result_list]))
        print(dict_with_number)
        print('Please choose task number?')
        delete_i = int(input())
        for key, value in dict_with_number.items():
            if key == delete_i:
                del self.data[value]


class ToDoList_Save(ToDoRecord):
    def save_list(self):
        with open(self.file, "w ", encoding="utf-8") as f:
            json.dump((self.date, self.task), f)

        
