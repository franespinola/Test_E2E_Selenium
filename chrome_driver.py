from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def auto_test():
    
    driver = webdriver.Chrome()
    
    driver.get("https://virtual.um.edu.ar/login/index.php")

    username = driver.find_element(By.ID, "username")
    password= driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "loginbtn")

    username.send_keys("r.espinola")
    password.send_keys("kike5829")
    login_button.click()
    

    time.sleep(1)
    driver.get("https://virtual.um.edu.ar/mod/questionnaire/complete.php?id=210589")
    time.sleep(1)
    
    selector_1=driver.find_element(By.ID, 'auto-rb0001')
    if not selector_1.is_selected():
        selector_1.click()
    time.sleep(1)
    
    selector_2=driver.find_element(By.ID, 'dropSelecciòn')
    selector_2.click()
    time.sleep(1)

    select = Select(selector_2)
    select.select_by_index(3)
    time.sleep(1)

    enviar_encuesta=driver.find_element(By.CSS_SELECTOR, '#phpesp_response > div > div > input.btn.btn-primary.control-button-submit')
    enviar_encuesta.click()
    time.sleep(1)

auto_test()