from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        O(N+M), num of recipes, total number of ingredients
        O(N+M) due to the graph and in-degree maps 
        topological sorting
        build a dependency graph, where we only produce a recipe if all of its dependencies (ingredients) are available.
        Track the in-degree of each recipe (i.e., number of ingredients it needs).
        Start with the supplies as your initial available items.
        For each ingredient, update dependent recipes and reduce their in-degree.
        If a recipe’s in-degree becomes zero, you can produce it.
        """
        gr, indegree = defaultdict(list), defaultdict(int)
        for recipe, ingred_list in zip(recipes, ingredients):
            for ing in ingred_list:
                gr[ing].append(recipe)
                indegree[recipe] += 1
        d, res = deque(supplies), []
        while d:
            item = d.popleft()
            for recipe in gr[item]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    res.append(recipe)
                    d.append(recipe)
        return res 
            

        