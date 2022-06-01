import matplotlib.pyplot as plt
import time
import numpy as np
from prtpy.packing.bin_completion import bin_completion
from prtpy.bins import BinsKeepingContents
from typing import Callable, Any
import math
from typing import List



def bin_completion_with_improvement(items: List):
    start = time.perf_counter()
    bin_completion(BinsKeepingContents(), 100, items,True)
    finish = time.perf_counter()
    return (round(finish - start, 2))


def bin_completion_without_improvement(items: List):
    start = time.perf_counter()
    bin_completion(BinsKeepingContents(), 100, items,False)
    finish = time.perf_counter()
    return (round(finish - start, 2))







if __name__ == "__main__":
    item_size = []
    with_improve = []
    without_improve = []
    size = 10
    for _ in range(5):
        items = []
        for i in range(size):
            items.append(math.ceil(np.random.uniform(low=0, high=100)))
        with_improve.append(bin_completion_with_improvement(items))
        without_improve.append(bin_completion_without_improvement(items))
        item_size.append(size)
        size += 4

    print("with improve:")
    for i in with_improve:
        print(i)
    print("------------------")
    print("withot improve:")
    for i in without_improve:
        print(i)

    # plot in red the result with improve and in blue the results without improve

    plt.plot(with_improve, item_size,'r')
    plt.plot(without_improve, item_size,'b')
    plt.xlabel("input size")
    plt.ylabel("run time")
    plt.show()

