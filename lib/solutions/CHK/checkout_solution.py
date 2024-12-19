

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    prod = {
       'A': 50,
       'B': 30,
       'C': 20,
       'D': 15,
    }

    if len(skus) == 1 and skus in prod.keys():
        return prod[skus]

    return -1
