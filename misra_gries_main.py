def misra_gries(k, data):
    """
    Implement the Misra-Gries algorithm.

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

    misra_gries_factor = len(data) / k

    for elem in data:
        if elem in d1.keys():
            if elem in d2.keys():
                d2[elem] += 1
            else:
                d2[elem] = 1

    for key in list(d2.keys()):
        if d2[key] < misra_gries_factor:
            del d2[key]

    return d2


print("Algorithm test:")

stream = [1, 4, 5, 4, 4, 5, 4, 4]

k_par = 2

res = misra_gries(k_par, stream)  # should return 4: 5
print(res)

# 3

print("\nTest - no guarantee of finding the most frequent element in data stream:")
stream = [1, 1, 1, 2, 3, 4, 8, 6, 9, 8]
k_par = 2
res = misra_gries(k_par, stream)
print(res)
