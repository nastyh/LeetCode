class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        """
        O(nlogn) and O(n)
        sort the items
        build max_beauty_at_price that is the list of price, maximum max_beauty we can get
        process queries: if current val < the middle element, go right; otherwise left
        """
        items.sort()
        res = []
        max_beauty_at_price = []
        curr_max_beauty = 0
        
        for price, beauty in items:
            curr_max_beauty = max(curr_max_beauty, beauty)
            max_beauty_at_price.append((price, curr_max_beauty))
        
        for query in queries:
            idx = bisect_right(max_beauty_at_price, (query, float('inf'))) - 1
            
            if idx >= 0:
                res.append(max_beauty_at_price[idx][1])
            else:
                res.append(0)
        return res
    def maximumBeauty_pointers(self, items: List[List[int]], queries: List[int]) -> List[int]:
        """
        O(nlogn) 
        O(n + q)
        Using the two pointers (i for queries and j for items), iterate through the sorted queries.
        For each query, check whether the current item's price is less than or equal to the query. 
        If so, make updates
        If the current item's price is greater than the query price or if all items have been processed, just move to the next query by incrementing i.
        Store the maximum beauty found for each query price in a dictionary.
        """
        items.sort(key=lambda x: x[0])
        d = {}
        # track of the maximum beauty, and indices for items and queries
        max_b, item_ix, query_ix = 0, 0, 0
        sorted_q = sorted(queries)
        while query_ix < len(sorted_q):
            curr_q = sorted_q[query_ix]
            # Update the maximum beauty as long as there are items that can be bought within current_query price
            while item_ix < len(items) and curr_q >= items[item_ix][0]:
                max_b = max(max_b, items[item_ix][1])
                item_ix += 1
            # maximum beauty for the current query price
            d[curr_q] = max_b
            query_ix += 1
        
        return [d[query] for query in queries]


