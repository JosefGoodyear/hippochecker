from selenium import webdriver
from selenium.webdriver.chrome.options import Options

email = 'some_number@holbertonschool.com'  # your login email
password = 'some_password'  # your password
headless = False  # Set to False for setup/troubleshooting
results_in_terminal = True  # Set see results of checker in terminal

#  Initialize browser for Unix/Linux. May need to be changed for Windows.
if headless is True:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
else:
    driver = webdriver.Chrome()
