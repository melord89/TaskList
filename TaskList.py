class TaskList(object):
    def __init__(self):
        self.task_list = []


    def get_task_list(self):
        return self.task_list

    def add_several_tasks(self, tasks):
        self.task_list.append(tasks)
        # self.task_list.update({id : task_name})

    def remove_task(self, task_name):
        self.task_list.remove(task_name)


class Task(object):
    def __init__(self, _id, tname):
        self.id = _id
        self.tname = tname



