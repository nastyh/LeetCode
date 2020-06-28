def findRestaurant(list1, list2):
    shorter = list1 if len(list1) < len(list2) else list2
    longer = list1 if len(list1) >= len(list2) else list2
    shorter_d, longer_d, combined_d = {}, {}, {}
    for k, v in enumerate(shorter):
        shorter_d[v] = k
    for k, v in enumerate(longer):
        longer_d[v] = k

    for key in shorter_d:
        if key in longer_d:
            combined_d[key] = shorter_d[key] + longer_d[key]

    return [k for k, v in combined_d.items() if v == min(combined_d.values())]



if __name__ == '__main__':
    print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
    print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Shogun", "Burger King"]))
