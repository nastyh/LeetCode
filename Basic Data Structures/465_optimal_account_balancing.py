class Solution:
    def minTransfers_recursion(self, transactions: List[List[int]]) -> int:
        """
        O(n*2^n) -- to run the recursion function n times 
        O(2^n) -- due to the extra lists
        if the length is n, we need n - 1 transactions at most
        how many subgroups the balance list can be divided into such that
        the sum of balances in each subgroup is 0.
        store the non-zero net balance of each person in a list
        use a binary number to indicate which people are in the group, with the lowest bit set to 1 to denote that the 0th
        person is in the group, and so on.
        optimal solution to the original problem by recursively searching for the optimal solutions to subproblems.
        remove one person from the current group at a time and recursively find the optimal solution for that subgroup. 
        if the total balance of the current group is zero, it means that the sum of each subproblem is not zero
        (since each subproblem is obtained by removing a non-zero balance from the current problem).
        Therefore, the non-zero part of the subproblem, plus the balance of the additional person in the
        current problem, make up an additional group whose sum is zero. Thus, the optimal solution to the current
        problem is the maximum optional solution to its subproblems plus 1

        create dp of length 2**n with all values == -1
        collect all non-zero balances
        helper divides the input into the largest possible number of subgroups with sum of 0

        """
        bank = defaultdict(int)
        for a, b, amount in transactions:
            bank[a] += amount
            bank[b] -= amount
        
        balances = [balance for balance in bank.values() if balance]
        n = len(balances)

        # Settle debt except person with ID i
        def _helper(i):
            while i < n and balances[i] == 0:
                i += 1
            # Base Case
            if i == n: return 0
            transaction = 101
            for nxt in range(i + 1, n):
                # Optimize by ONLY considering transactions if there is a net sign change
                if balances[i] * balances[nxt] < 0:
                    balances[nxt] += balances[i]                    # UPDATE
                    transaction = min(transaction, 1 + dfs(i + 1))  # RECURSE
                    balances[nxt] -= balances[i]                    # UNDO
            return transaction
        return _helper(0)

        def minTransfers_another(self, transactions: List[List[int]]) -> int:
            """
            debt table for everyone.
            eliminate people with zeroes
            If there is any pair of complementary values (ex. 5 and -5), settle up both of them and count it as one transaction.
            The remaining will goes to the list.

            Sweep from 0 to len(debts)
            At each step, settle up current person with another person with a larger index. (Only look at following people)
            Skip people with 0 or same sign
            (Attempt settling up only when debts[current guy]*debts[following guy]<0)
            Check the next person to see the minimum transactions needed.
            """
            store = defaultdict(int) # debt table
            for i, j, k in transactions: #from, to, amount
                store[i] += k
                store[j] -= k
            temp,pairs = defaultdict(int),0
            for i, j in store.items():
                if j: # eliminate zeros 
                    if temp[-j] > 0: # eliminate pairs like (-5, 5) since it's a wash
                        temp[-j] -= 1
                        pairs += 1
                    else:
                        temp[j] += 1
            debts = [] # to list
            for i,j in temp.items():
                if j:
                    debts += [i]*j

            def bt(idx):
                while idx < len(debts) and not debts[idx]:
                    idx += 1
                if idx==len(debts):
                    return 0
                
                res = len(debts) # just an upper bound for transactions
                for i in range(idx + 1,len(debts)):
                    if debts[idx] * debts[i] < 0:
                        debts[i] += debts[idx]
                        res = min(res, bt(idx + 1) + 1)
                        debts[i] -= debts[idx]
                return res
            return bt(0) + pairs 
                