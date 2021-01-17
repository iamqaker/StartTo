import pytest
from scr.main.testtemplates.FlowName1 import pepperoniCheckFlow

@pytest.fixture
def error_fixture():
    assert 0


def test_ok():
    print("ok")


def test_fail():
    pepperoniCheckFlow()
    assert 0
#gidhub

#ИМПОРТ ПАЙТЕСТ НАЙТИ ПРОЕК ИЗ РЕАЛЬНОЙ ЖИЗНИ И КАК ПРАВА В ПАПКАХ
