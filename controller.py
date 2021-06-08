#Created by : Putra
#Updated at 08 June 2020 11:00


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import json
from time import sleep
import requests
import os

f = open('settings.json',)
raw = json.load(f)
url = f"{raw['url']}?"
uploader_name = raw["uploader_name"]
squad = raw["squad"]
phone_number = raw["phone_number"]
retool = raw["retool_url"]

urlWhatsapp = 'http://events.temancurhat.id:3000/whatsapp/send'

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("--log-level=3")



driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chrome_options)

wait = WebDriverWait(driver, 100)
LongWait = WebDriverWait(driver, 240)


def sendWaConfirmation(data):
    """
    This function will submit message to Whatsapp
    :param x: object 'to' and 'msg'
    :return: Success
    """
    key = {"to": [str(data['to'])], "msg": data['msg']}
    result = requests.post(urlWhatsapp, json=key)
    return result.text

def loginFirst():
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'auth-form-container')))
    driver.find_element_by_id('email').send_keys('uploader@pinhome.id')
    driver.find_element_by_id('password').send_keys('Data-entry2021#')
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[3]/div/div/form/div[3]/button').click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ant-message')))
    waitLoading()

def getData(pic_name, squad):
    req = requests.get(f"{url}squad={squad.lower()}&user={pic_name.lower()}")
    result = req.json()
    return result

def updateDataResult(squad,id,user):
    req = requests.post(f"{url}&squad={squad.lower()}&id={id}&user={user.lower()}")
    print(f"{id} : Success!")

def waitLoading():
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'fetching')))

        LongWait.until_not(EC.presence_of_element_located((By.CLASS_NAME, 'fetching')))

    except TimeoutException:
        pass 

    sleep(1)

def inputHarga(data):
    price = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[17]/div/div/div[1]/div/div[2]/div/input'
    wait.until(EC.presence_of_element_located((By.XPATH, price)))
    sleep(2)
    driver.find_element_by_xpath(price).send_keys(data)

def inputDesc(data):
    desc = '//*[@id="selectDescription"]/div/div[2]/div[1]'
    driver.find_element_by_xpath(desc).send_keys(data)

def inputTipeListing(data):
    tipe_listing = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[9]/div/div/div[1]/div/div[2]/div/div[1]/div/div'
    driver.find_element_by_xpath(tipe_listing).click()

    tipe_listing = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[9]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/input'
    driver.find_element_by_xpath(tipe_listing).click()
    driver.find_element_by_xpath(tipe_listing).send_keys(data)
    sleep(3)
    driver.find_element_by_xpath(tipe_listing).send_keys(Keys.RETURN)
    sleep(1)


def inputTipeProperti(data):
    tipe_properti = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[11]/div/div/div[1]/div/div[2]/div/div[1]/div/div')))
    tipe_properti.click()

    tipe_properti = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[11]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/input'
    driver.find_element_by_xpath(tipe_properti).send_keys(data)
    sleep(1)
    driver.find_element_by_xpath(tipe_properti).send_keys(Keys.RETURN)

def inputTipeBangunan(data):
    tipe_bangunan = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[12]/div/div/div[1]/div/div[2]/div/div/div/div'
    driver.find_element_by_xpath(tipe_bangunan).click()

    tipe_bangunan = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[12]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/input'
    driver.find_element_by_xpath(tipe_bangunan).send_keys(data)
    sleep(1)
    driver.find_element_by_xpath(tipe_bangunan).send_keys(Keys.RETURN)
    sleep(1)

def inputMetodePembayaranJual():
    metode_pembayaran = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[14]/div/div/div[1]/div/div[2]/div/div[1]/div/div')))
    metode_pembayaran.click()

    metode_pembayaran = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[14]/div/div/div[1]/div/div[2]/div/div[1]/div/div/ul/li/div/input'
    driver.find_element_by_xpath(metode_pembayaran).send_keys(Keys.RETURN)
    sleep(0.5)
    driver.find_element_by_xpath(metode_pembayaran).send_keys(Keys.DOWN)
    driver.find_element_by_xpath(metode_pembayaran).send_keys(Keys.RETURN)
    sleep(0.5)
    driver.find_element_by_xpath(metode_pembayaran).send_keys(Keys.DOWN)
    driver.find_element_by_xpath(metode_pembayaran).send_keys(Keys.RETURN)

