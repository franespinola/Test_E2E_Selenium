from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def auto_test():
    url='https://biblioteca.um.edu.ar/?_gl=1*13zexqr*_ga*NTQwODQwMS4xNjkyMzcwOTMx*_ga_S845M31WNT*MTY5ODc1NzU0OS45NC4wLjE2OTg3NTc1NDkuMC4wLjA.*_ga_90T32KTHPN*MTY5ODc1NzU0OS45NC4wLjE2OTg3NTc1NDkuMC4wLjA.*_ga_5HD6DC6SNB*MTY5ODc1NzU0OS45NC4wLjE2OTg3NTc1NDkuMC4wLjA.&_ga=2.253938568.1227183241.1698623339-5408401.1692370931'
    
    driver = webdriver.Chrome()
    
    driver.get(url)

    time.sleep(1)
    
    driver.find_element(By.ID, "translControl1").send_keys('"Ingeniería de Software" de Pressman')

    driver.find_element(By.ID, "searchsubmit").submit()
    
    time.sleep(3)

    if '"Ingeniería de Software" de Pressman' in driver.page_source:
        print('Existe el libro')
    else:
        print('No existe el libro')
auto_test()