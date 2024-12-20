products = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

offers = {
    'A': {
        3: [{"sku": "A", "q": 3, "p": 130}],
        5: [{"sku": "A", "q": 5, "p": 200}]
    },
    
    'B': {
        2: [{"sku": "B", "q": 2, "p": 45}]
    },

    'E': {
        2: [
            {"sku": "E", "q": 2, "p": 80},
            {"sku": "B", "q": 1, "p": -30}
        ]
    }
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not skus:
        return 0 
    
    if not isinstance(skus, str):
        return -1
    
    if len(skus) == 1 and skus in products.keys():
        return products[skus]
    
    if len(skus) > 1:
        basket = {}
        
        for sku in list(skus):
            if sku not in products:
                return -1 
            
            if sku in basket:
                basket[sku]["q"] += 1
            else:
                basket[sku] = {"q": 1, "total": 0}
        print(basket)
        return 0

        # for sku,quantity in basket.items():
        #     if not sku in offers:
        #         total += products[sku] * quantity
        #     else:
        #         num_single_items = basket[sku] % offers[sku]['q']
        #         num_bundles = int(basket[sku] / offers[sku]['q'])
        #         total += (num_single_items * products[sku] + num_bundles * offers[sku]['p'])
        # print(total)
        # return total

    return -1


if __name__ == "__main__":
    import sys

    skus = sys.argv[1]
    checkout(skus)






