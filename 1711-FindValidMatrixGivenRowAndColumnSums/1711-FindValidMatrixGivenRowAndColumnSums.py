# Last updated: 6/4/2025, 9:19:58 PM
class Solution:
    def restoreMatrix(self, rowsum: List[int], colsum: List[int]) -> List[List[int]]:
        r=len(rowsum)
        c=len(colsum)
        arr=[[0]*c for _ in range(r)]
        i,j=0, 0
        while i<r and j<c:
            x=min(rowsum[i], colsum[j])
            arr[i][j]=x
            if(rowsum[i]==colsum[j]):
                i+=1
                j+=1
            elif(rowsum[i]>colsum[j]):
                rowsum[i]-=colsum[j]
                j+=1
            else:
                colsum[j]-=rowsum[i]
                i+=1
        return arr