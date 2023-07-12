from pyhealth.calculations.calculate import calculate_bmi


if __name__ == '__main__':
    heights = [1.75, 1.65, 1.80]
    weights = [80, 55, 95.2]

    bmis = calculate_bmi(heights, weights)
    print(bmis)
