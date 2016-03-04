class TaskList(object):
    def __init__(self):
        self.task_list = []

    def get_task_list(self):
        return self.task_list

    def add_tasks(self, *tasks):
        self.task_list += [task for task in tasks]

    def remove_task(self, task_name):
        [self.task_list.remove(task) for task in self.task_list if task.name == task_name]

    def get_task_id(self, task_name):
        try:
            return [self.task_list[index].id for index, task in enumerate(self.task_list) if task.name == task_name][0]
        except IndexError:
            return None

class Task(object):
    def __init__(self, _id, name):
        self.id = _id
        self.name = name



