##app > div.lite-page-wrap > div > div:nth-child(3) > div.lite-page-tab > div.tab-item.cur > i:nth-child(1)
import time

from selenium import webdriver

url = 'https://weibo.com/5884573948/H7wJvgD7M?ref=home&rid=0_131072_8_4725540773956118792_0_0&type=comment'


def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    driver.start_client()
    return driver


def find_info():
    # css_selector
    sel = 'span > span > span > em:nth-child(2)'
    elems = driver.find_elements_by_css_selector(sel)
    return [int(el.text) for el in elems[1:]]


while True:
    driver = start_chrome()
    driver.get(url)
    time.sleep(6)
    info = find_info()

    rep, comm, like = info
    if rep > 30:
        print('xxxxx'+str(rep))
        print(f'qwerrreww{rep}')
        break
    else:
        print('123444')

    time.sleep(1200)

print('done')
