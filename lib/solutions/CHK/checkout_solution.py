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


    return -1


