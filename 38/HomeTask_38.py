from abc import abstractmethod, ABC
from random import choice


# ====задача 1=======================================================================
class MediaAccount(ABC):
    @abstractmethod
    def account_registration(self, login, password):
        """Принимает логин для регистрации и проверяет его корректность и уникальность"""
        pass

    @abstractmethod
    def check_password(self, password):
        """Принимает пароль для регистрации и проверяет его на соответствие требованиям безопасности"""
        pass

    @abstractmethod
    def is_login_unique(self, login):
        """Проверяет логин на уникальность"""
        pass


class Facebook(MediaAccount):
    def account_registration(self, login, password):
        if 5 < len(login) < 15 and self.is_login_unique(login):
            if self.check_password(password):
                print(
                    f"Логин и пароль корректны. Учетная запись с логином {login} зарегистрирована"
                    f" на {self.__class__.__name__}.")
            else:
                print("Пароль не соответствует требованиям безопасности")
        else:
            print(f"Логин не уникален или не соответствует правилам регистрации {self.__class__.__name__}")

    def check_password(self, password):
        return choice([True, True, False])

    def is_login_unique(self, login):
        return choice([True, True, True, False])


class Instagram(MediaAccount):
    def account_registration(self, login, password):
        if 5 < len(login) < 15 and self.is_login_unique(login):
            if self.check_password(password):
                print(
                    f"Логин и пароль корректны. Учетная запись с логином {login} зарегистрирована"
                    f" на {self.__class__.__name__}.")
            else:
                print("Пароль не соответствует требованиям безопасности")
        else:
            print(f"Логин не уникален или не соответствует правилам регистрации {self.__class__.__name__}")

    def check_password(self, password):
        return choice([True, True, True, True, True, True, True, True, True, False])

    def is_login_unique(self, login):
        return choice([True, False])


class Twitter(MediaAccount):
    def account_registration(self, login, password):
        if 3 < len(login) < 20 and self.is_login_unique(login):
            if self.check_password(password):
                print(
                    f"Логин и пароль корректны. Учетная запись с логином {login} зарегистрирована"
                    f" на {self.__class__.__name__}.")
            else:
                print("Пароль не соответствует требованиям безопасности")
        else:
            print(f"Логин не уникален или не соответствует правилам регистрации {self.__class__.__name__}")

    def check_password(self, password):
        return choice([True, True, True, True, False])

    def is_login_unique(self, login):
        return choice([True, True, True, True, True, True, False])


class SocialMediaAccountFactory:
    @staticmethod
    def create_media_account(social_network_name: str, login, account):
        social_network_name = social_network_name.lower()
        if social_network_name == 'twitter':
            account = Twitter()
            return account.account_registration(login, account)

        elif social_network_name == 'instagram':
            account = Instagram()
            return account.account_registration(login, account)

        elif social_network_name == 'facebook':
            account = Facebook()
            return account.account_registration(login, account)
        else:
            print('Не возможно зарегистрироваться в этой социальной сети')
            return False


class ProxySocialMediaAccount:
    def __init__(self):
        self.incorrect_content = ("Нельзя так говорить", "Cont2", "Cont3",)
        self.login_access_denied = {"resource1": ["Login2"],
                                    "resource2": ["Login3"],
                                    "resource3": ["Login1", "Login2", "Cont3"]}

    def content_moderation(self, content, login):
        if content in self.incorrect_content:
            print(f"Incorrect content '{content}' by '{login}' account. Publication refused")
            self.set_login_blocked("resource1", login)

        else:
            print(f"'{content}' is published")

    def access_control(self, resource, login):
        if login in self.login_access_denied[resource]:
            print(f"Access on {resource} for {login} account is closed.")
            return False
        else:
            print(f"Access on {resource} for {login} account is open.")
            return True

    def set_login_blocked(self, resource, login):
        self.login_access_denied[resource].append(login)
        print(f"Login '{login}' is added in block list for '{resource}' resource.")


factory = SocialMediaAccountFactory()
acc_tw1 = factory.create_media_account("Twitter", "Login1", "12333")
acc_tw2 = factory.create_media_account("twitter", "ab", "1fdsfssd2333")
acc_tw3 = factory.create_media_account("Twwitter", "absfdfsc", "12333")
print("-*-" * 30)
proxy1 = ProxySocialMediaAccount()
proxy1.access_control("resource1", "Login1")
proxy1.access_control("resource2", "Login1")
proxy1.content_moderation("Cont5", "Login1")
proxy1.content_moderation("Нельзя так говорить", "Login1")
print("-*-" * 30)
print("-*-" * 30)
# ===================================================================================
# ====задача 2=======================================================================


from time import ctime


class File:
    @staticmethod
    def open_file(filename):
        return open(filename, encoding="utf-8")

    def get_content_from_file(self, filename):
        try:
            content = self.open_file(filename).read()
            return content
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def write_content_to_file(filename, content):
        try:
            open(filename, "w", encoding="utf-8").write(content + "\n")
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def add_content_to_file(filename, content):
        try:
            open(filename, "a", encoding="utf-8").write(content + "\n")
            return True
        except Exception as e:
            print(e)
            return False


