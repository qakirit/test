import unittest
from appium import webdriver


class AndroidTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "Android Emulator",
            "app": "C:\\Users\\kirit.solanki\\PycharmProjects\\test\\Mosaico Tiles_2.5(22)-debug.apk",
            "automationName": "UiAutomator2"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def test_android_app(self):
        # Your test logic here
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
