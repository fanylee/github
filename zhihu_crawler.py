from selenium import webdriver
import time


def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    driver.start_client()
    return driver


def find_strangers():
    # btn
    btn_sel = 'div.ContentItem-extra > button.Button--blue'
    elems = driver.find_elements_by_css_selector(btn_sel)
    return elems


def add_fren():
    pass


def push():
    pass


while True:
    url = ''
    follow_url = ''
    driver = start_chrome()
    driver.get(url)
    if not driver.get_cookie():
        push()
    time.sleep(20)  # waitin login

driver.get(follow_url)
time.sleep(6)
strangers = find_strangers()
for s in strangers:
    s.click()
    time.sleep(3)

print('Done')
time.sleep(3000)
