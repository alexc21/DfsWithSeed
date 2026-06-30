def somme_liste(lst):
    res = 0
    for i in lst:
        res += i
    return res


def filtrer_pairs(lst):
    return [i for i in lst if i % 2 == 0]


"""
exercice 3:
lst est une liste vide
on fait une boucle for avec un range de 3
et on append 2 fois une liste contenant i
et on  l'affiche
"""


def factorielle(n):
    if n == 1:
        return 1
    else:
        return n * factorielle(n - 1)


def somme_recursive(lst):

    if not lst:
        return 0
    else:
        return lst[0] + somme_recursive(lst[1:])


def inverser_chaine(s):
    if s == "":
        return s
    else:
        return s[-1] + inverser_chaine(s[:-1])


def two_sum(nums, target):
    somme = 0
    lst = []
    dictio: dict[int, int] = {i: nums[i] for i in range(len(nums))}

    for i in dictio:
        if somme != target:
            somme += dictio[i]
            lst.append(i)
    return lst


def max_subarray(nums):
    somme = 0
    max_global = float("-inf")
    curren_start = 0
    best_start = 0
    best_end = 0

    for i in range(len(nums)):
        if somme < 0:
            somme = nums[i]
            curren_start = i
        else:
            somme += nums[i]

        if somme > max_global:
            max_global = somme
            best_start = curren_start
            best_end = i
    return [nums[i] for i in range(best_start, best_end + 1)]


def max_product_subarray(nums):
    max_cur = nums[0]
    min_cur = nums[0]
    best_result = nums[0]
    new_max = 0
    new_min = 0
    for i in range(1, len(nums)):
        new_max = max(nums[i], min_cur * nums[i], max_cur * nums[i])
        new_min = min(nums[i], min_cur * nums[i], max_cur * nums[i])
        max_cur = new_max
        min_cur = new_min
        best_result = max(max_cur, best_result)


def sliding_window(lst, k):
    return [max(lst[i:i+k]) for i in range(len(lst) - k + 1)]
