from parser import parser
from checker import checker, login, results


def main():
    user_input = parser()
    login()
    problems = checker(user_input[0], user_input[1])
    results(problems)


if __name__ == "__main__":
    main()
