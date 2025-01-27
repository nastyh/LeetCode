"""
Input:

list of menu items: think of something like List<Map<String,Integer>>,
where the key is the name of the menu item and the value is the cost. Example: Popcorn:10, CocaCola:4, Water:2, Coffe:3
amount of coin
Output:
return all the possible items you can buy (without repetition) with the given coins.
"""
from typing import Dict, List
import unittest


def find_combinations(menu: Dict[str, int], coins: int) -> List[List[str]]:
    if not menu or coins <= 0:
        return []
    res = []
    items = list(menu.keys())
    def _helper(st_ix, curr_res, coins_left):
        if coins_left < 0: return
        res.append(curr_res[:])
        for i in range(st_ix, len(items)):
            _helper(i+1, curr_res+[items[i]], coins_left-menu[items[i]])
    _helper(0, [], coins)
    return res

class TestCanBuy(unittest.TestCase):

    def test_empty_menu(self):
        self.assertEqual(find_combinations({}, 10), [])

    def test_zero_coins(self):
        self.assertEqual(find_combinations({"A": 5, "B": 10}, 0), [])

    def test_single_item_can_buy(self):
        self.assertEqual(find_combinations({"A": 5}, 5), [{ "A"}])

    def test_single_item_cannot_buy(self):
        self.assertEqual(find_combinations({"A": 5}, 4), [])

    def test_multiple_items_can_buy(self):
        menu = {"A": 5, "B": 10, "C": 3}
        coins = 15
        expected_combinations = [{ "A", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C", "B"}, { "A", "C"}]