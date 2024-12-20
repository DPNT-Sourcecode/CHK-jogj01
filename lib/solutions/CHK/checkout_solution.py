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
            {"sku": "B", "q": 2, "p": 30}
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
        # basket = {
        #   'A': {'q': 0, 'total': 0}, 
        #   'B': {'q': 0, 'total': 0}, 
        #   'C': {'q': 0, 'total': 0}, 
        #   'D': {'q': 0, 'total': 0}, 
        #   'E': {'q': 0, 'total': 0}
        # }
        basket = {sku: {"q": 0, "total": 0} for sku in products.keys()}
        
        for sku in list(skus):
            if sku not in products:
                return -1 
            
            basket[sku]["q"] += 1
            basket[sku]["total"] += products[sku]
        print(basket)

        for sku, dict_ in basket.items():
            if sku in offers:
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
                
        
        return basket

        
        # for sku, val_dict in basket.items():
        #     basket_q = val_dict["q"]

        #     if sku not in offers:
        #         basket[sku]["total"] += products[sku] * basket_q

        #     else:
        #         # offer_dict = {
        #         #   3: [{'sku': 'A', 'q': 3, 'p': 130}], 
        #         #   5: [{'sku': 'A', 'q': 5, 'p': 200}]}
        #         # }
        #         # offer_dict = {
        #         #   2: [
        #         #       {'sku': 'E', 'q': 2, 'p': 80},
        #         #       {'sku': 'B', 'q': 1, 'p': -30},
        #         # ]
        #         offer_dict = offers.get(sku)
        #         print(offer_dict)
                
        #         # [5, 3]
        #         # [2]
        #         sorted_q = sorted(offer_dict.keys(), reverse=True)
        #         print(sorted_q)
                
        #         i = 0
        #         remaining_items = basket_q
        #         while i < len(sorted_q):
        #             offer_q = sorted_q[i]
        #             print(i, remaining_items, sorted_q[i])
        #             # offer_list = [{'sku': 'A', 'q': 5, 'p': 200}]
        #             # offer_list = [{'sku': 'A', 'q': 3, 'p': 130}]
        #             # offer_list = [
        #             #   {'sku': 'E', 'q': 2, 'p': 80},
        #             #   {'sku': 'B', 'q': 1, 'p': -30}
        #             # ]
        #             offer_list = offer_dict[sorted_q[i]]
        #             print(offer_list)

        #             for dict_ in offer_list:
        #                 sku_to_update = dict_["sku"]
        #                 print(sku, sku_to_update)
        #                 print(f"sku_to_update != sku: {sku_to_update != sku}")
        #                 print(f"sku_to_update in basket: {sku_to_update in basket}")


        #                 if (sku_to_update != sku) and (basket_q < offer_q):
        #                     continue
                            
        #                 elif (sku_to_update != sku) and (sku_to_update not in basket):
        #                     num_bundles = int(basket_q / offer_q)
        #                     basket[sku_to_update] = {"q": num_bundles, "total": num_bundles*dict_['p']}

        #                 # elif (sku_to_update != sku) and (sku_to_update in basket):
        #                 #     num_bundles = int(basket_q / offer_q)
        #                 #     basket[sku_to_update]["total"] += num_bundles*dict_['p']

        #                 elif (sku_to_update != sku) and (sku_to_update in basket):
        #                     num_bundles = int(basket_q / offer_q)
        #                     basket[sku_to_update]["q"] += num_bundles
        #                     basket[sku_to_update]["total"] = basket[sku_to_update]["q"] * dict_['p']

        #                 else:
        #                     num_bundles = int(remaining_items / dict_['q'])
        #                     single_items = remaining_items % dict_['q']
        #                     print(num_bundles)
        #                     print(single_items)
        #                     basket[sku]["total"] += num_bundles * dict_['p']
        #                     i += 1
        #                     remaining_items = single_items
        #                     print(basket)
                
        #         basket[sku]["total"] += products[sku] * remaining_items
        #         print(basket)
        #         print()
                        
        # print(basket)
                            

        # total = 0
        # for sku, dict_ in basket.items():
        #     if dict_["total"] > 0:
        #         total += dict_["total"]
        # print(total)
        # return total

    return -1


if __name__ == "__main__":
    import sys

    skus = sys.argv[1]
    checkout(skus)





