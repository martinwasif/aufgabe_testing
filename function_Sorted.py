from typing import List
"""funktion überprüft das alle werten in der liste in aufsteigend reihe sind """
def is_sorted(lst: List[int])-> bool :
    for i in range(len(lst)-1):
        if lst[i]> lst[i+1]:
            return False
    return True
