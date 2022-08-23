import pytest as pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get('https://lexmotion.pipedrive.com')
        request.cls.browser = browser
    except Exception as e:
        print(e)
    finally:
        yield
        browser.quit()
