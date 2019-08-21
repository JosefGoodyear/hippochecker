from time import sleep
from config import driver, email, password, max_wait_time, no_color
from color import color
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def login():
    # log in to the intranet
    print('logging in...')
    try:
        driver.get('https://intranet.hbtn.io')
        driver.find_element_by_id('user_login').send_keys(email)
        driver.find_element_by_id('user_password').send_keys(password)
        driver.find_element_by_name('commit').click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, 'signed_in')))
    except TimeoutException:
        print('login failed.')
        driver.quit()
        exit()


def validator(project, problems):
    # Check that project and problem numbers are valid
    valid_problems = []
    driver.get('https://intranet.hbtn.io/projects/' + project)
    possible_problems = driver.find_elements_by_xpath("//*[contains(text(), 'Check your code?')]")
    if len(possible_problems) == 0:
        print('There are no problems to check for project ' + project)
        return valid_problems
    if problems == 'all':
        for problem in range(len(possible_problems)):
            valid_problems.append(problem)
        return valid_problems
    for problem in problems:
        if 0 <= problem < len(possible_problems):
            valid_problems.append(problem)
        else:
            print(str(problem) + ' is not a valid problem number or cannot be checked.')
    return valid_problems


def checker(project, problems):
    # Check valid problems
    for count, problem in enumerate(problems):
        print('checking #' + str(problem) + '...')
        if count != 0:
            driver.execute_script('window.open('');')
            driver.switch_to.window(driver.window_handles[count])
            driver.get('https://intranet.hbtn.io/projects/' + project)
        all_problems = driver.find_elements_by_xpath("//*[contains(text(), 'Check your code?')]")
        all_problems[problem].click()
        sleep(1)  # wait for check test to appear
        check = driver.find_elements_by_class_name('correction_request_test_admin')
        check[problem].click()


def results(problems):
    # Print results
    for count, problem in enumerate(problems):
        driver.switch_to.window(driver.window_handles[count])
        sleep(1)  # allow time for tab switch and loading to start
        wait = WebDriverWait(driver, max_wait_time)  # if timeout occurs try increasing max_wait_time.
        print('-------- Problem #' + str(problem) + ' --------')
        try:
            wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "check-inline")))
            sleep(1)  # allow time for all results to appear
        except TimeoutException:
            print('A timeout occurred while reporting the results. Try increasing max_wait_time.')
            continue
        code_passed_count = 0
        code_failed_count = 0
        req_passed_count = 0
        req_failed_count = 0
        code_passed = driver.find_elements_by_xpath('//div[@title="Correct output of your code - success"]')
        code_failed = driver.find_elements_by_xpath('//div[@title="Correct output of your code - fail"]')
        req_passed = driver.find_elements_by_xpath('//div[@title="Requirement - success"]')
        req_failed = driver.find_elements_by_xpath('//div[@title="Requirement - fail"]')
        for cp in code_passed:
            if cp.is_displayed():
                code_passed_count += 1
        for cf in code_failed:
            if cf.is_displayed():
                code_failed_count += 1
        for rp in req_passed:
            if rp.is_displayed():
                req_passed_count += 1
        for rf in req_failed:
            if rf.is_displayed():
                req_failed_count += 1
        if code_passed_count == 0 and code_failed_count == 0 and req_passed_count == 0 and req_failed_count == 0:
            print('Results failed to load.')
            continue
        if no_color:
            req_passed_str = str(req_passed_count)
            req_failed_str = str(req_failed_count)
            code_passed_str = str(code_passed_count)
            code_failed_str = str(code_failed_count)
        else:            
            req_passed_str = (color.green if req_passed_count > 0 else "") +\
                             str(req_passed_count) + color.reset
            req_failed_str = (color.red if req_failed_count > 0 else "") +\
                             str(req_failed_count) + color.reset
            code_passed_str = (color.bg.green + color.black if code_passed_count > 0 else "") +\
                              str(code_passed_count) + color.reset
            code_failed_str = (color.bg.red + color.black if code_failed_count > 0 else "") +\
                              str(code_failed_count) + color.reset
        print('REQUIREMENTS: ' + req_passed_str + ' passed. ' + req_failed_str + ' failed.')
        print('OUTPUT: ' + code_passed_str + ' passed. ' + code_failed_str + ' failed.')
