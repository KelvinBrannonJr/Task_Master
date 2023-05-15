FILEPATH = "tasks.txt"


def get_tasks(filepath=FILEPATH):
    """ Read a text file and return the list of task items. """
    # With context manager - same as file.open() but, it automatically closes file after context scope
    with open(filepath, 'r') as file_local:
        tasks_local = file_local.readlines()
    return tasks_local


def write_tasks(tasks_arg, filepath=FILEPATH):
    """ Write the task items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(tasks_arg)