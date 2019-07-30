from time import sleep
from config import driver, email, password


def login():
    print('logging in...')
    driver.get('https://intranet.hbtn.io')
    driver.find_element_by_id("user_login").send_keys(email)
    driver.find_element_by_id("user_password").send_keys(password)
    driver.find_element_by_name("commit").click()

    # check for login success/failure


def checker(project,problems):
    for count, problem in enumerate(problems):
        print('checking #' + str(problem) + '...')
        if count != 0:
            driver.execute_script('window.open('');')
            driver.switch_to.window(driver.window_handles[count])
        driver.get('https://intranet.hbtn.io/projects/' + project)
        buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Check your code?')]")

        try:
            buttons[problem].click()
        except IndexError:
            print(str(problem) + ' is out of range')
            exit()
        sleep(0.5)
        check = driver.find_elements_by_class_name('correction_request_test_admin')
        check[problem].click()
    # get feedback
    driver.switch_to.window(driver.window_handles[0])
    sleep(35)  # add a sleep loop?
    checks = driver.find_elements_by_class_name('check-inline')
    passed = driver.find_elements_by_class_name('success')
    failed = driver.find_elements_by_class_name('fail')
    req = driver.find_elements_by_class_name('requirement')
    code = driver.find_elements_by_class_name('code')

    print('# of checks: ' + str(len(checks)))
    print('PASSED: ' + str(len(passed)) + 'checks. FAILED: ' + str(len(failed)) + 'checks.')
    print('Requirements: ' + str(len(req)) + 'checks. Output: ' + str(len(code)) + ' checks.')
