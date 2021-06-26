import random
from all_sorts import quicksort, merge_sort, bubble_sort, insertion_sort, selection_sort
import time

def create_random_list(size, max_val):
    return [random.randint(1, max_val) for i in range(size)]

def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed time: {seconds:.5f}")


size = int(input("What size list do you want to create? "))
max = int(input("What is the max value of the range? "))
run_time = int(input('For how many times do you want to run? '))


for i in range(run_time):
    print("Run time: ", i + 1)

    l = create_random_list(size, max)

    analyze_func(bubble_sort, l.copy())
    analyze_func(selection_sort, l.copy())
    analyze_func(insertion_sort, l.copy())
    analyze_func(merge_sort, l.copy())
    analyze_func(quicksort, l.copy())
    analyze_func(sorted, l.copy())

    print("--" * 20)