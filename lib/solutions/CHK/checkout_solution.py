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
            {"sku": "E", "q": 2, "p": 80},
            {"sku": "B", "q": 1, "p": -30}
            # {"sku": "B", "q": 1, "p": 0}  # for OPTION A and OPTION B
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
            # basket[sku]["p"] += products[sku]
        print(basket)

        for sku, qp_dict in basket.items():
            basket_q = qp_dict["q"]

            if basket_q > 0 and sku not in offers:
                print("print from if")
                basket[sku]["p"] += basket[sku]["q"] * products[sku]
                print(basket)
                print()

            elif basket_q > 0 and sku in offers:
                print("print from elif")
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
                else:
                    remaining_items = basket_q
                    for offer_q in sorted_q:
                        # e.g. offer for buying 3 As:
                        # [{"sku": "A", "q": 3, "p": 130}]
                        offer_list = offer_dict[offer_q]
                        print(offer_list)

                        for dict_ in offer_list:
                            sku_to_update = dict_["sku"]
                            # basket[sku_to_update]["p"] = 0                                

                            if sku != sku_to_update:
                                print("from sku != sku_to_update")
                                
                                promo_q = dict_["q"]
                                promo_p = dict_["p"]
                                basket[sku_to_update]["p"] += promo_q * promo_p

                                ### OPTION B:
                                # promo_q = dict_["q"]
                                # promo_p = dict_["p"]
                                # remaining_q = basket[sku_to_update]["q"] - promo_q
                                # remaining_p = products[sku_to_update]
                                # basket[sku_to_update]["p"] = promo_q * promo_p + remaining_q * remaining_p
                                
                                #### OPTION A:
                                # print(basket[sku_to_update]["q"])
                                # print(dict_["q"])
                                # num_bundles = int(basket[sku_to_update]["q"] / dict_["q"])
                                # single_items = basket[sku_to_update]["q"] % dict_["q"]
                                # print(sku_to_update, num_bundles, single_items)
                                # basket[sku_to_update]["p"] += num_bundles * dict_["p"]
                                # basket[sku_to_update]["p"] += products[sku_to_update] * single_items
                                break

                            
                            num_bundles = int(remaining_items / dict_["q"])
                            single_items = remaining_items % dict_["q"]
                            print(sku_to_update, remaining_items, num_bundles, single_items)
                            
                            basket[sku_to_update]["p"] += num_bundles * dict_["p"]
                            remaining_items = single_items

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

        
        # for sku, val_dict in basket.items():
        #     basket_q = val_dict["q"]

        #     if sku not in offers:
        #         basket[sku]["total"] += products[sku] * basket_q

        #     else:
        #         # offer_dict = {
        #         #   3: [{"sku": "A", "q": 3, "p": 130}], 
        #         #   5: [{"sku": "A", "q": 5, "p": 200}]}
        #         # }
        #         # offer_dict = {
        #         #   2: [
        #         #       {"sku": "E", "q": 2, "p": 80},
        #         #       {"sku": "B", "q": 1, "p": -30},
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
        #             # offer_list = [{"sku": "A", "q": 5, "p": 200}]
        #             # offer_list = [{"sku": "A", "q": 3, "p": 130}]
        #             # offer_list = [
        #             #   {"sku": "E", "q": 2, "p": 80},
        #             #   {"sku": "B", "q": 1, "p": -30}
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
        #                     basket[sku_to_update] = {"q": num_bundles, "total": num_bundles*dict_["p"]}

        #                 # elif (sku_to_update != sku) and (sku_to_update in basket):
        #                 #     num_bundles = int(basket_q / offer_q)
        #                 #     basket[sku_to_update]["total"] += num_bundles*dict_["p"]

        #                 elif (sku_to_update != sku) and (sku_to_update in basket):
        #                     num_bundles = int(basket_q / offer_q)
        #                     basket[sku_to_update]["q"] += num_bundles
        #                     basket[sku_to_update]["total"] = basket[sku_to_update]["q"] * dict_["p"]

        #                 else:
        #                     num_bundles = int(remaining_items / dict_["q"])
        #                     single_items = remaining_items % dict_["q"]
        #                     print(num_bundles)
        #                     print(single_items)
        #                     basket[sku]["total"] += num_bundles * dict_["p"]
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



