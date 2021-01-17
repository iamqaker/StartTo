from scr.main.testtemplates.FlowName1 import notknow





def test_ok():
    print("ok")


def test_fail():
    notknow.flow()


test_fail()