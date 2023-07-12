from typing import List

from pyhealth.indicators.health import bmi


def calculate_bmi(heights: List[float], weights: List[float]) -> List[float]:
    """Calculate bmis for lists of heights and weights

    Parameters
    ----------
    heights : List[float]
        List of heights in m
    weights : List[float]
        List of weights in kg

    Returns
    -------
    List[float]
       List of BMIs = weight/(height**2)
    """
    bmis = []
    for i in range(0, len(heights)):
        bmis.append(bmi(heights[i], weights[i]))
    return bmis
