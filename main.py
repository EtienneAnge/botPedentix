from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

geckodriver_path = "geckodriver"


# Créer un objet Service avec le chemin du driver
service = Service(executable_path=geckodriver_path)

driver = webdriver.Firefox(service = service)
driver.get("https://cemantix.certitudes.org/pedantix")



driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/button/span").click()
driver.find_element(By.XPATH, "//*[@id='dialog-close']").click()

input_case = driver.find_element(By.XPATH, "//*[@id='pedantix-guess']")


def is_element_present(driver, xpath):
    try:
        # Tente de trouver l'élément par son XPath
        driver.find_element(By.XPATH, xpath)
        return True
    except NoSuchElementException:
        # Si l'élément n'est pas trouvé, renvoie False
        return False

input_case.send_keys("un", Keys.ENTER)

i = 1
tab = []

while is_element_present(driver,"//*[@id='article']" + "/p[" + i + "]"):
	while is_element_present(driver,)
	i++
	pass

#driver.close()





