# misra_gries_lab_py
Solving frequent items problem

    misra_gries function implements the Misra-Gries algorithm for finding frequent items in a data stream.

    The algorithm works by maintaining two dictionaries: d1 and d2. d1 is a sliding window of the last k items in the stream, and 
    d2 is a dictionary of all items that have appeared more than 1/k times in the stream.

    The algorithm works as follows:

    1. For each item in the data stream:
        * If the item is in d1, increment its count in d1.
        * If the item is not in d1, add it to d1.
        * If the size of d1 exceeds k, remove the item with the lowest count from d1.
    2. For each item in d2:
        * If the item's count in d2 is less than 1/k, remove it from d2.

    The final output of the algorithm is the dictionary d2, which contains all of the frequent items in the data stream.

- misra_gries_main.py: misra_gries function and basic tests
- misra_gries_terminal: misra_gries function for usage with text files in terminal 
- misra_gries_brute_mem_tests: brute-force alternative for Misra-Gries algorithm with memory usage comparison
  
