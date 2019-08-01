from selenium import webdriver
from selenium.webdriver.chrome.options import Options

email = ''  # your login email
password = ''  # your password
headless = True  # headless recommended for setup/troubleshooting
results_in_terminal = True  # see results of checker in terminal

if headless is True:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
else:
    driver = webdriver.Chrome()
