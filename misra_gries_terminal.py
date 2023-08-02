import sys
import string


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


print("\nAlgorithm test for console arguments")
if len(sys.argv) == 1:
    print("Empty list of args! Please execute from terminal with 'python misra_gries_terminal.py filename k_parameter'")
    exit(-1)

filename = sys.argv[1]

k = 2

try:
    k = int(sys.argv[2])
    if k <= 0:
        raise ValueError
except ValueError:
    print("Wrong k value!")
    exit(-1)
except IndexError:
    print("Please input k value!")
    exit(-1)

if not isinstance(filename, str) or not isinstance(k, int):
    print("Wrong console arguments!")
    exit(-1)

try:
    with open(filename, mode="r", encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
    exit(-1)

content = content.lower()
words = []
alphabet = string.ascii_letters

word = ""
for i in range(0, len(content)):
    if content[i] in alphabet:
        word += content[i]
    else:
        if word != "":
            words.append(word)
            word = ""

res = misra_gries(k, words)
res = dict(sorted(res.items(), key=lambda item: item[1]))
reversed_res = {key: res[key] for key in reversed(list(res.keys()))}
res = reversed_res
print(res)