def inputMetodePembayaranSewa():
    metode_pembayaran = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[14]/div/div/div[1]/div/div[2]/div/div[1]/div/div')))
    metode_pembayaran.click()

    metode_pembayaran = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[14]/div/div/div[1]/div/div[2]/div/div[1]/div/div/ul/li/div/input'
    driver.find_element_by_xpath(metode_pembayaran).send_keys(Keys.DOWN)
    driver.find_element_by_xpath(metode_pembayaran).send_keys(Keys.RETURN)
    sleep(0.5)

def inputProvince(data):
    province = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[4]/div/div/div[1]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div'
    driver.find_element_by_xpath(province).click()

    province = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[4]/div/div/div[1]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/input'
    driver.find_element_by_xpath(province).send_keys(data)
    sleep(0.5)
    driver.find_element_by_xpath(province).send_keys(Keys.RETURN)

def inputCity(data):
    city = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[4]/div/div/div[1]/div/div/div/div[5]/div/div/div[1]/div/div[2]/div/div[1]/div/div'
    driver.find_element_by_xpath(city).click()

    city= '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[4]/div/div/div[1]/div/div/div/div[5]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/input'
    driver.find_element_by_xpath(city).send_keys(data)
    sleep(0.5)
    driver.find_element_by_xpath(city).send_keys(Keys.RETURN)

def inputDistrict(data):
    district = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[4]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div/div'
    driver.find_element_by_xpath(district).click()

    district = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[4]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/input'
    driver.find_element_by_xpath(district).send_keys(data)
    sleep(0.5)
    driver.find_element_by_xpath(district).send_keys(Keys.RETURN)

def inputStreetName(data):
    street = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[4]/div/div/div[1]/div/div/div/div[9]/div/div/div[1]/div/div[2]/div/span/input'
    driver.find_element_by_xpath(street).send_keys(data)

def inputCertificate(data):
    sertifikat = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[6]/div/div/div[1]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div'
    driver.find_element_by_xpath(sertifikat).click()


    sertifikat = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[6]/div/div/div[1]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/input'
    driver.find_element_by_xpath(sertifikat).send_keys(data)
    sleep(0.5)
    driver.find_element_by_xpath(sertifikat).send_keys(Keys.RETURN)

def inputPerabot(data):
    perabot = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[6]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div/div'
    driver.find_element_by_xpath(perabot).click()

    perabot = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[6]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/input'
    driver.find_element_by_xpath(perabot).send_keys(data)
    sleep(0.5)
    driver.find_element_by_xpath(perabot).send_keys(Keys.RETURN)

def inputListrik(data):
    listrik = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[6]/div/div/div[1]/div/div/div/div[6]/div/div/div[1]/div/div[2]/div/div/div/div'
    driver.find_element_by_xpath(listrik).click()

    listrik = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[6]/div/div/div[1]/div/div/div/div[6]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/input'
    driver.find_element_by_xpath(listrik).send_keys(data)
    sleep(0.5)
    driver.find_element_by_xpath(listrik).send_keys(Keys.RETURN)

def inputLuasBangunan(data):
    luas_bangunan = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[6]/div/div/div[1]/div/div/div/div[8]/div/div/div[1]/div/div[2]/div/span/input'
    driver.find_element_by_xpath(luas_bangunan).send_keys(data)

def inputLuasTanah(data):
    luas_tanah = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[6]/div/div/div[1]/div/div/div/div[13]/div/div/div[1]/div/div[2]/div/span/input'
    driver.find_element_by_xpath(luas_tanah).send_keys(data)

