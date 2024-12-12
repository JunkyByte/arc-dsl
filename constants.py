from typing import Tuple as _Tuple
from arc_types import Integer as _Integer

F = False
T = True

ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10

NEG_ONE = -1
NEG_TWO = -2

DOWN: _Tuple[_Integer, _Integer] = (1, 0)
RIGHT: _Tuple[_Integer, _Integer] = (0, 1)
UP: _Tuple[_Integer, _Integer] = (-1, 0)
LEFT: _Tuple[_Integer, _Integer] = (0, -1)

ORIGIN: _Tuple[_Integer, _Integer] = (0, 0)
UNITY: _Tuple[_Integer, _Integer] = (1, 1)
NEG_UNITY: _Tuple[_Integer, _Integer] = (-1, -1)
UP_RIGHT: _Tuple[_Integer, _Integer] = (-1, 1)
DOWN_LEFT: _Tuple[_Integer, _Integer] = (1, -1)

ZERO_BY_TWO: _Tuple[_Integer, _Integer] = (0, 2)
TWO_BY_ZERO: _Tuple[_Integer, _Integer] = (2, 0)
TWO_BY_TWO: _Tuple[_Integer, _Integer] = (2, 2)
THREE_BY_THREE: _Tuple[_Integer, _Integer] = (3, 3)