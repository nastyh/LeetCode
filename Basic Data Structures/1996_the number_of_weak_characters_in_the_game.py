from collections import defaultdict
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """
        sort by attack
        build a dict where you group the items 
        with the same attack value and collect their defenses 
        track the maximum defense encountered for the next attack group
        For each group, every character is compared against the highest defense seen so
        far among characters with strictly higher attack.
        If a character’s defense is lower than that maximum, then it is weak.
        After processing a group, we update the maximum defense value with the best defense from the current group.
        """
        properties.sort(key=lambda x: x[0])
        res = 0
        d = defaultdict(list)
        for attack, defense in properties:
            d[attack].append(defense)
        max_defense = 0
        for atk in sorted(d.keys(), reverse=True):
            for defense in d[atk]:
                if defense < max_defense:
                    res += 1
            max_defense = max(max_defense, max(d[atk]))
        return res