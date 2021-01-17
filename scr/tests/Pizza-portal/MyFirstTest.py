#используем функции только из тест темплейтс
#сдесь мы закрываем хром драйвер
#можем сдесь хрань идентификаторы теста
#можно использовать дикораторы(но не обязательно)
#файл запускаем пайтестом идинтификатор,название теста и результат



#from scr.main.testtemplates.FlowName1 import pepperoniCheckFlow
#from scr.main.testtemplates.FlowName2 import FirstSitePage
#from scr.driver.chromedriver import Driver_method
import pytest




@pytest.fixture
def error_fixture():
    assert 0


def test_ok():
    print("ok")


def test_fail():
    assert 0


#pepperoniCheckFlow()
#FirstSitePage()

#Driver_method().close_webdriver()

