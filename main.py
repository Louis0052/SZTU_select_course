from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium import webdriver
from time import localtime, strftime, sleep
from my_info import *


def is_exist(driver, xpath):  # 检查xpath路径是否存在，避免网页加载过慢导致的错误 若元素存在则返回该元素，不存在则返回false
    while 1:
        try:
            ele = driver.find_element(By.XPATH, xpath)
            return ele
        except NoSuchElementException:
            print("Element not found. Keep trying again.")
            sleep(1)
            driver.refresh()  # 刷新页面，重新加载元素


def login():
    # 初始化，并且不让浏览器界面关闭
    # 获取配置对象 => 什么样的浏览器就选择什么浏览器配置
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    option.add_argument("--headless")  # 隐藏浏览器页面
    # 获取driver对象, 并将配置好的option传入进去
    driver = webdriver.Chrome(options=option)
    driver.get('https://auth.sztu.edu.cn/idp/authcenter/ActionAuthChain?entityId=jiaowu')

    # 登录并进入选课界面
    driver.find_element(By.ID, 'j_username').send_keys(ac)
    sleep(0.3)
    driver.find_element(By.ID, 'j_password').send_keys(pw)
    driver.find_element(By.ID, 'loginButton').click()
    sleep(1.5)
    xk_button1 = is_exist(driver, '//*[@id="dataList"]/tbody/tr[1]/td/a')
    xk_button1.click()
    sleep(0.5)
    xk_button2 = is_exist(driver, '//*[@id="attend_class"]/tbody/tr[2]/td[4]/a')
    xk_button2.click()
    sleep(0.5)
    xk_button3 = is_exist(driver, '/html/body/form/div/div/input[2]')
    xk_button3.click()
    sleep(0.5)
    match course_type:  # 选课类型
        case '1':
            driver.get('https://jwxt.sztu.edu.cn/jsxsd/xsxkkc/comeInBxqjhxk')
        case '2':
            driver.get('https://jwxt.sztu.edu.cn/jsxsd/xsxkkc/comeInGgxxkxk')
        case '3':
            driver.get('https://jwxt.sztu.edu.cn/jsxsd/xsxkkc/comeInKnjxk')
        case '4':
            driver.get('https://jwxt.sztu.edu.cn/jsxsd/xsxkkc/comeInFawxk')
        case _:
            print('Course type error')
            driver.quit()
            exit()
    return driver


def select_course(driver):
    try_time = 1
    while 1:
        driver.execute_script(js_method)  # 控制台执行选课js方法
        select_status = driver.switch_to.alert.text  # 获取选课状态
        if '你确认选择' in select_status:
            driver.switch_to.alert.accept()
            select_status = driver.switch_to.alert.text
        # sleep(0.5)
        driver.switch_to.alert.accept()
        if '选课成功' in select_status:
            print(strftime('%Y-%m-%d %H:%M:%S', localtime()), select_status)
            driver.quit()
            return
        elif '已选择' in select_status or '冲突' in select_status:
            print(select_status)
            driver.quit()
            return
        else:  # 为了能够第一时间抢课，即使不在选课时间范围时程序也将持续运行
            print(select_status)
            try_time += 1
            sleep(gap_time)
            print(f'第{try_time}次自动选课中...')


if __name__ == '__main__':
    driver = login()
    driver.switch_to.window(driver.window_handles[0])  # 切换窗口，测试时此处新打开的页面处在第0位，不知道其他环境下情况是否相同，按需更改
    select_course(driver)
