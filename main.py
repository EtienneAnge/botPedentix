from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
from openai import OpenAI


apiKey = "sk-fiv5yfnOoEnmDumB0ZxbqnTNlLgkCMBKB-LDCJ4WgCT3BlbkFJifivloN_ZHaQ8LGa9xAD3kBpTJC9tTC9T3gKf7DXcA"

client = OpenAI(api_key=apiKey)

geckodriver_path = "./geckodriver"


# Créer un objet Service avec le chemin du driver
service = Service(executable_path=geckodriver_path)

driver = webdriver.Firefox(service = service)
driver.get("https://cemantix.certitudes.org/pedantix")



driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/button/span").click()
driver.find_element(By.XPATH, "//*[@id='dialog-close']").click()

input_case = driver.find_element(By.XPATH, "//*[@id='pedantix-guess']")


#input_case.send_keys("un", Keys.ENTER)

tab = []

start_time = time.time()

id = 0

while True:

    try:
        # Tente de trouver l'élément par son id
        node = driver.find_element(By.ID, id)
    except:
        # Si l'élément n'est pas trouvé
        break

    if(node.text.strip() != ""):
        tab.append(node.text)
        #print(node.text)
    
    id = id + 1
    

print(tab)


end_time = time.time()
print(end_time - start_time)


histoMess=[{
        "role": "user",
        "content": "je joue au pédentix.Tu dois me donner 10 mot. Tu dois seulement me répondre par les mot et les mots doivent être séparé par '-'",
    },
    {
        "role": "assistant",
        "content": "d'accord alors allons y",
    }]

#histoMess.append({"role": "user","content": ("voici les mots trouvé " + str(tab))})

response = client.chat.completions.create(
    messages = histoMess,
    model="gpt-3.5-turbo",
)


# Affiche la réponse
print(response.choices[0].message.content)

histoMess.append({"role": "assistant","content": response.choices[0].message.content})

tableau = response.choices[0].message.content.split('-')

for i in range(0,10):
    input_case.send_keys(tableau[i], Keys.ENTER)
    time.sleep(0.05)
print(histoMess)
#driver.close()





