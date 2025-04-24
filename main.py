from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
from openai import OpenAI



client = OpenAI(api_key=apiKey)

geckodriver_path = "./geckodriver"


# Créer un objet Service avec le chemin du driver
service = Service(executable_path=geckodriver_path)

driver = webdriver.Firefox(service = service)
driver.get("https://cemantix.certitudes.org/pedantix")



driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/button/span").click()
driver.find_element(By.XPATH, "//*[@id='dialog-close']").click()

input_case = driver.find_element(By.XPATH, "//*[@id='pedantix-guess']")
enter_case = driver.find_element(By.XPATH, "//*[@id='pedantix-guess-btn']")

 
# tab contenent la discussion avec chatgpt
histoMess=[{
            "role": "user",
            "content": "je joue au pédentix : je dois trouvé une page wikipedia (caché) avec des mots.Tu dois me donner 50 mots, sachant que tu ne dois jamais me donner un mot que tu m'as déjà donné et tu ne dois pas me donner de mot facile du genre déterminant, etc. J'utilise tas réponse dans un script python donc tu dois seulement me répondre par les mot et les mots doivent être séparé par '-'",
        }]

#historique du tableau des mots pour ne pas remettre les meme mot a chaque fois mais uniquement les nouveaux
tabHisto = []

while True:

    # I. cherche les mot de la page et les stocke dans un tableau

    #tableau contenent les mots de la page
    tab = []

    #cherche les mots avec les id
    id = 0

    while True:

        try:
            # Tente de trouver l'élément par son id
            node = driver.find_element(By.ID, id)
        except:
            # Si l'élément n'est pas trouvé
            break

        #enleve les mots non trouvé
        if(node.text.strip() != ""):
            tab.append(node.text)
            #print(node.text)
        
        id = id + 1
        

    #print(tab)

    tab = [mott for mott in tab if mott not in tabHisto]
    for mot in tab:
        tabHisto.append(mot)
    
    print(tab)
    if tab == []:
        histoMess.append({"role": "user","content": "continue avec la consigne du début. Aucun nouveau mot trouvé"})
    else:
        histoMess.append({"role": "user","content": ("continue avec la consigne du début. Voici les nouveaux mots trouvés " + str(tab))})

    response = client.chat.completions.create(
        messages = histoMess,
        model="gpt-3.5-turbo",
    )



    histoMess.append({"role": "assistant","content": response.choices[0].message.content})

    tableau = response.choices[0].message.content.split('-')

    for mot in tableau:
        input_case.send_keys(mot)
        enter_case.click()

print(histoMess)



#driver.close()