def inputLantai(data):
    lantai = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[6]/div/div/div[1]/div/div/div/div[9]/div/div/div[1]/div/div[2]/div/input'
    driver.find_element_by_xpath(lantai).send_keys(data)

def inputBedroom(data):
    berdoom = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[6]/div/div/div[1]/div/div/div/div[17]/div/div/div[1]/div/div[2]/div/input'
    driver.find_element_by_xpath(berdoom).send_keys(data)

def inputToilet(data):
    toilet = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[6]/div/div/div[1]/div/div/div/div[18]/div/div/div[1]/div/div[2]/div/input'
    driver.find_element_by_xpath(toilet).send_keys(data)


def agentTab(ag_komisi, ag_number):
    agent_tab = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[1]/div/div/div/div/div[1]/div[2]'
    driver.find_element_by_xpath(agent_tab).click()
    sleep(1)

    komisi = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div[2]/div/span/input'
    driver.find_element_by_xpath(komisi).send_keys(str(ag_komisi))

    agent_listing = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div'
    driver.find_element_by_xpath(agent_listing).click()

    agent_listing = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[3]/div/input'
    driver.find_element_by_xpath(agent_listing).send_keys('Agen Pinhome')
    driver.find_element_by_xpath(agent_listing).send_keys(Keys.DOWN)
    sleep(2)
    driver.find_element_by_xpath(agent_listing).send_keys(Keys.RETURN)

    agent_number = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div'
    driver.find_element_by_xpath(agent_number).click()

    agent_number = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/input'
    driver.find_element_by_xpath(agent_number).send_keys(ag_number)
    sleep(2)
    driver.find_element_by_xpath(agent_number).send_keys(Keys.RETURN)

def photoTab():
    foto_tab = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[1]/div/div/div/div/div[1]/div[3]'
    driver.find_element_by_xpath(foto_tab).click()

def detailsTab():
    details = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[1]/div/div/div/div/div[1]/div[1]'
    driver.find_element_by_xpath(details).click()
    sleep(5)

def inputPhotoData(data, building_type):

    for root, dirs, files in os.walk(f'./Listing Photos/{data}'):
        path = os.path.abspath(os.getcwd())
        fixed_path = path.replace('\\', '/')
        combined = ""
        allFiles = []
        for filename in files:
            photo = f"{fixed_path}/Listing Photos/{data}/{filename} \n "
            combined += photo
            allFiles.append(filename[0])

    file_path = combined[:-3]

    photoUpload = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[3]/div/div/div[1]/div/div/span/div/span/input')))
    photoUpload.send_keys(file_path)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div')))
    sleep(3)
    selectPhotoDataCategories(allFiles, building_type)



def selectPhotoDataCategories(list_file, building_type):
    photo_obj = {
        "rumah": [
            {
                "no": 1,
                "category": "Tampak Depan"
            },
            {
                "no": 2,
                "category": "Ruang Tamu"
            },
            {
                "no": 3,
                "category": "Lainnya"
            },
            {
                "no": 4,
                "category": "Lainnya"
            },
            {
                "no": 5,
                "category": "Lainnya"
            },
        ],
        "apartemen": [
            {
                "no": 1,
                "category": "Ruang Tamu"
            },
            {
                "no": 2,
                "category": "Ruang Tamu"
            },
            {
                "no": 3,
                "category": "Kamar Tidur"
            },
            {
                "no": 4,
                "category": "Lainnya"
            },
            {
                "no": 5,
                "category": "Lainnya"
            },
        ],
        "ruko": [
            {
                "no": 1,
                "category": "Tampak Depan"
            },
            {
                "no": 2,
                "category": "Tampak Depan"
            },
            {
                "no": 3,
                "category": "Lainnya"
            },
            {
                "no": 4,
                "category": "Lainnya"
            },
            {
                "no": 5,
                "category": "Lainnya"
            },
        ],
        "xpath":[
            {
                "no": 1,
                "click": '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div/div/div/div/div',
                "input": '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div/div/div/div/div/div[2]/div/input'
            },
            {
                "no": 2,
                "click": '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div',
                "input": '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/input'
            },
            {
                "no": 3,
                "click": '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/div[1]/div[2]/div[3]/div/div[3]/div/div/div/div/div',
                "input": '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/div[1]/div[2]/div[3]/div/div[3]/div/div/div/div/div/div[2]/div/input'
            },
            {
                "no": 4,
                "click": '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/div[1]/div[2]/div[4]/div/div[3]/div/div/div/div/div',
                "input": '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/div[1]/div[2]/div[4]/div/div[3]/div/div/div/div/div/div[2]/div/input'
            },
            {
                "no": 5,
                "click": '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/div[1]/div[2]/div[5]/div/div[3]/div/div/div/div/div',
                "input": '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div/div/div/div[1]/div[2]/div[5]/div/div[3]/div/div/div/div/div/div[2]/div/input'
            },
        ]
    }


    for i in range(len(list_file)):
        category_photo = photo_obj[building_type.lower()][int(list_file[i])-1]['category']
        clickDiv = photo_obj['xpath'][i]['click']
        inputDiv = photo_obj['xpath'][i]['input']


        inputPhotoCategory(clickDiv,inputDiv,category_photo)

    sleep(3)
    savePhotoCategory()

    


