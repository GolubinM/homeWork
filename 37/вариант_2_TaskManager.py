import time


def task_management_system():
    class TaskManager:
        def __init__(self):
            self.tasks = []
            self.__access_rules = {"editor": ["admin"],
                                   "viewer": ["admin", "user"]}

        def check_credentials(self, user_role, need_credentials):
            if user_role in self.__access_rules[need_credentials]:
                return True
            else:
                return False

        def _add_task(self, task_description, name_task_to, user_role):
            if self.check_credentials(user_role, need_credentials="editor"):
                new_task = Task(task_description, name_task_to)
                self.tasks.append(new_task)
                self.successful_add_task_message(task_description)
            else:
                self.not_credentials_message(task_description)

        def _get_task_by_description(self, user_role, tasks_key_words=""):
            if self.check_credentials(user_role, need_credentials="viewer"):
                return [task for task in self.tasks if
                        tasks_key_words.lower() in task._task_description.lower()]
            else:
                self.not_credentials_message()

        def _get_task_by_executor(self, user_role, executor_name_key_words=""):
            if self.check_credentials(user_role, need_credentials="editor"):
                return [task for task in self.tasks if
                        executor_name_key_words.lower() in task._executor.lower()]
            else:
                return self.not_credentials_message(print_msg=False)

        def _get_task_adapter(self, user_role, tasks_key_words="", get_object=False, get_name_to=False,
                              full_info=False):
            selected_tasks_obj = self._get_task_by_description(user_role, tasks_key_words)
            if get_object:
                return selected_tasks_obj
            elif get_name_to:
                return [f"{task._task_description}: {task._executor}" for task in selected_tasks_obj]
            elif full_info:
                if self.check_credentials(user_role, need_credentials="editor"):
                    return [
                        f"{i}. {task._task_description}: {task._executor}," \
                        f" start at {task._start_time}, is completed: {task._complete}"
                        for i, task in enumerate(selected_tasks_obj, 1)]
                else:
                    return self.not_credentials_message()
            else:
                return [task._task_description for task in selected_tasks_obj]

        def _set_task_executor(self, user_role, executor, tasks_key_words=""):
            if self.check_credentials(user_role, need_credentials="editor"):
                tasks = self._get_task_by_description(user_role, tasks_key_words)
                for task in tasks:
                    task._executor = executor
                    print(f"Executor '{task._task_description}' task set as '{executor}'")
            else:
                return self.not_credentials_message(print_msg=False)

        def _set_complete_status(self, user_role, tasks_key_words="", is_complete=True):
            tasks = self._get_task_by_description(user_role, tasks_key_words)
            if tasks:
                for task in tasks:
                    task._complete = is_complete

        @staticmethod
        def successful_add_task_message(task_description):
            print(f"Task '{task_description}' was created.")

        @staticmethod
        def not_credentials_message(task_description=None, print_msg=True):
            msg = "You have not enough credentials. "
            if task_description:
                msg += f"Task '{task_description}' was not created."
            if print_msg:
                print(msg)
            return False

    class User:
        def __init__(self, name, email="", role="user"):
            self.name = name
            self.email = email
            self.role = role.lower()

        def task_create(self, task_manager: TaskManager, name_task_to=None, task_description=None):
            if task_description is None:
                task_description = input("Введите описание задачи: ")
            if name_task_to is None:
                name_task_to = input("Введите имя ответственного за выполнение задачи: ")
            print(self.name)
            task_manager._add_task(task_description, name_task_to, self.role)

        def get_task_by_keyword(self, task_manager: TaskManager, task_keyword=""):
            tasks = task_manager._get_task_adapter(self.role, task_keyword, get_object=True)
            if tasks:
                return tasks
            else:
                return "You have not enough credentials."

        def get_task_description_by_keyword(self, task_manager: TaskManager, task_keyword=""):
            tasks = task_manager._get_task_adapter(self.role, task_keyword)
            if tasks:
                return tasks
            else:
                return "You have not enough credentials. "

        def get_task_descript_name_resp_by_keyword(self, task_manager: TaskManager, task_keyword=""):
            tasks = task_manager._get_task_adapter(self.role, task_keyword, get_name_to=True)
            if tasks:
                return tasks
            else:
                return "You have not enough credentials."

        def get_task_by_executor(self, task_manager: TaskManager, task_keyword="", get_obj=False):
            tasks = task_manager._get_task_by_executor(self.role, task_keyword)
            if tasks:
                if get_obj:
                    return tasks
                return [f'{task._executor}: {task._task_description}' for task in tasks]
            else:
                return "You have not enough credentials."

        def get_tasks_full_info(self, task_manager: TaskManager, task_keyword="", print_out=True):
            tasks = task_manager._get_task_adapter(self.role, task_keyword, full_info=True)
            if tasks:
                if print_out:
                    for task in tasks: print(task)
                return tasks
            else:
                return "You have not enough credentials."

        def set_executor(self, task_manager: TaskManager, task_keyword: str = "", executor: str = ""):
            task_manager._set_task_executor(self.role, executor, task_keyword)

        def set_complete_status(self, task_manager: TaskManager, task_keyword: str = "", is_completed: bool = True):
            task_manager._set_complete_status(self.role, task_keyword, is_completed)

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

    user1 = User("Tom", role="admin")
    user2 = User("Sam", role="user")
    manager1 = TaskManager()
    user1.task_create(manager1, "Karl", "Вырыть яму")
    user1.task_create(manager1, "Pierre", "Расширить яму")
    user1.task_create(manager1, "Pole", "Посадить дерево")
    user2.task_create(manager1, "Serge", "Закопать яму")
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


task_management_system()
