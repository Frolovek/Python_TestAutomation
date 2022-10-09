from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    maximum = max(inp, key=inp.count)
    minimum = min(inp, key=inp.count)
    return maximum, minimum