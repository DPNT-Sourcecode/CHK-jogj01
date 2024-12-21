products = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

offers = {
    "A": {
        3: [{"sku": "A", "q": 3, "p": 130}],
        5: [{"sku": "A", "q": 5, "p": 200}]
    },
    
    "B": {
        2: [{"sku": "B", "q": 2, "p": 45}]
    },

    "E": {
        2: [
            #{"sku": "E", "q": 2, "p": 80},
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
        basket = {sku: {"q": 0, "p": 0} for sku in products.keys()}
        for sku in list(skus):
            if sku not in products:
                return -1 
            
            basket[sku]["q"] += 1
            basket[sku]["p"] += products[sku]
        print(basket)

        for sku, qp_dict in basket.items():
            basket_q = qp_dict["q"]

            # if basket_q > 0 and sku not in offers:
            #     basket[sku]["p"] += basket[sku]["q"] * products[sku]

            if basket_q > 0 and sku in offers:
                print("print from elif")
                print(sku)
                # e.g. for product A:
                # {
                #   3: [{"sku": "A", "q": 3, "p": 130}], 
                #   5: [{"sku": "A", "q": 5, "p": 200}]}
                # }

                # e.g. for product B:
                # {
                #   2: [
                #       {"sku": "E", "q": 2, "p": 80},
                #       {"sku": "B", "q": 1, "p": 0}
                # ]
                # }
                offer_dict = offers.get(sku)
                print(offer_dict)
                
                # [5, 3]
                # [2]
                sorted_q = sorted(offer_dict.keys(), reverse=True)
                print(sorted_q)

                if basket_q < sorted_q[-1]:
                    basket[sku]["p"] = basket_q * products[sku]
                    print(basket)
                    print()
                else:
                    remaining_items = basket_q
                    
                    for offer_q in sorted_q:
                        # e.g. offer for buying 3 As:
                        # [{"sku": "A", "q": 3, "p": 130}]
                        offer_list = offer_dict[offer_q]
                        print(offer_list)

                        for dict_ in offer_list:
                            print(sku)
                            sku_to_update = dict_["sku"]
                            basket[sku_to_update]["p"] = 0
                                            
                            if sku != sku_to_update:
                                print("from sku != sku_to_update")
                                promo_q = dict_["q"]
                                promo_p = dict_["p"]
                                basket[sku_to_update]["p"] += promo_q * promo_p
                                break

                            if sku == sku_to_update:
                                print("sku == sku_to_update")
                                num_bundles = int(remaining_items / dict_["q"])
                                single_items = remaining_items % dict_["q"]
                                print(sku_to_update, remaining_items, num_bundles, single_items)
                                
                                basket[sku_to_update]["p"] += num_bundles * dict_["p"]
                                remaining_items = single_items
                                print(basket)   
                            
                    print("printing the remaining items:")
                    print(sku_to_update, remaining_items, products[sku_to_update])
                    # if sku == sku_to_update:
                    basket[sku_to_update]["p"] += products[sku_to_update] * remaining_items
                    print(basket)
                    print()     
                            
        
        print(basket)
        tot = 0
        for val_dict in basket.values():
            if val_dict["q"] > 0:
                tot += val_dict["p"]
        print(tot)

        return tot

    return -1


if __name__ == "__main__":
    import sys

    skus = sys.argv[1]
    checkout(skus)





