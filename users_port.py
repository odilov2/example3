import json
from main import replay


def log_out(username, password):
    print("Chiqishni xohlaysizmi")
    out = int(input(
        """
        1. Ha
        2. Yo`q 
     -> """
        ))
    if out == 1:
        return replay()

    elif out == 2:
        return user_port(username, password)

    else:
        print("Bunday xizmat yo`q")
        return log_out(username, password)


def refresh(username, password):
    new_username = input("Yangi usernameni kiriting: ")
    new_password = input("Yangi passwordni kiriting: ")
    with open("users.json", "r") as file:
        data = json.load(file)
    new_user = ""
    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            new_user = user
            new_user["username"] = new_username
            new_user["password"] = new_password
            data["users"].remove(data["users"].index(user))
            data["users"].append(new_user)
            with open("users.json", "w") as t:
                json.dump(data, t, indent=4)
            break

def course_list(username, password):
    with open("course_list.json", "r") as file:
        courses = json.load(file)
        j = courses["course"]
        for i in j:
            print(i)
            return user_port(username, password)


def back(username, password):
    print("Qaytishni istaysizmi")
    k = int(input(
        """
        1.Ha
        2.Yo`q
        
     -> """
    ))
    if k == 1:
        return user_port(username, password)
    else:
        return about_me(username, password)


def about_me(username, password):
    with open("users.json", "r") as file:
        data = json.load(file)
    users = ""
    for user in data["users"]:
        if user["username"] == username and user["password"] == password and user["status"] == "0":
            users = f"""
        
                  First_name: {user["first_name"]}
                  Last_name:  {user["last_name"]}
                  Username:   {user["username"]}
                  Password:   {user["password"]}
                  Create_date: {user["create_date"]}
                  """
    print(users)
    return back(username, password)


def user_port(username, password):
    kind = int(input(
        """
        1. Profil
        2. Kurslar ro`yxati
        3. Kursga yozilish
        4. Ma`lumotlarni o`zgartirish
        5. Chiqish
        """
    ))

    if kind == 1:
        return about_me(username, password)

    elif kind == 2:
        return course_list(username, password)

    elif kind == 3:
        pass

    elif kind == 4:
        return refresh(username, password)

    elif kind == 5:
        return log_out(username, password)
    else:
        print("Bunday xizmat mavjud emas")
        return user_port(username, password)
