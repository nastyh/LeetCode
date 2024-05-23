class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # the problem here is to process elements accurately
        # and the edge cases like when you have the same people in the same place
        # and under $1000
        d = defaultdict(list)  # we will have d[name] = [time, amount, city]
        invalid = set() # to cover the same people
        res = []
        for k, v in enumerate(transactions):
            # easy: process elements splitting them on a comma 
            name, time, amount, city = v.split(",")
            if int(amount) > 1000:
                invalid.add(k) # the most obvious check, add the index to the set
            if name in d:  # the same person 
                for prev_tr, ix in d[name]:  # looking at their past behavior
                    _, prev_time, _, prev_city = prev_tr.split(",") # only need to pieces here
                    if abs(int(time) - int(prev_time)) <= 60 and prev_city != city:
                        # two another conditions: time and location
                        invalid.add(ix) # because we need both operations in the answer
                        invalid.add(k)
            d[name].append((v, k))
        for i in invalid: # build the answer 
            res.append(transactions[i])
        return res