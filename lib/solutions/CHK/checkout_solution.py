from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    prod = {
       'A': 50,
       'B': 30,
       'C': 20,
       'D': 15,
    }

    if not isinstance(skus, str):
        return -1

    if len(skus) == 1 and skus in prod.keys():
        return prod[skus]
    
    if len(skus) > 1:
        basket = defaultdict(list(skus), 0)
        print(basket)
        return skus


    return -1


if __name__ == "__main__":

    import os
    import sys

    print(os.environ['PYTHONPATH'])

    skus = sys.argv[1]
    checkout(skus)






