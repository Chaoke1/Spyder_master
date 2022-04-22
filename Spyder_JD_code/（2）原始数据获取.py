import requests
import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def Spyder_Master(drive, url):
    dic = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        # 根据不同的设备进行更改
    }
    goods_simple = open('goods_List.txt', mode='a', encoding='utf-8')
    driver.get(url)
    # /html/body/div[7]/div/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[3]/strong/i       记录XPath完整地址
    # //*[@id=\"J_goodsList\"]/ul/li[1]/div/div[3]/strong/i                             记录XPath相对地址

    scroll_to_bottom(driver)
    for i in range(1, 60):
        price = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div[1]/div/div[2]/ul/li[" + str(
            i) + "]/div/div[3]/strong/i")
        Name_brand = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div[1]/div/div[2]/ul/li[" + str(
            i) + "]/div/div[4]/a/em")
        goods_simple.write(str(price.text) + " " + str(Name_brand.text) + "\n")
        # print(price.text + " " + Name_brand.text)
    driver.quit()


def scroll_to_bottom(driver):
    # 控制浏览器自动拉倒底部

    js = "return action=document.body.scrollHeight"
    # 初始化现在滚动条所在高度为0
    height = 0
    # 当前窗口总高度
    new_height = driver.execute_script(js)

    while height < new_height:
        # 将滚动条调整至页面底部
        for i in range(height, new_height, 100):
            driver.execute_script('window.scrollTo(0, {})'.format(i))
            time.sleep(0.2)
        height = new_height
        time.sleep(0.1)
        new_height = driver.execute_script(js)



for j in range(1, 91):
    s = Service(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")  # 驱动路径，调试使用的话需要安装合适的浏览器驱动
    driver = webdriver.Chrome(service=s)
    time.sleep(2)
    url = "https://list.jd.com/list.html?cat=9987%2C653%2C655&page=" + str(2 * j - 1) + "&s=" + str(60 * j - 59) + "&click=0"
    Spyder_Master(driver,url)

