from ast import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rslt = [[1]]
        for i in range(1, numRows):
            r = [1]  
            for j in range(1, i):
                r.append(rslt[i-1][j-1] + rslt[i-1][j])
            
            r.append(1)
            rslt.append(r)

        return rslt