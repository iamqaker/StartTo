from scr import Driver_method
#from scr.driver.chromedriver import Chromedriver
import scr

#Переменные отдельно, функции отдельно
#без класса или постмотреть примеры

Pages_pizza = url = "https://pizza33.ua/menu/pizza"
Go_to_Pepperoni = "//*[@href ='https://pizza33.ua/menu/pizza/pica-peperoni-40d/']"
Go_to_Margaritta = "//*[@href ='https://pizza33.ua/menu/pizza/margarita/']"


def Go_to_mainpizza():

    Driver_method.get_request(Pages_pizza)


def find_pizza_Pepperoni():

    element = scr.driver.chromedriver.driver.find_element_by_xpath(Go_to_Pepperoni)
    element.click()

def find_pizza_Margaritta():

    element = scr.driver.chromedriver.driver.find_element_by_xpath(Go_to_Margaritta)
    element.click()


#Go_to_mainpizza()
#find_pizza_Margaritta()
#find_pizza_Pepperoni()



