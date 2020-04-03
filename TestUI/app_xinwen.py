from appium import webdriver
import time


# 滑动屏幕
# 获得机器屏幕大小x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


# 屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)


# 查找元素是否存在
def findItem(el):
    source = driver.page_source
    if el in source:
        return True
    else:
        return False


def findNewsADItem(el1, el2):
    r_el1 = findItem(el1)
    r_el2 = findItem(el2)
    return r_el1 or r_el2
"""
app进入app
用例---开机-点击落地页
用例2---进入综合tab，点里面广告，click后返回到综合列表，再继续往下找
用例3---NBA 社区
"""

if __name__ == "__main__":
    # 安卓
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '7486a58',  # vivo:7486a58  小米8：e89fc8ee  华为V20：5ENDU19124004356
        'platformVersion': '9',  # OPPO：5.1 小米8：8.1.0  华为V20：9
        'appPackage': 'com.hupu.games',
        # 'appActivity': 'com.hupu.games.activity.LaunchActivity',
        'appActivity': '.launcher.StartUpActivity',
        'noReset': 'true'
    }
    print(desired_caps)
    # 启动appium后，确认手机连上电脑，然后执行，就会启动App
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 休眠3秒等待页面加载完成
    time.sleep(3)
    print(driver)
    # 点击开屏的跳过按钮
    if findItem("com.hupu.games:id/tv_timer_jump"):
        driver.find_element_by_id("com.hupu.games:id/tv_timer_jump").click()
        print("找到跳过")   #现在没有找到这个按钮，没有实现点击
    elif findItem("com.hupu.games:id/img_ads_full"):
        driver.find_element_by_id("com.hupu.games:id/img_ads_full").click()
        print("点击广告")
        time.sleep(3)
        driver.find_element_by_id("com.hupu.games:id/btn_back_arrow").click()
    time.sleep(4)
