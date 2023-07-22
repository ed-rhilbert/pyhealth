from typing import Union

def bmi(height: float, weight: float) -> Union[float, None]:
    """Calculate BMI (Body Mass Index)

    bmi = weight [kg] / (height [m])^2

    Parameters
    ----------
    weight : float
        weight in kg
    height : float
        height in m

    Returns
    -------
    Union[float, None]
        Body Mass Index or None if height == 0

    Examples
    --------
    >>> bmi(70, 1.8)
    21.604938271604937

    >>> bmi(70, 0)
    None
    """
    if height != 0:
        return (weight/height**2) if height > 0 and weight > 0 else None