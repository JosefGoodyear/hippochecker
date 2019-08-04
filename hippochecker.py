#!/usr/bin/env python3  # for Unix/Linux users. Change for windows
from parser import parser
from checker import login, validator, checker, results
from config import driver, headless, results_in_terminal


def main():

    user_input = parser()
    login()
    problems = validator(user_input[0], user_input[1])
    checker(user_input[0], problems)
    if results_in_terminal is True:
        results(problems)
    if headless is True:
        driver.quit()


if __name__ == '__main__':
    main()
