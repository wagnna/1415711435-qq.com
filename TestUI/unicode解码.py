import time
from appium import webdriver
import re


def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


# 屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)


if __name__ == "__main__":
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',  # vivo:7486a58  小米8：e89fc8ee  华为V20：5ENDU19124004356  moniqi emulator-5554
        'platformVersion': '10',  # OPPO：5.1 小米8：8.1.0  华为V20：9 模拟器 10
        'appPackage': 'com.hupu.games',
        'appActivity': '.launcher.StartUpActivity',
        # 'appWaitActivity': '.view.activity.SlidingActivity',
        'noReset': 'true'
    }
    # 启动appium后，确认手机连上电脑，然后执行，就会启动App
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 休眠3秒等待页面加载完成
    time.sleep(15)
    driver.find_element_by_id("com.hupu.games:id/btn_mytab").click()
    print("点击我的")
    time.sleep(3)
    driver.find_element_by_xpath("//*[@text='JRs小说']").click()
    driver.implicitly_wait(25)
    """定位到书城"""
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                 ".FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android"
                                 ".webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View["
                                 "16]/android.view.View[2]/android.widget.Image").click()
    """热门下第一本书"""
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                 ".FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android"
                                 ".webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View["
                                 "1]/android.view.View[8]/android.widget.Image[2]").click()
    time.sleep(15)

    """进入详情页点击阅读打开阅读器"""

    """进入详情页加入书架"""

    driver.quit()


"""看完视频没有找到关闭按钮"""

"""
driver.find_element_by_xpath("//*[@text='集卡赢豪礼']").click()
元素：
集卡赢豪礼
抽奖：
看视频领：addNumDefault.26208b58
专家预测

"""
