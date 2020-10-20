from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import smtplib

url = "https://www.coronatracker.com/pt-br/"


driver = webdriver.Chrome()
driver.get(url)

sleep(5)

save = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span')

death = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/span')

cases = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span')

casestext = cases.text
savetext = save.text
deathtext = death.text

print('Casos Confirmados: {}'.format(casestext))

print('Casos Recuperados: {}'.format(savetext))

print('Mortes: {}'.format(deathtext))

msg = '\nCasos Confirmados:\n'+ casestext +'\nCasos salvos:\n'+ savetext + '\nMortos:\n' + deathtext

def sendmail():
    smtp = "smtp.gmail.com"
    server = smtplib.SMTP_SSL (smtp, 465)
    server.login('vinicius26oliveira@gmail.com', 'vini2604') 
    server.sendmail('vinicius26oliveira@gmail.com','jalefa7654@nic58.com',msg)
    
    server.quit()

    print ('EMAIL ENVIADO COM URGÊNCIA')
    
print (sendmail())
