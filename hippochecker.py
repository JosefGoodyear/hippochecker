#!/usr/bin/env python3
from parser import parser
from checker import checker, login, results, validator
from config import results_in_terminal, headless, driver


def main():
    user_input = parser()
    login()
    problems = validator(user_input[0], user_input[1])
    checker(user_input[0], problems)
    if results_in_terminal is True:
        results(problems)
    if headless is True:
        driver.quit()


if __name__ == "__main__":
    main()
