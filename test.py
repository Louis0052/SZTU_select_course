from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

def is_exist(driver,xpath):  # 检查xpath路径是否存在，避免网页加载过慢导致的错误
    try:
        ele = driver.find_element(By.XPATH,xpath)
        return ele
    except NoSuchElementException:
        return False

# 初始化，并且不让浏览器界面关闭
# 获取配置对象 => 什么样的浏览器就选择什么浏览器配置
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
option.add_argument("--headless")  # 隐藏浏览器页面
# 获取driver对象, 并将配置好的option传入进去
driver = webdriver.Chrome(options=option)
driver.get('https://auth.sztu.edu.cn/idp/authcenter/ActionAuthChain?entityId=jiaowu')
to_judge_element = driver.find_element(By.ID, 'j_username')
