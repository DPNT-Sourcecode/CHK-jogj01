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

        for sku,quantity in basket.items():
            if not sku in offers:
                total += products[sku] * quantity
            else:
                num_single_items = basket[sku] % offers[sku]['q']
                num_bundles = int(basket[sku] / offers[sku]['q'])
                total += (num_single_items * products[sku] + num_bundles * offers[sku]['p'])
        print(total)
        return total


    return -1


if __name__ == "__main__":
    import sys

    skus = sys.argv[1]
    checkout(skus)






