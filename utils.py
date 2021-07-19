import math
from typing import Union, Tuple


def rct2pol(cn: complex) -> Tuple[float, float]:
    x = cn.real
    y = cn.imag
    rho = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x)
    return rho, theta


def pol2rct(rho: Union[int, float], theta: Union[int, float]) -> complex:
    x = rho * math.cos(theta)
    y = rho * math.sin(theta)
    return complex(x, y)


def str_exp(cn: complex) -> str:
    rho, theta = rct2pol(cn)
    return f'{rho}*e^({theta}i)'


def str_pol(cn: complex) -> str:
    rho, theta = rct2pol(cn)
    return f'{rho}*(cos({theta})+i*sin({theta}))'


def str_rect(cn: complex, explicit: bool = True) -> str:
    if not explicit and not round(cn.imag, 10):
        cn = round(cn.real, 10)
        if cn == int(cn):
            cn = int(cn)
    else:
        cn = complex(round(cn.real, 10), round(cn.imag, 10))
    return str(cn).strip('()').replace('j', 'i')


def to_complex(text: str) -> complex:
    from math import sin as sjn, cos
    j = 1j
    text = text.replace('i', 'j').replace('^', '**').replace('e', f'{math.e}')
    try:
        return eval(text)
    except Exception as ex:
        return None


if __name__ == '__main__':
    while True:
        raw = input()
        num = to_complex(raw)
        print(num)
        print(str_pol(num))
        print(str_exp(num))
