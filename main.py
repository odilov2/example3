import json
import admins_port
from classs import Student
import users_port


def sign_up():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user = Student(first_name, last_name, username, password, satus=0)
    user.add_user()
    print("Royxatdan otdingiz")

    return users_port.user_port(username, password)


def login(username, password):
    with open("users.json", "r") as file:
        data = json.load(file)
    for user in data["users"]:
        if user["username"] == username and user["password"] == password and user["status"] == "0":
            return users_port.user_port(username, password)

        elif user["username"] == username and user["password"] == password and user["status"] == "1":
            return admins_port.admin_port(username, password)

    print("Bunday username mavjud emas yoki password xato")
    return replay()


def replay():
    test = int(input(
        """
        1.Ro`yxatdan o`tish
        2.Bekor qilish
        """
    ))
    if test == 1:
        return sign_up()
    elif test == 2:
        return main()
    else:
        print("Bunday xizmat mavjud emas")
        return replay()


def main():
    tip = int(input(
        """
        1.Login
        2.Registor
        -> """
    ))

    if tip == 1:
        username = input("username: ")
        password = input("password: ")
        return login(username, password)
    elif tip == 2:
        return sign_up()
    else:
        print("Bunday xizmat turi mavjud emas")
        print("Iltimos koddan xato topmasdan o`zingiz to`g`ri ma`lumot kiriting")
        return main()


if __name__ == '__main__':
    main()