def inputPhotoCategory(click,input,category):
    photo = wait.until(EC.presence_of_element_located((By.XPATH, click)))
    photo.click()

    driver.find_element_by_xpath(input).send_keys(category)
    sleep(0.5)
    driver.find_element_by_xpath(input).send_keys(Keys.RETURN)
    sleep(2)


def savePhotoCategory():
    save = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="table-tablePhotos"]/div/div/div/div[2]/div/div/button[2]')))
    save.click()
    wait.until_not(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="table-tablePhotos"]/div/div/div/div[2]/div/div/button[2]')))
    sleep(3)
    

def submitListing(data):
    save = '//div[@class="_124-M _retool-buttonSubmit"]/div/button'
    driver.find_element_by_xpath(save).click()
    sleep(2)

    inputPic = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="_124-M _retool-textinputPicName"]/div/div[2]/div/span/input')))
    sleep(3)
    inputPic.send_keys(data)

    submitPic = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="_124-M _retool-buttonModalPICConfirm"]/div/button[@class="ant-btn ant-btn-primary"]'))) 
    sleep(1)
    submitPic.click()
    
    submitData =  wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="ant-modal-confirm-body-wrapper"]/div[2]/button[2]')))
    sleep(2)
    submitData.click()
    
    
def defaultValue():
    status_ketersediaan = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div'
    driver.find_element_by_xpath(status_ketersediaan).click()
    status_ketersediaan = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/input'
    driver.find_element_by_xpath(status_ketersediaan).send_keys('Active')
    driver.find_element_by_xpath(status_ketersediaan).send_keys(Keys.RETURN)

    verified = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[4]/div/div/div[1]/div/div[2]/div/button[1]'
    driver.find_element_by_xpath(verified).click()

    tipe_pasar = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[8]/div/div/div[1]/div/div[2]/div/div[1]/div/div'
    driver.find_element_by_xpath(tipe_pasar).click()
    tipe_pasar = '//*[@id="root"]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div/div/div[6]/div/div/div/div/div[3]/div[1]/div[2]/div/div[21]/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[8]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/input'
    driver.find_element_by_xpath(tipe_pasar).send_keys('Seken')
    driver.find_element_by_xpath(tipe_pasar).send_keys(Keys.RETURN)

def createFolder(data):
    if not os.path.exists("Listing Photos"):
        os.makedirs("Listing Photos")
    if not os.path.exists(f"Listing Photos/{data}"):
        os.makedirs(f"Listing Photos/{data}")




