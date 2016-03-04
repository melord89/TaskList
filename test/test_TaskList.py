import pytest
@pytest.fixture
def TaskList():
    from TaskList.TaskList import TaskList
    return TaskList()

@pytest.fixture
def Task():
    from TaskList.TaskList import Task
    return Task

def test_can_create_Task(Task):
    task = Task(1, 'task1')
    assert (task.id, task.name) == (1, 'task1')


def test_can_create_task_list(TaskList):
    assert TaskList


def test_is_empty_task_list_on_creation(TaskList):
    assert TaskList.get_task_list() == []


def test_can_return_task_list(TaskList):
    assert isinstance(TaskList.get_task_list(), list)


@pytest.fixture
def tasklist_with_one_task(TaskList, Task):
    TaskList.add_tasks(Task(1, 'task1'))
    return TaskList


@pytest.fixture
def tasklist_with_several_tasks(TaskList, Task):
    TaskList.add_tasks(Task(1, 'task1'),
                       Task(2, 'task2'),
                       Task(3, 'task3'))
    return TaskList

def test_can_add_new_task(tasklist_with_one_task, Task):
    list_len = len(tasklist_with_one_task.get_task_list())
    tasklist_with_one_task.add_tasks(Task(1, 'task1'))
    assert len(tasklist_with_one_task.get_task_list()) == list_len + 1


def test_check_length_after_remove(tasklist_with_several_tasks):
    list_lenght = len(tasklist_with_several_tasks.get_task_list())
    tasklist_with_several_tasks.remove_task('task3')
    assert list_lenght - len(tasklist_with_several_tasks.get_task_list()) == 1


def test_can_remove_task(tasklist_with_several_tasks):
    tasklist_with_several_tasks.remove_task('task2')
    assert 'task2' not in tasklist_with_several_tasks.get_task_list()
    assert 'task1', 'task3' in tasklist_with_several_tasks.get_task_list()
    tasklist_with_several_tasks.remove_task('task7')
    assert 'task7' not in tasklist_with_several_tasks.get_task_list()

def test_can_check_id(tasklist_with_one_task):
    assert tasklist_with_one_task.get_task_id('task1') == 1
    assert tasklist_with_one_task.get_task_id('task5') is None
