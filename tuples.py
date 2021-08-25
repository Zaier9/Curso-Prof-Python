from typing import Tuple

numbers: Tuple[int, float, int] = (1, 0.5, 2)


==================================================================

from typing import Tuple, Dict, List

CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
    {
        'coord1': (1,2),
        'coord2': (3,4)
    },
    {
        'coord1': (5,6),
        'coord2': (7,8)
    },
]
