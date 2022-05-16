from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Github credentials
username = "ShilkinYuV"
password = "!29Ofebov@"

# initialize the Chrome driver
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

# перейти на страницу входа
driver.get("http://ShilkinYuV:!29Ofebov@@sm-sue.fsfk.local/sd/operator/?anchor=")
time.sleep(1)
# найти поле имени пользователя / электронной почты и отправить само имя пользователя в поле ввода
driver.find_element(By.NAME, value="username").send_keys(username)
# найти поле ввода пароля и также вставить пароль
driver.find_element(By.NAME, value="password").send_keys(password)
# нажмите кнопку входа в систему
driver.find_element(By.CLASS_NAME, value="submit-button").click()

driver.add_cookie({'name': 'ShilkinYuV', 'value': '!29Ofebov@', 'path': '/'})
time.sleep(2)
driver.get("http://sm-sue.fsfk.local/sd/operator/#uuid:employee$49321051!%7B%22tab%22:%22b661b970-470d-404c-14f6-1144fae3f071,6d426ec2-fb00-edd9-7519-697065c94cf9%22%7D")

# ждем завершения состояния готовности
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# получаем ошибки (если есть)
errors = driver.find_elements(By.CLASS_NAME, value="flash-error")
# при необходимости распечатать ошибки
# для e в ошибках:
#     print(e.text)
# если мы находим это сообщение об ошибке в составе error, значит вход не выполнен
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")
    driver.find_element(By.ID, value="gwt-debug-AdvlistPrsSelectTool.f544db61-174b-675b-008b-00005c7fef0d").click()
    time.sleep(2)
    driver.find_element(By.ID, value="1211840402").click()
    time.sleep(1)
    driver.find_element(By.ID, value="gwt-debug-exportAdvlist.f83c557b-1703-ca38-0386-00007da9d7e6").click()

    time.sleep(2)
    driver.find_element(By.ID, value="gwt-debug-AdvlistPrsSelectTool.f544db61-174b-675b-008b-00005c7fef0d").click()
    time.sleep(2)
    driver.find_element(By.ID, value="1211840401").click()
    time.sleep(1)
    driver.find_element(By.ID, value="gwt-debug-exportAdvlist.f83c557b-1703-ca38-0386-00007da9d7e6").click()
  

    # items = driver.find_elements(By.TAG_NAME, value="div")
    # for item in items:
    #     text = item.text
    #     print(text)

    
