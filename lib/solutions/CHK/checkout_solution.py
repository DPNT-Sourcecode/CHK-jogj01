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

            if sku not in offers:
                basket[sku]["total"] += products[sku] * basket_q

            else:
                # offer_dict = {
                #   3: [{'sku': 'A', 'q': 3, 'p': 130}], 
                #   5: [{'sku': 'A', 'q': 5, 'p': 200}]}
                # }
                # offer_dict = {
                #   2: [
                #       {'sku': 'E', 'q': 2, 'p': 80},
                #       {'sku': 'B', 'q': 1, 'p': -30},
                # ]
                offer_dict = offers.get(sku)
                print(offer_dict)
                
                # [5, 3]
                # [2]
                sorted_q = sorted(offer_dict.keys(), reverse=True)
                print(sorted_q)
                
                i = 0
                remaining_items = basket_q
                while i < len(sorted_q):
                    print(i, remaining_items)
                    # offer_list = [{'sku': 'A', 'q': 5, 'p': 200}]
                    # offer_list = [{'sku': 'A', 'q': 3, 'p': 130}]
                    # offer_list = [
                    #   {'sku': 'E', 'q': 2, 'p': 80},
                    #   {'sku': 'B', 'q': 1, 'p': -30}
                    # ]
                    offer_list = offer_dict[sorted_q[i]]
                    print(offer_list)

                    for dict_ in offer_list:
                        sku_to_update = dict_["sku"]

                        if sku_to_update != sku:
                            try:
                                basket[sku_to_update]["total"] += dict_['q']
                            except:
                                pass

                        else:
                            num_bundles = int(remaining_items / dict_['q'])
                            print(num_bundles)
                            print(remaining_items % dict_['q'])
                            basket[sku_to_update]["total"] += num_bundles * dict_['p']
                            i += 1
                            remaining_items -= dict_['q']
                
                basket[sku_to_update]["total"] += products[sku_to_update] * remaining_items

                        
        print(basket)
                            

        total = 0
        for sku, dict_ in basket.items():
            if dict_["total"] > 0:
                total += dict_["total"]
        print(total)
        return total

    return -1


if __name__ == "__main__":
    import sys

    skus = sys.argv[1]
    checkout(skus)








