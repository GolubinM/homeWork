import time


def task_management_system():
    class TaskManager:
        def __init__(self):
            self.tasks = []

        def _add_task(self, task_description, name_task_to):
            new_task = Task(task_description, name_task_to)
            self.tasks.append(new_task)
            self.successful_add_task_message(task_description)

        def _get_task_by_description(self, tasks_key_words=""):
            return [task for task in self.tasks if
                    tasks_key_words.lower() in task._task_description.lower()]

        def _get_task_by_executor(self, executor_name_key_words=""):
            return [task for task in self.tasks if
                    executor_name_key_words.lower() in task._executor.lower()]

        def _get_task_adapter(self, tasks_key_words="", get_object=False, get_name_to=False,
                              full_info=False):
            selected_tasks_obj = self._get_task_by_description(tasks_key_words)
            if get_object:
                return selected_tasks_obj
            elif get_name_to:
                return [f"{task._task_description}: {task._executor}" for task in selected_tasks_obj]
            elif full_info:
                return [
                    f"{i}. {task._task_description}: {task._executor}," \
                    f" start at {task._start_time}, is completed: {task._complete}"
                    for i, task in enumerate(selected_tasks_obj, 1)]
            else:
                return [task._task_description for task in selected_tasks_obj]

        def _set_task_executor(self, executor, tasks_key_words=""):
            tasks = self._get_task_by_description(tasks_key_words)
            for task in tasks:
                task._executor = executor
                print(f"Executor '{task._task_description}' task set as '{executor}'")

        def _set_complete_status(self, tasks_key_words="", is_complete=True):
            tasks = self._get_task_by_description(tasks_key_words)
            if tasks:
                for task in tasks:
                    task._complete = is_complete

        @staticmethod
        def successful_add_task_message(task_description):
            print(f"Task '{task_description}' was created.")

    class User:
        def __init__(self, name, email=""):
            self.name = name
            self.email = email

        @staticmethod
        def get_task_by_keyword(task_manager: TaskManager, task_keyword=""):
            """get task as Task's object by task description's keyword string"""
            tasks = task_manager._get_task_adapter(task_keyword, get_object=True)
            if tasks:
                return tasks

        @staticmethod
        def get_task_description_by_keyword(task_manager: TaskManager, task_keyword=""):
            """get task description by task description's keyword string"""
            tasks = task_manager._get_task_adapter(task_keyword)
            if tasks:
                return tasks

        @staticmethod
        def get_task_descript_name_resp_by_keyword(task_manager: TaskManager, task_keyword=""):
            """get task description and executor name by task description's keyword string"""
            tasks = task_manager._get_task_adapter(task_keyword, get_name_to=True)
            if tasks:
                return tasks

        @staticmethod
        def get_task_by_executor(task_manager: TaskManager, task_keyword="", get_obj=False):
            """get task description by executor name's keyword string"""
            tasks = task_manager._get_task_by_executor(task_keyword)
            if tasks:
                if get_obj:
                    return tasks
                return [f'{task._executor}: {task._task_description}' for task in tasks]

    class Admin(User):
        def __init__(self, name, email=""):
            super().__init__(name, email)
            self._role = "admin"

        @staticmethod
        def task_create(task_manager: TaskManager, executor=None, task_description=None):
            while not task_description:
                task_description = input("Введите описание задачи: ")
            while not executor:
                executor = input("Введите имя ответственного за выполнение задачи: ")
            task_manager._add_task(task_description, executor)

        @staticmethod
        def set_executor(task_manager: TaskManager, task_keyword: str = "", executor: str = ""):
            task_manager._set_task_executor(executor, task_keyword)

        @staticmethod
        def set_complete_status(task_manager: TaskManager, task_keyword: str = "", is_completed: bool = True):
            task_manager._set_complete_status(task_keyword, is_completed)

        @staticmethod
        def get_tasks_full_info(task_manager: TaskManager, task_keyword="", print_out=True):
            tasks = task_manager._get_task_adapter(task_keyword, full_info=True)
            if tasks:
                if print_out:
                    for task in tasks: print(task)
                return tasks

    class Task:
        def __init__(self, task_description, executor):
            self._task_description = task_description
            self._executor = executor
            self._complete = False
            self._start_time = time.ctime()

        def __set_task(self):
            self._task_description = input("Введите описание задачи")

        def __set_task_user(self, user: User):
            self._executor = user

        def __set_task_complete(self, is_complete: bool):
            self._complete = is_complete

        def __get_task(self):
            return self._task_description

        def __get_task_user(self, user: User):
            return self._executor

        def __get_task_complete(self):
            return self._complete

    user1 = Admin("Tom")
    user2 = User("Sam")
    manager1 = TaskManager()
    user1.task_create(manager1)
    user1.task_create(manager1, "Karl", "Вырыть яму")
    user1.task_create(manager1, "Pierre", "Расширить яму")
    user1.task_create(manager1, "Pole", "Посадить дерево")
    try:
        user2.task_create(manager1, "Serge", "Закопать яму")
    except AttributeError as e:
        print(e, "Данный пользователь не является экземпляром класса Admin!")

    user1.task_create(manager1, "Serge", "Закопать яму")
    print(user1.get_task_description_by_keyword(manager1, "Вырыть"))
    print(user1.get_task_description_by_keyword(manager1, "ям"))
    print(user1.get_task_description_by_keyword(manager1))
    print(user1.get_task_descript_name_resp_by_keyword(manager1))
    print(user1.get_task_descript_name_resp_by_keyword(manager1, "ДЕРЕВО"))
    print(user2.get_task_by_executor(manager1, ""))
    user1.set_executor(manager1, "Закопать яму", "Karl")
    print(user1.get_task_by_executor(manager1, ""))
    user1.set_complete_status(manager1, "ям", is_completed=True)
    user1.set_complete_status(manager1, "Закопать", is_completed=False)
    user1.get_tasks_full_info(manager1)
    try:
        user2.get_tasks_full_info(manager1, "купи")
    except AttributeError as e:
        print(e, "Данный пользователь не является экземпляром класса Admin!")


task_management_system()
