from collections import defaultdict
from variables import products, offers

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        return -1
    
    if len(skus) == 1 and skus in products.keys():
        return products[skus]
    
    if len(skus) > 1:
        total = 0
        basket = {}
        
        for sku in list(skus):
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





