import json


def users_list(username, password):
    with open("users.json", "r") as file:
        user = json.load(file)
        j = user["users"]
        for i in j:
            print(i)
            return admin_port(username, password)


def ref(username, password):
    new_username = input("Yangi usernameni kiriting: ")
    new_password = input("Yangi passwordni kiriting: ")
    with open("users.json", "r") as file:
        data = json.load(file)

    for user in data["users"]:
        if user["username"] == new_username or user["password"] == new_password:
            print("Siz eski ma`lumotlarni kiritdingiz")
            return ref(username, password)
        else:
            if user["status"] == "1":
                user["username"] = new_username
                user["password"] = new_password
                with open("users.json", "w") as t:
                    json.dump(data, t, indent=4)
            else:
                break
            return admin_port(username, password)


def add_course(self):
    with open("course_list.json", "r") as file:
        data = json.load(file)
        new_course = f"""
          "name": "{self.name}",
          "description": "{self.description}",
          "modules_count": {self.__modules_count},
          "price": {self.__price},
          "status": "{self.__status}",
          "active_students": {self.active_students}
          """
        for course in data["course"]:
            if course["name"] == self.name and course["description"] == self.description and course[
             "modules_count"] == self.__modules_count and course["price"] == self.__price:
                data.append(new_course)
                with open("course_list.json", "w") as f:
                    json.dump(data, f, indent=4)
            else:
                print("Bunday kurs mavjud")
                return admin_port


def courses_list(username, password):
    with open("course_list.json", "r") as file:
        courses = json.load(file)
        j = courses["course"]
        for i in j:
            print(i)
            return admin_port(username, password)


def admin_port(username, password):
    services = int(input(
        """
        1. Kurslar royxati
        2. Kurs qo`shish
        3. Userlar royxati
        4. Ma`lumotlarni o`zgartirish
     -> """))

    if services == 1:
        return courses_list(username, password)

    if services == 2:
        return add_course(username)

    if services == 3:
        return users_list(username, password)

    if services == 4:
        return ref(username, password)
