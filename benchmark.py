import timeit
from function_sorted import is_sorted

"""erstellung große sortierte liste"""
sorted_list = list(range(1000000))

"""erstellung große unsortierte liste"""
unsorted_list = list(range(1000000, 0, -1))

"""zeit verbracht bei jeder liste """
time_sorted = timeit.timeit(lambda: is_sorted(sorted_list), number=1)
time_unsorted = timeit.timeit(lambda: is_sorted(unsorted_list), number=1)


"""ergebnisse ausgeben"""
print(f"zeit für sortierte liste: {time_sorted:.6f} sekunden")
print(f"zeit für unsortierte liste: {time_unsorted:.6f} sekunden")