#Main Function
def jualRumah(result):
    
    inputHarga(result['minimum_sell'])
    defaultValue()
    inputTipeListing(result['listing_type'])
    inputTipeProperti(result['market_type'])
    waitLoading()
    sleep(3)
    inputTipeBangunan(result['building_type'])
    waitLoading()
    sleep(1)
    inputMetodePembayaranJual()
    sleep(1)
    inputProvince(result['province'])
    waitLoading()
    inputCity(result['city'])
    waitLoading()
    inputDistrict(result['district'])
    waitLoading()
    inputStreetName(result['street_name'])
    inputCertificate(result['unit_certification'])
    inputPerabot(result['furniture_status'])
    inputListrik(result['listrik'])
    inputLuasBangunan(result['luas_bangunan'])
    inputLuasTanah(result['luas_tanah'])
    inputLantai(result['jumlah_lantai'])
    inputBedroom(result['kamar_tidur'])
    inputToilet(result['kamar_mandi'])
    inputDesc(result['description'])
    agentTab(result['komisi'], result['agent_number'])
    photoTab()
    inputPhotoData(result['listing_id'], result['building_type'])
    submitListing(uploader_name)
    updateDataResult(squad,result['listing_id'],uploader_name)
    waitLoading()
    detailsTab()

def sewaRumah(result):
    inputHarga(result['minimum_rent'])
    defaultValue()
    inputTipeListing(result['listing_type'])
    inputTipeProperti(result['market_type'])
    waitLoading()
    sleep(3)
    inputTipeBangunan(result['building_type'])
    waitLoading()
    sleep(1)
    inputMetodePembayaranSewa()
    sleep(1)
    inputProvince(result['province'])
    waitLoading()
    sleep(1)
    inputCity(result['city'])
    waitLoading()
    sleep(1)
    inputDistrict(result['district'])
    waitLoading()
    sleep(1)
    inputStreetName(result['street_name'])
    inputPerabot(result['furniture_status'])
    inputListrik(result['listrik'])
    inputLuasBangunan(result['luas_bangunan'])
    inputLuasTanah(result['luas_tanah'])
    inputLantai(result['jumlah_lantai'])
    inputBedroom(result['kamar_tidur'])
    inputToilet(result['kamar_mandi'])
    inputDesc(result['description'])
    agentTab(result['komisi'], result['agent_number'])
    photoTab()
    inputPhotoData(result['listing_id'], result['building_type'])
    submitListing(uploader_name)
    updateDataResult(squad,result['listing_id'],uploader_name)
    waitLoading()
    detailsTab()

def jualApartemen(result):
    inputHarga(result['minimum_sell'])
    defaultValue()
    inputTipeListing(result['listing_type'])
    inputTipeProperti(result['market_type'])
    waitLoading()
    sleep(3)
    inputTipeBangunan(result['building_type'])
    waitLoading()
    sleep(1)
    inputMetodePembayaranJual()
    sleep(1)
    inputProvince(result['province'])
    waitLoading()
    inputCity(result['city'])
    waitLoading()
    inputDistrict(result['district'])
    waitLoading()
    inputStreetName(result['street_name'])
    inputCertificate(result['unit_certification'])
    inputPerabot(result['furniture_status'])
    inputListrik(result['listrik'])
    inputLuasBangunan(result['luas_bangunan'])
    inputBedroom(result['kamar_tidur'])
    inputToilet(result['kamar_mandi'])
    inputDesc(result['description'])
    agentTab(result['komisi'], result['agent_number'])
    photoTab()
    inputPhotoData(result['listing_id'], result['building_type'])
    submitListing(uploader_name)
    updateDataResult(squad,result['listing_id'],uploader_name)
    waitLoading()
    detailsTab()

