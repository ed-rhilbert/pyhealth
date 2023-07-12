from pyhealth.calculations.calculate import calculate_bmi


def test_calculate_bmi_type():
    heights = [1, 2]
    weights = [50, 100]

    assert isinstance(calculate_bmi(heights, weights), list)


def test_calculate_bmi_values():
    heights = [1, 2]
    weights = [50, 100]

    assert calculate_bmi(heights, weights) == [50, 25]
