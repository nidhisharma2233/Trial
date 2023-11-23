#6. Remove duplicates from a list while preserving the order of elements.
def remove_duplicates(lst):
        print (list(dict.fromkeys(lst).keys()))


nums = [2, 4, 3, 5, 4, 6, 9, 2, 1]
remove_duplicates(nums)