def sewaApartemen(result):
    inputHarga(result['minimum_rent'])
    defaultValue()
    inputTipeListing(result['listing_type'])
    inputTipeProperti(result['market_type'])
    waitLoading()
    sleep(3)
    inputTipeBangunan(result['building_type'])
    waitLoading()
    sleep(1)
    inputMetodePembayaranSewa()
    sleep(1)
    inputProvince(result['province'])
    waitLoading()
    inputCity(result['city'])
    waitLoading()
    inputDistrict(result['district'])
    waitLoading()
    inputStreetName(result['street_name'])
    inputPerabot(result['furniture_status'])
    inputListrik(result['listrik'])
    inputLuasBangunan(result['luas_bangunan'])
    inputBedroom(result['kamar_tidur'])
    inputToilet(result['kamar_mandi'])
    inputDesc(result['description'])
    agentTab(result['komisi'], result['agent_number'])
    photoTab()
    inputPhotoData(result['listing_id'], result['building_type'])
    submitListing(uploader_name)
    updateDataResult(squad,result['listing_id'],uploader_name)
    waitLoading()
    detailsTab()

def jualRuko(result):
    inputHarga(result['minimum_sell'])
    defaultValue()
    inputTipeListing(result['listing_type'])
    inputTipeProperti(result['market_type'])
    waitLoading()
    sleep(3)
    inputTipeBangunan(result['building_type'])
    waitLoading()
    sleep(1)
    inputMetodePembayaranJual()
    sleep(1)
    inputProvince(result['province'])
    waitLoading()
    inputCity(result['city'])
    waitLoading()
    inputDistrict(result['district'])
    waitLoading()
    inputStreetName(result['street_name'])
    inputCertificate(result['unit_certification'])
    inputPerabot(result['furniture_status'])
    inputListrik(result['listrik'])
    inputLuasBangunan(result['luas_bangunan'])
    inputLuasTanah(result['luas_tanah'])
    inputLantai(result['jumlah_lantai'])
    inputToilet(result['kamar_mandi'])
    inputDesc(result['description'])
    agentTab(result['komisi'], result['agent_number'])
    photoTab()
    inputPhotoData(result['listing_id'], result['building_type'])
    submitListing(uploader_name)
    updateDataResult(squad,result['listing_id'],uploader_name)
    waitLoading()
    detailsTab()

def sewaRuko(result):
    inputHarga(result['minimum_rent'])
    defaultValue()
    inputTipeListing(result['listing_type'])
    inputTipeProperti(result['market_type'])
    waitLoading()
    sleep(3)
    inputTipeBangunan(result['building_type'])
    waitLoading()
    sleep(1)
    inputMetodePembayaranSewa()
    sleep(1)
    inputProvince(result['province'])
    waitLoading()
    inputCity(result['city'])
    waitLoading()
    inputDistrict(result['district'])
    waitLoading()
    inputStreetName(result['street_name'])
    inputPerabot(result['furniture_status'])
    inputListrik(result['listrik'])
    inputLuasBangunan(result['luas_bangunan'])
    inputLuasTanah(result['luas_tanah'])
    inputLantai(result['jumlah_lantai'])
    inputToilet(result['kamar_mandi'])
    inputDesc(result['description'])
    agentTab(result['komisi'], result['agent_number'])
    photoTab()
    inputPhotoData(result['listing_id'], result['building_type'])
    submitListing(uploader_name)
    updateDataResult(squad,result['listing_id'],uploader_name)
    waitLoading()
    detailsTab()


def clasificationLoop(data_list):
    for data in data_list:
        if data['listing_type'] == 'Jual' or data['listing_type'] ==  'Jual dan Sewa':
            data['listing_type'] = 'Beli'

        if data['building_type'].lower() == 'rumah' and data['listing_type'].lower() == 'beli':
            jualRumah(data)
        elif data['building_type'].lower() == 'rumah' and data['listing_type'].lower() == 'sewa':
            sewaRumah(data)
        elif data['building_type'].lower() == 'apartemen' and data['listing_type'].lower() == 'beli':
            jualApartemen(data)
        elif data['building_type'].lower() == 'apartemen' and data['listing_type'].lower() == 'sewa':
            sewaApartemen(data)
        elif data['building_type'].lower() == 'ruko' and data['listing_type'].lower() == 'beli':
            jualRuko(data)
        elif data['building_type'].lower() == 'ruko' and data['listing_type'].lower() == 'sewa':
            sewaRuko(data)
    driver.quit()
