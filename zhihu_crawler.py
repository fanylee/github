from selenium import webdriver
import time


def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    driver.start_client()
    return driver


def find_strangers():
    # btn
    btn_sel = '#Pl_Official_RelationFans__90 > div > div > div > div.follow_box > div.follow_inner > ul > li:nth-child(5) > dl > dd.opt_box > span > a:nth-child(1)'
    elems = driver.find_elements_by_css_selector(btn_sel)
    return elems


def add_fren():
    pass

url = 'https://weibo.com/'
follow_url = 'https://weibo.com/5767028504/fans?from=100505&wvr=6&mod=headfans&current=fans#place'
driver = start_chrome()
driver.get(url)
if not driver.get_cookies():
#    push()
    time.sleep(20)

driver.get(follow_url)
time.sleep(6)
strangers = find_strangers()
strangers[0].click()
# for s in strangers:
# s.click()
time.sleep(3)

print('Done')
time.sleep(3000)
