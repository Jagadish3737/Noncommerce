import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup(browser):
    if browser == "ie":
        driver = webdriver.Ie()
        print("Launching ie browser.......")

    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching firefox browser.......")

    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching Microsoft edge browser.......")

    else:
        driver = webdriver.Chrome()
        print("Launching chrome browser.......")
    return driver

def pytest_addoption(parser):  #Get value from CLI/Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):    #Return browser value return method
    return request.config.getoption("--browser")



########### Pytest HTML Report #############

# It is the hooks for adding environment info to HTML report
def pytest_configure(config):
    config._metadata["Project name"] = 'nop commerce'
    config._metadata["Module name"] = 'Customers'
    config._metadata["Tester name"] = 'Jagadish'

# It is hook for Delete/Modify environment iinfo to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
