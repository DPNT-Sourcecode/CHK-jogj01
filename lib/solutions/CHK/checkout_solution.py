from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    products = {
       'A': 50,
       'B': 30,
       'C': 20,
       'D': 15,
    }

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




