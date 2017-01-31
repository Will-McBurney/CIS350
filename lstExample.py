#List examples

def sum_list(lst):
    """Returns the sum of elements in the list\n
    Uses direct reference in loop"""
    out = 0
    for i in lst:
        out = out + i
    return out

def sum_list_with_index(lst):
    """Returns the sum of elements in the list\n
    Uses index reference in loop"""
    out = 0
    for i in range(0,len(lst)):
        out = out + lst[i]
    return out

def make_1_to_100_list():
    """Returns a lst [1,2,3,...,99,100]"""
    out = []
    for i in range(1,101):
        out.append(i)
    return out

def main():
    lst = make_1_to_100_list()
    print(sum_list_with_index(lst))

main()
