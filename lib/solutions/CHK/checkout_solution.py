products = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
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

        # basket = {
        #   'A': {'q': 3, 'total': 0}, 
        #   'B': {'q': 2, 'total': 0}, 
        #   'C': {'q': 1, 'total': 0}, 
        #   'D': {'q': 1, 'total': 0}, 
        #   'E': {'q': 2, 'total': 0}
        # }
        for sku, val_dict in basket.items():
            basket_q = val_dict["q"]
            if offer_dict := offers.get(sku, None):
                # offer_dict = {
                #   3: [{'sku': 'A', 'q': 3, 'p': 130}], 
                #   5: [{'sku': 'A', 'q': 5, 'p': 200}]}
                # }
                for offer_q in offer_dict.keys():
                    if basket_q >= offer_q:
                        # offer_list = [{'sku': 'A', 'q': 3, 'p': 130}]
                        offer_list = offer_dict[offer_q]
                        for dict_ in offer_list:
                            sku_to_update = dict_["sku"]
                            num_single_items = basket_q % dict_['q']
                            num_bundles = int(basket_q / dict_['q'])
                            basket[sku_to_update]["total"] += (
                                num_single_items * products[sku_to_update] + num_bundles * dict_['p']
                            )
                            
            else:
                basket[sku]["total"] += products[sku] * basket_q
        print(basket)
                            


        # for sku,quantity in basket.items():
        #     if not sku in offers:
        #         total += products[sku] * quantity
        #     else:
        #         num_single_items = basket[sku] % offers[sku]['q']
        #         num_bundles = int(basket[sku] / offers[sku]['q'])
        #         total += (num_single_items * products[sku] + num_bundles * offers[sku]['p'])
        # print(total)
        # return total
        return 0

    return -1


if __name__ == "__main__":
    import sys

    skus = sys.argv[1]
    checkout(skus)









