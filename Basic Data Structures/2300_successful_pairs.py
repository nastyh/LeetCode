class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        Sort potions
        We need to find such a potion (for each spess) so that multiplied by the current spell the result is >= target
        Process potions from the right. If spell times the current potion >= success, we can try and pick a weaker potion
        and see how it works
        O(nlogn + mlogm)
        O(n) or maybe O(1) due to extra data structures
        """
        potions.sort()
        spells_mapping = [(sp, ix) for ix, sp in enumerate(spells)] # value from the list: its index 
        spells_mapping.sort() # sort by the strongest spell
        res = [0] * len(spells)
        max_potion_ix = len(potions) - 1 # the last potion is the strongest since it's all sorted 
        for spell, ix in spells_mapping:
            while max_potion_ix >= 0 and spell * potions[max_potion_ix] >= success: 
                # first needed b/c lists can be of the different lengths
                # second is the core condition
                max_potion_ix -= 1 # move the pointer since we need to test a weaker potion
            res[ix] = len(potions) - (max_potion_ix + 1) # build the result
        return res