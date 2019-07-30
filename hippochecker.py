from parser import parser
from checker import checker, login


def main():
    user_input = parser()
    login()
    checker(user_input[0], user_input[1])


if __name__ == "__main__":
    main()
