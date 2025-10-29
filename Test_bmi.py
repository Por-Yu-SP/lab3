import bmi.bmi as mass

def test_bmi_normal_weight():
    result=10
    test=0
    height=1.7
    weight=60
    result=mass.calculate_bmi(height,weight)
    assert (result==test)

def test_bmi_over_weight():
    result=10
    test=1
    height=1.4
    weight=90
    result=mass.calculate_bmi(height,weight)
    assert (result==test)
    
def test_bmi_under_weight():
    result=10
    test=-1
    height=1.8
    weight=40
    result=mass.calculate_bmi(height,weight)
    assert (result==test)
    