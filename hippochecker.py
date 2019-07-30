from parser import parser
from checker import checker


def main():
    user_input = parser()
    checker(user_input[0], user_input[1])


if __name__ == "__main__":
    main()
