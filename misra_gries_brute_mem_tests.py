from pympler import asizeof


def count_elem_brute(k, data):
    """
    Counts the number of elements in a list that appear less than k times.

    :param k: The factor responsible for the number of entries that will be stored in the result dictionary.
    :param data: The data stream.
    :return: A dictionary mapping elements to their counts and memory usage.
    """

    D1 = {}

    for elem in data:
        if elem in D1.keys():
            D1[elem] += 1
        else:
            D1[elem] = 1

    n = len(data)
    misra_gries_factor = n / k

    for key in list(D1.keys()):
        if D1[key] < misra_gries_factor:
            del D1[key]

    return D1, asizeof.asizeof(D1)


def misra_gries(k, data):
    """
    Implementation of the Misra-Gries algorithm.

    :param k: The factor responsible for the number of entries that will be stored in the result dictionary.
    :param data: The data stream.
    :return: A dictionary of frequent items and memory usage.
    """

    d1 = {}
    d2 = {}

    for elem in data:
        if elem in d1.keys():
            d1[elem] += 1
        elif len(d1) < k - 1:
            d1[elem] = 1
        else:
            for key in list(d1):
                d1[key] -= 1
                if d1[key] == 0:
                    del d1[key]

    for elem in data:
        if elem in d1.keys():
            if elem in d2.keys():
                d2[elem] += 1
            else:
                d2[elem] = 1

    return d2, asizeof.asizeof(d1) + asizeof.asizeof(d2)


stream = [1, 4, 5, 4, 4, 5, 4, 4]
print("Data:", stream)
res1, mem_usg_count = count_elem_brute(2, stream)
res2, mem_usg_misra_gries = misra_gries(2, stream)
print("------------------------")
print(f"Memory usage:\ncount_elems_mgf: {mem_usg_count}\nmisra_gries: "
      f"{mem_usg_misra_gries}")

print("------------------------")
print("Algorithm test count_elems_mgf:")

k_par = 2

res = count_elem_brute(k_par, stream)
print(res)
