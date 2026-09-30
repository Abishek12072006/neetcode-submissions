class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[]
        for i in range(n+1):
            new=bin(i)[2:]
            count=0
            for i in new:
                if i=='1':
                    count+=1
            output.append(count)
        return output

        