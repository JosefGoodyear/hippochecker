from time import sleep
from config import driver, email, password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login():
    print('logging in...')
    try:
        driver.get('https://intranet.hbtn.io')
        driver.find_element_by_id("user_login").send_keys(email)
        driver.find_element_by_id("user_password").send_keys(password)
        driver.find_element_by_name("commit").click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'signed_in')))
    except:
        print("login failed.")
        driver.quit()
        exit()


def checker(project, problems):
    for count, problem in enumerate(problems):
        print('checking #' + str(problem) + '...')
        if count != 0:
            driver.execute_script('window.open('');')
            driver.switch_to.window(driver.window_handles[count])
        driver.get('https://intranet.hbtn.io/projects/' + project)
        buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Check your code?')]")

        try:
            buttons[problem].click()
            sleep(0.5)
            check = driver.find_elements_by_class_name('correction_request_test_admin')
            check[problem].click()
        except IndexError:
            print(str(problem) + ' is not a valid problem, or cannot be checked.')

    # get feedback
    driver.switch_to.window(driver.window_handles[0])
    try:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'check-inline')))
        checks = driver.find_elements_by_class_name('check-inline')
        passed = driver.find_elements_by_class_name('success')
        failed = driver.find_elements_by_class_name('fail')
        req = driver.find_elements_by_class_name('requirement')
        code = driver.find_elements_by_class_name('code')
        code_passed = set(passed) & set(code)
        code_failed = set(failed) & set(code)
        req_passed = set(passed) & set(req)
        req_failed = set(failed) & set(req)
        print('-------- Problem #' + str(problem) + ' --------')
        print('NUMBER OF CHECKS: ' + str(len(checks)))
        print('TOTAL:' + str(len(passed)) + ' passed. ' + str(len(failed)) + ' failed.')
        print('REQUIREMENTS: ' + str(len(req_passed)) + ' passed. ' + str(len(req_failed)) + ' failed.')
        print('OUTPUT: ' + str(len(code_passed)) + ' passed. ' + str(len(code_failed)) + ' failed.')
    except:
        print('Results failed to load.')
        driver.quit()
        exit()
