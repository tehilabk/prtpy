from typing import Callable, List, Any
from prtpy import outputtypes as out, Bins, BinsKeepingContents
from prtpy.packing import first_fit
import math


def l2_lower_bound(binsize: float, items: List) -> float:
    print(items)
    print(sum(items))

    items.sort(reverse=True)

    total_sum = sum(items)
    estimated_waste = 0
    capacity = binsize

    for x in items:
        r = capacity - x
        smaller_elements = []
        for i in range(len(items) - 1, items.index(x), -1):
            if (items[i] > r):
                break
            smaller_elements.append(items[i])

        s = sum(smaller_elements)
        if s == r:
            for element in smaller_elements:
                items.remove(element)
            # items.remove(element for element in smaller_elements)
            capacity = binsize
        elif s < r:
            estimated_waste += r - s
            for element in smaller_elements:
                items.remove(element)
            # items.remove(element for element in smaller_elements)
            capacity = binsize
        else:
            for element in smaller_elements:
                items.remove(element)
            # items.remove(element for element in smaller_elements)
            capacity = binsize - (s - r)
    print(estimated_waste)
    return (estimated_waste + total_sum) / binsize


def bin_completion(
        bins: Bins,
        binsize: float,
        items: List[any],
        valueof: Callable[[Any], float] = lambda x: x
) -> Bins:
    """
    "A New Algorithm for Optimal Bin Packing", by Richard E. Korf (2002) https://www.aaai.org/Papers/AAAI/2002/AAAI02-110.pdf
    Algorithm: Given a set of numbers, and a set of bins of fixed capacity,
    the algorithm finds the minimum number of bins needed to contain all the numbers,
    such that the sum of the numbers assigned to each bin does not exceed the bin capacity.

    >>> from prtpy.bins import BinsKeepingContents, BinsKeepingSums

    Example 1: max capacity
    >>> bin_completion(BinsKeepingContents(), binsize=100, items=[100,100,100,100,100,100])
    [[100], [100], [100], [100], [100], [100]]

    Example 2: min capacity
    >>> bin_completion(BinsKeepingContents(), binsize=100, items=[1,2,3,4,5,85])
    [[1,2,3,4,5,85]]

    Example 3: Complex input
    >>> bin_completion(BinsKeepingContents(), binsize=100, items=[99,94,79,64,50,44,43,37,32,19,18,7,3])
    [[99], [94,6], [79,18,3], [64,32], [50,43,7], [44,37,19]]

    Example 4: Article Example #1
    >>> bin_completion(BinsKeepingContents(), binsize=100, items=[100, 98, 96, 93, 91, 87, 81, 59, 58, 55, 50, 43, 22, 21, 20, 15, 14, 10, 8, 6, 5, 4, 3, 1, 0])
    [[100], [98, 1], [96, 4], [93, 6], [91, 8], [87, 10, 3], [81, 14, 5], [59, 21, 20], [58, 22, 15], [55, 43], [50]]

    Example 5: Article Example #2
    >>> bin_completion(BinsKeepingContents(), binsize=100, items=[6, 12, 15, 40, 43, 82])
    [[82,6,12], [15,40,43]]

    Example 6: Article Example #3
    >>> bin_completion(BinsKeepingContents(), binsize=100, items=[99, 97, 94, 93, 8, 5, 4, 2])
    [[99], [97, 2], [94, 5], [93, 4], [8]]
    """

    ffd_solution = first_fit.decreasing(BinsKeepingContents(), binsize, items)
    lower_bound = l2_lower_bound(binsize, items)

    # Check casting
    if ffd_solution.num == math.ceil(lower_bound):
        return ffd_solution

    

    return 0


if __name__ == "__main__":
    import doctest

    items = [99, 97, 94, 93, 8, 5, 4, 2]
    s = sum(items)
    print(l2_lower_bound(100, items))
    print("sum ", s)
    print("sum+98 ", (98 + sum(items)))
    print("Should be ", ((98 + sum(items)) / 100))

    from prtpy.packing import first_fit as ff

    items = [100, 100, 100, 100, 100, 100]
    print(ff.decreasing(BinsKeepingContents(), binsize=100, items=[99, 94, 79, 64, 50, 44, 43, 37, 32, 19, 18, 7, 3]))
    # print(doctest.testmod())