class FileProxy:
    def __init__(self):
        self.file_access_denied = ["password.txt", "my_diary.txt"]
        self.files_cash = {"filename": "cashed_file_content"}

    @staticmethod
    def get_content_file_with_logging(filename_to_read, log_filename="read_attempt.log"):
        log = f"{filename_to_read}: attempt to read on {ctime()}"
        content = File().get_content_from_file(filename_to_read)
        log += f", is successful: {bool(content)}."
        open(log_filename, "a", encoding="utf-8").write(f"{filename_to_read}: attempt to read on {ctime()}\n")
        print(log)
        return content

    def get_content_file_with_cashed(self, filename):
        content = File().get_content_from_file(filename)
        if bool(content):
            self.files_cash[filename] = content
            print(f"'{filename}' file content was added to cash")
        else:
            print(f"'{filename}' file content was not added to cash")
        return content

    def get_content_file_access_control(self, filename):
        if filename in self.file_access_denied:
            print(f"Access to '{filename}' file is denied")
            return False
        else:
            return File().get_content_from_file(filename)


text1 = "Пример содержания: 1"
f = File()
print("1).** class File ***********")
f.write_content_to_file("test1.txt", text1)
open_f_obj = f.open_file("test1.txt")
print(type(open_f_obj))
print(open_f_obj.read())
print("2).*************************")
text2 = "Пример содержания: 2"
f.add_content_to_file("test1.txt", text2)
file_content2 = f.get_content_from_file("test1.txt")
print(file_content2)
f.write_content_to_file("my_diary.txt", file_content2)
print("3).*************************")
proxy1 = FileProxy()
proxy1.get_content_file_with_logging("test1.txt")
proxy1.get_content_file_with_logging("my_diary.txt")
controlled_content1 = proxy1.get_content_file_access_control("test1.txt")
print(controlled_content1)
print("4).*************************")
controlled_content2 = proxy1.get_content_file_access_control("my_diary.txt")
print(controlled_content2)
print("5.1).*************************")
cont4 = proxy1.get_content_file_with_cashed("test1.txt")
print(cont4)
print("5.2).***cashed content********")
cashed_cont4 = proxy1.files_cash["test1.txt"]
print(cashed_cont4)


# ===================================================================================
# ====задача 3=======================================================================

class Command(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def process(self):
        pass


class VolumeUpCommand(Command):
    def process(self):
        self.receiver.volume_up_command()


class VolumeDownCommand(Command):
    def process(self):
        self.receiver.volume_down_command()


class PowerOnCommand(Command):
    def process(self):
        self.receiver.power_on_command()


class PowerOffCommand(Command):
    def process(self):
        self.receiver.power_off_command()


# Объект-получатель
class Receiver:
    @staticmethod
    def volume_up_command():
        print('Volume increase.')

    @staticmethod
    def volume_down_command():
        print('Volume decrease')

    @staticmethod
    def power_on_command():
        print('Power on.')

    @staticmethod
    def power_off_command():
        print('Power off.')


class RemoteControl:
    def __init__(self):
        self.assign_button_command = {}
        self._commands: list = []
        self._current_command_key = 0

    def push_command(self, command):
        """помещаем команду в реестр команд"""
        self._commands.append(command)

    def set_command(self, button, cmd):
        # self.cmd = cmd
        self.assign_button_command[button] = cmd

    def press_button(self, button):
        try:
            current_command = self.assign_button_command[button]
            self.push_command(current_command)
            current_command.process()
        except Exception as e:
            print(f"Button {button} is not assigned any command.")

    def press_undo_btn(self):
        try:
            last_command = self._commands.pop()
            print(f"Last command '{last_command.__class__.__name__}' was canceled")
        except Exception as e:
            print("There is not any command to cancel")

    def press_redo_btn(self):
        try:
            last_command = self._commands[-1]
            self.push_command(last_command)
            last_command.process()
            print(f"Last command '{last_command.__class__.__name__}' was repeated")
        except Exception as e:
            print("There is not any command to cancel")


tv = Receiver()
print(tv)
power_on_command = PowerOnCommand(tv)
power_off_command = PowerOnCommand(tv)
volume_up_command = VolumeUpCommand(tv)
volume_down_command = VolumeDownCommand(tv)
print(volume_up_command.receiver)
print(volume_up_command)
remote_control = RemoteControl()
remote_control.set_command("On", power_on_command)
remote_control.set_command(2, volume_up_command)
remote_control.set_command(9, volume_down_command)
remote_control.press_button("On")
remote_control.press_button(2)
remote_control.press_button(9)
remote_control.press_redo_btn()
remote_control.press_undo_btn()
remote_control.press_undo_btn()
remote_control.press_undo_btn()
remote_control.press_undo_btn()
