import datetime
import json


class User:
    def __init__(self, username: str, password: str, status=0):
        self.__username = username
        self.__password = password
        self.__status = status
        self.create_date = f'{datetime.datetime.today().date()}'

    def get_username(self):
        return self.__username

    def set_username(self, new_username):
        with open("users.json", "r") as file:
            data = json.load(file)
        for user in data["users"]:
            if user["username"] != new_username:
                self.__username = new_username
            else:
                print(f'{new_username} nomli foydalanuvchi mavjud.')

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        if new_password != self.__password and len(new_password) >= 8:
            self.__password = new_password
        else:
            print("Siz eski passwordni kiritdingiz yoki password uzunligini meyoriga yetkazmadingiz")

    def get_status(self):
        return self.__status

    def get_create_date(self):
        return self.create_date


class Student(User):
    def __init__(self, first_name, last_name, username, password, satus):
        User.__init__(self, username, password, satus)
        self.first_name = first_name
        self.last_name = last_name
        self.create_date = f'{datetime.datetime.today().date()}'

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def add_user(self):
        with open("users.json", "r") as file:
            data = json.load(file)

        new_user = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": Student.get_username(self).__str__(),
            "password": Student.get_password(self).__str__(),
            "status": Student.get_status(self).__str__(),
            "create_date": self.create_date
        }

        data["users"].append(new_user)
        with open("users.json", "w") as k:
            json.dump(data, k, indent=4)


class Course:
    def __init__(self, name, description, modules_count, price, status, active_students):
        self.name = name
        self.description = description
        self.__modules_count = modules_count
        self.__price = price
        self.__status = status
        self.active_students = active_students
        self.create_date = datetime.datetime.today()

    def get_modules_count(self):
        return self.__modules_count

    def get_price(self):
        return self.__price

    def get_status(self):
        return self.__status

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_active_students(self):
        return self.active_students

    def create_date(self):
        return self.create_date
