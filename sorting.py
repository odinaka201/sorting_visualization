def bubble_sort(vals):
    swaps = False
    n = len(vals)
    for i in range(n):
        for j in range(n-1):
            if vals[j] > vals[j+1]:
                swaps = True
                curr = vals[j]
                vals[j] = vals[j+1]
                vals[j+1] = curr
        if not swaps:
            return vals
        else:
            swaps = False
print(bubble_sort([1, 2, 3, 5, 4]))


def selection_sort():
    pass 

def insertion_sort():
    pass 

def shell_sort():
    pass 

def cocktail_shaker_sort():
    pass 

def merge_sort():
    pass

def quick_sort():
    pass

def heap_sort():
    pass

def bucket_sort():
    pass

def radix_sort():
    pass

def timsort():
    pass

def introsort():
    pass

def bitonic_sort():
    pass

def bogo_sort():
    pass

def gnome_sort():
    pass

def comb_sort():
    pass

def bead_sort():
    pass

def sleep_sort():
    pass

def tree_sort():
    pass

def odi_sort():
    # TODO: come up with your own sorting algorithm
    pass

