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
        sku_list = list(skus)
        basket = {}
        for sku in sku_list:
            if sku in basket:
                basket[sku] += 1
            else:
                basket[sku] = 1
        print(basket)
        return -1


    return -1


if __name__ == "__main__":
    import sys

    skus = sys.argv[1]
    checkout(skus)


