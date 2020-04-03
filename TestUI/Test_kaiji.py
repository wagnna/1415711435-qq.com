import time

from appium import webdriver
from self import self

from TestUI.app1 import findItem
import unittest
from TestUI.shijian import *


class Test_01(self):  # Base_page父类，为了使用父类里面的driver方法
    def __init__(self, driver: webdriver):
        self.driver = driver

    # def setup(self):
    #     self.start =start()

    #

    def test_kaiji(self):
        # 点击开屏的跳过按钮
        if findItem("com.hupu.games:id/tv_timer_jump"):
            self.driver.find_element_by_id("com.hupu.games:id/tv_timer_jump").click()
            print("找到跳过")  # 现在没有找到这个按钮，没有实现点击
        elif findItem("com.hupu.games:id/img_ads_full"):
            self.driver.find_element_by_id("com.hupu.games:id/img_ads_full").click()
            print("点击广告")
            time.sleep(3)
            self.driver.find_element_by_id("com.hupu.games:id/btn_back_arrow").click()
        time.sleep(4)



if __name__ == "__main__":
    s=start()
    unittest.main()
