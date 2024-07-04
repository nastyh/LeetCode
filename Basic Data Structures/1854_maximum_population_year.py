class Solution:
    def maximumPopulation_dict(self, logs: List[List[int]]) -> int:
        """
        O(n) both
        Return the earliest year with the maximum population.
        """
        d = defaultdict(int)
        # calc ther live population in each year and save in the dict
        # 1950: 1, 1951: 1, 1952: 1...
        for born_year, dead_year in logs:
            for y in range(born_year, dead_year):
                d[y] += 1
        # return the earliest maxinum population year
        return max(d.items(), key=lambda x: (x[1], -x[0]))[0]

    def maximumPopulation_linear(self, logs: List[List[int]]) -> int:
        """
        O(n) both
        population for any given year will only change with new births or deaths
        earliest year with the maximum population has to be a birth year since the population will only
        increase with new births. Therefore, we only need to consider the birth years 
        Find the earliest birth year and latest birth year; these will be the lower bound and upper bound of our final answer
        calculate the total population for each birth year (using the dictionary with population changes) and the max population year in the same loop
        """
        population_changes = defaultdict(int)
        min_birth_year, max_birth_year = min(logs)[0], max(logs)[0]
        for birth, death in logs:
            population_changes[birth] += 1
            population_changes[death] -= 1
        # d looks like: 1950: 1, 1961: -1, 1960: 1, 1971: -1, 1970: 1, 1981: -1 
        
        current_population = 0
        max_population = 0
        max_population_year = min_birth_year
        for year in range(min_birth_year, max_birth_year + 1):
            current_population += population_changes[year]
            if current_population > max_population:
                max_population = current_population
                max_population_year = year
        return max_population_year
