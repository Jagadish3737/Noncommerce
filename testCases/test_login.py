import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL= ReadConfig.getApplicationURL()
    username= ReadConfig.getUseremail()
    password= ReadConfig.getPassword()
    logger= LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("************* Test_001_Login ***************")
        self.logger.info("************* Start home page ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title= self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************* Home page passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.error("************* Home page failed ***************")
            assert False
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************* Login test verifying ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*************Login test passed***************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.error("*************Login test failed***************")
            self.driver.close()
            assert False