from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# Inicia ChromeDriver
#options = Options()  
#options.add_argument("--headless")
chrome = webdriver.Chrome('/Users/bruno/Desktop/python/chromedriver')#local que estiver o chromedriver
comentario = 175
nomes = ["@perfis de usuarios do insta"]
nome = 0

# Abre Pagina 
chrome.get('https://www.instagram.com/')


input('pressione ENTER para iniciar...')

# Abre Pagina sorteio
chrome.get('https://www.instagram.com/xxxxxxxx/') #pagina do sorteio
chrome.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div/div/div/div[2]/a/div/div[2]').click()
      
while 1:
    
    while(1):
        try:
            chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click()
            chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(nomes[nome] + " " + nomes[nome+1]+ " " + str(comentario))
            sleep(3)
            break
        except:       
            continue
# ENVIA COMENTARIO:
    while(1):
        try:
            chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]').click()
            sleep(5)
            chrome.get('https://www.instagram.com/xxxxxx/')  #pagina aleatorio          
            sleep(5)
            chrome.get('https://www.instagram.com/')
            sleep(10)
            chrome.get('https://www.instagram.com/xxxxxx/') #pagina aleatorio
            sleep(5)
            chrome.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div/div/div/div[2]/a/div/div[2]').click()
            sleep(5)
            break
        except:             
            continue
      
    comentario = comentario + 1
    nome = nome + 1
    if nome > len(nomes):
        nome = 0
    print("Realizado " + str(comentario) + " tentativas")













    
        





   
            
 
  


    
    
    
 
