class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        with the deque
        """
        deck.sort()
        
        # Initialize a deque to store the indices
        indices = deque(range(len(deck)))  # 0, 1... and to the end
        # Initialize the result array
        result = [0] * len(deck)
        
        # Iterate over sorted deck and populate result array
        for card in deck:
            # Take the index of the next unrevealed card
            idx = indices.popleft()  # indices matches deck
            # Assign the revealed card to the correct position
            result[idx] = card
            # If there are still unrevealed cards, move the next unrevealed card to the end
            if indices:
                indices.append(indices.popleft())
        return result

    def deckRevealedIncreasing_recur(self, deck: List[int]) -> List[int]:
        """
        Sort the deck
        Decide whether the first element is used or put back
        Store the card used in current iteration in a list (in ascending order)
        Store the card folded in another list (by recursively calling the functino)
        Merge the 2 lists
        Base case when number of remaining cards <= 2
        """
        deck.sort() 
        l = len(deck)
        def recur(start: int, use_next: bool):
            if len(deck) - start <= 2 and use_next: 
                return deck[start:]
            elif len(deck) - start <= 2: 
                res = deck[start:]
                res = res[::-1]
                return res 
            
            if use_next: 
                mid_pt = ceil((start + l) / 2)
                first_half = deck[start:mid_pt] 
                second_half = recur(mid_pt, (l - start) % 2 == 0)
            else: 
                mid_pt = floor((start + l) / 2)
                second_half = deck[start:mid_pt]
                first_half = recur(mid_pt,  (l - start) % 2 == 1)

            # merge 
            res = [] 
            for i in range(len(first_half)): 
                res.append(first_half[i])
                if i < len(second_half): 
                    res.append(second_half[i])
            return res
    
        return recur(0, True)