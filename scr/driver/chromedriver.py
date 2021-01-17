from selenium import webdriver
import unittest

#Не вызываем никаких функции сдесь.(Сделал)
#Опционально можно сделать отдельно конфигурацию веб-драйвера и отдельно методы в разный классах.(Сделано)
#Сделать все по PEP 8, отформатировать код.
#Изменить размен Хромдрайвера(который я укажу)(Cделал)

#Chrome driver config

PATH = r"C:\Users\vladislav\PycharmProjects\pythonProject\scr\driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

class Chromedriver():

    #global driver

    def size():

        #PATH = r"C:\Users\vladislav\PycharmProjects\pythonProject\scr\driver\chromedriver.exe"
        #driver = webdriver.Chrome(PATH)
        #self.driver = driver
        driver.set_window_size(800, 600,
        driver.window_handles[0])



class Driver_method:


    def get_request(url):

        driver.get(url)



    def close_webdriver(self):

        driver.close()


    #def find_Pizza(self,Pizza):

        #element = driver.find_element(Pizza)
        #element.click()



#Chromedriver().size()
#Driver_method().get_request()
#Driver_method().close_webdriver()