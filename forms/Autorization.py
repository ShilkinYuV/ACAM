
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSettings
from ui.Autorization import Ui_MainWindow
from forms.MainForm import MainForm
import sys


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from libs.ConnectionDB import ConnectionDB
from libs.send_to_mail import SendMail



class Autorization(QtWidgets.QMainWindow):

    def __init__(self) -> None:
        super(Autorization, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.get_autorization_data)
        connectionDB = ConnectionDB()
        # connectionDB.select_all()
        self.first_connection = True
        # self.mail = SendMail()
        # self.mail.send_email('test message', 'ShilkinYuV@fsfk.local', 'ShilkinYuV@fsfk.local', 'This is BODY')
        # self.mail.send_email('number', 'request_type', 'registration_date', 'service', 'component', 'service_recipient','location')
        self.filter1 = None
        self.filter2 = None
        self.filter3 = None
        self.mail_sender = None
        self.pass_sender = None
        self.mail_group_one = None
        self.mail_group_two = None

        
    
    def get_autorization_data(self):
        try:
            self.filter1 = self.ui.lineEdit_3.text()
            self.filter2 = self.ui.lineEdit_4.text()
            self.filter3 = self.ui.lineEdit_5.text()
            self.mail_sender = self.ui.lineEdit_6.text()
            self.pass_sender = self.ui.lineEdit_7.text()
            self.mail_group_one = self.ui.lineEdit_8.text()
            self.mail_group_two = self.ui.lineEdit_9.text()
            
            if(self.filter1 != None and self.filter2 != None and self.filter3 != None and self.mail_sender != None
            and self.pass_sender != None and self.mail_group_one != None and self.mail_group_two != None):                   
                self.options = Options()
                self.options.add_argument("--headless")
                self.driver = webdriver.Chrome()
                self.driver.maximize_window()
                self.driver.implicitly_wait(6)
                            
                self.username = self.ui.lineEdit.text()
                self.password = self.ui.lineEdit_2.text()

                # перейти на страницу входа
                self.driver.get("http://ShilkinYuV:!29Ofebov@@sm-sue.fsfk.local/sd/operator/?anchor=")
                time.sleep(1)
                # найти поле имени пользователя / электронной почты и отправить само имя пользователя в поле ввода
                self.driver.find_element(By.NAME, value="username").send_keys(self.username)
                # найти поле ввода пароля и также вставить пароль
                self.driver.find_element(By.NAME, value="password").send_keys(self.password)
                # нажмите кнопку входа в систему
                self.driver.find_element(By.CLASS_NAME, value="submit-button").click()

                self.driver.add_cookie({'name':  self.username, 'value': self.password, 'path': '/'})
                time.sleep(2)
                
                # ждем завершения состояния готовности
                WebDriverWait(driver=self.driver, timeout=10).until(
                    lambda x: x.execute_script("return document.readyState === 'complete'")
                )
                error_message = "Incorrect username or password."
                # получаем ошибки (если есть)
                errors = self.driver.find_elements(By.CLASS_NAME, value="flash-error")
                # при необходимости распечатать ошибки
                # для e в ошибках:
                #     print(e.text)
                # если мы находим это сообщение об ошибке в составе error, значит вход не выполнен
                if any(error_message in e.text for e in errors):
                    print("[!] Login failed")
                else:
                    # print("[+] Login successful")
                    self.openMainForm()
        except Exception:
            time.speep(600)
            self.get_autorization_data(self) 
        

    def openMainForm(self):      
        self.mainForm = MainForm(my_window=self) 
        self.mainForm.show()
        self.hide()
