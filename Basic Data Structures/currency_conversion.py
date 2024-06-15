from collections import defaultdict
from collections import deque

currency_rates = [] # list to store dictionary values: see the func below to fill it out
dict_values = ["start","end","exchange_rate"] # list to associate with currencies
def currency_converter(currencyfrom, currencyto, rates = currency_rates):
    final_rate = 1 #initialise final rate value 
    nowcurrency = currencyfrom #checks whether currenct currency matches target

    while True:
        for item in rates:
            #loops through dict list to find currenct currency
            if item["start"] == nowcurrency: 
                print(f"{nowcurrency} ->", end=" ")
                final_rate = final_rate * (item["exchange_rate"]) #applies exchange rate to final rate
                nowcurrency = item["end"] #modies current currency
                print(nowcurrency)
                if nowcurrency == currencyto: 
                    break # break for loop if current currency matches target
            if item["end"] == nowcurrency:
                print(f"{nowcurrency} ->", end=" ")
                final_rate = final_rate * (1/item["exchange_rate"]) #applies inverse of exchange rate to final rate
                nowcurrency = item["start"] #modies current currency
                print(nowcurrency)
                if nowcurrency == currencyto:
                    break # break for loop if current currency matches target
        if nowcurrency == currencyto:
                    break # break while loop if current currency matches target
    return final_rate

def currency_conversion_dict(exchangeRate, values = dict_values):
    currency_dict = {}
    for index, value in enumerate(exchangeRate):
        currency_dict[values[index]] = value
    currency_rates.append(currency_dict)




def findRate(l, s, t):
    """
    array of currency conversion rates. E.g. ['USD', 'GBP', 0.77] which means 1 USD is equal to 0.77 GBP
    an array containing a 'from' currency and a 'to' currency

    Example:
    You are given the following parameters:
    Rates: ['USD', 'JPY', 110] ['US', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
    To/From currency ['GBP', 'AUD']

    Find the rate for the 'To/From' curency. In this case, the correct result is 1.89.
    """
    res = -1
    d = {}
    visited = set()
    for arr in l:
        m  = d.get(arr[0], {}) 
        m[arr[1]] = arr[2]
        d[arr[0]] = m
        m  = d.get(arr[1], {}) 
        m[arr[0]] = 1 / arr[2]
        d[arr[1]] = m
    
    def recur(curr, value, visited): # DFS recursion
        if(curr == t):
            nonlocal res
            res = max(res, value)
            return 
        if(curr in visited):
            return 
        visited.add(curr)

        if(curr in d):
            c = list(d[curr].keys())
            i = 0 
            while(i < len(c)):
                recur(c[i], value * cache[curr][c[i]], visited.union(c[i]))
                i += 1
    recur(s, 1, set())

     def recur_bfs(curr, value, visited):
        q = [[s, 1]]
        while(len(q)):
            e=q.pop(0)
            c, val = e
            if c not in visited:
               if c == t:
                   res = max(res, val)
            else:
                visited.add(c)
                i = 0
                if c in d:
                    k = list(d[c].keys())
                     while i < len(k):
                        q.append([k[i], d[c][k[i]] * val])
                        i += 1
        return res




    
