class Solution:
    def oddString(self, words: List[str]) -> str:
        """
        O(mn), words times characters 
        O(m) words 
        idea is to build a dict (calculated_values): [list of words in words that have the same value]
        At the end, there will be an element where its value consists of only one input
        This is the string that is unique 
        """
        d = {}
        # Helper to calculate the difference array for a given word
        def calculate_difference_array(word: str) -> tuple:
            return tuple(ord(word[i + 1]) - ord(word[i]) for i in range(len(word) - 1))
        
        # Populate the difference map with difference arrays
        for word in words:
            difference_array = calculate_difference_array(word)
            if difference_array in d:
                d[difference_array].append(word)
            else:
                d[difference_array] = [word]
        
        # Find the difference array that has only one corresponding word
        for string_list in d.values():
            if len(string_list) == 1:  # Unique difference array
                return string_list[0]  # Return the unique string

       def oddString_one_place(self, words: List[str]) -> str:
           """
           as above, no helper function
           """
           d = {} # (numbers that a differences): [words that have such differences]
            for word in words:
                curr_res = []
                for ch_ix in range(len(word) - 1):
                    curr_res.append(ord(word[ch_ix + 1]) - ord(word[ch_ix]))  
                curr_res = tuple(curr_res)  # Convert list to tuple for use as a dictionary key
                if curr_res in d:
                    d[curr_res].append(word)
                else:
                    d[curr_res] = [word]
            # Return the list of words that have unique 'curr_res' values
            for strings in d.values():
                if len(strings) == 1:  # Only one occurrence of this 'curr_res'
                    return strings[0]  # Fixed to return the correct string
