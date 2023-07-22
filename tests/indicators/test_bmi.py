from pyhealth.indicators.health import bmi

def test_bmi_ok():
    assert bmi(2, 100) == 25

def test_bmi_height_zero():
    assert not bmi(0, 100)
