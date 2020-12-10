 def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def recurse_number(n):
            # base case
            if n == 1:
                return ["0", "1" , "8"]
            if n== 2:
                return ["00", "11", "88","69","96" ]
            
            res = []
            for num in recurse_number(n-2):
                res.append("0"+ num + "0")
                res.append("6"+ num + "9")
                res.append("9" + num + "6")
                res.append("8" + num + "8")
                res.append("1" + num + "1")
            return res
        
        if n == 0:
            return [""]
        elif n == 1:
            return ["0", "1" , "8"]
        else:
            return [number for number in recurse_number(n) if number[0] != "0" and number[-1] != "0"]