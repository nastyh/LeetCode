class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        """
        O(n&2m), companies and others
        O(m), others 
        """
        res = []
        fav_set =[set(companies) for companies in favoriteCompanies]
        print(fav_set)
        for ix, co in enumerate(fav_set):
            check = False
            for others in fav_set:
                if co != others and others >= co:
                    check = True
                    break
            if not check:
                res.append(ix)
        res.sort()
        return res

    def peopleIndexes_dict(self, favoriteCompanies: List[List[str]]) -> List[int]:
        """
        O(mn) and O(m)
        dict where company: [indices of the lists this company occurs]
        then iterate over the given list of list again and check for a 
        particular index->if the intersection of set(company name's hash value list)s length is equal to 1 or not.
        """
        d = {}
        res = []
        for i in range(len(favoriteCompanies)):
            for co in favoriteCompanies[i]:
                if co in d:
                    d[co].append(i)
                else:
                    d[co] = [i] 
        for i in range(len(favoriteCompanies)):
            b = set(d[favoriteCompanies[i][0]])
            for j in favoriteCompanies[i][1:]:
                b = b & set(d[j])
            if len(b) == 1:
                res.append(i)
        return res
