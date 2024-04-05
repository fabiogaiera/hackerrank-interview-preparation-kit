import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


def test_releases_all():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')

    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver) \
        .click_and_hold(clickable) \
        .key_down(Keys.SHIFT) \
        .key_down("a") \
        .perform()

    time.sleep(3600)


def test_basic_options_edge():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    driver.get("https://www.selenium.dev")

    driver.find_element(By.XPATH, "//li[@id='MNU_W_order']").click()

    time.sleep(3600)

    driver.quit()


def test_basic_options_chrome():
    try:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        time.sleep(20)
        driver.quit()
    except Exception as e:
        print("An error occurred:", e)


test_releases_all()
