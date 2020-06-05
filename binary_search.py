# binary search algorithm

# exiting the loop/when lb equals ub or ROI is 0
# is the midpoint value the target?
# is the midpoint value < target?
# is the midpoint value > target?


def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:
            return -1

        mid_index = (lb + ub) // 2
        item_at_mid = xs[mid_index]

        if item_at_mid == target:
            return mid_index

        if item_at_mid < target:
            lb = mid_index + 1

        else:
            ub = mid_index
