class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed=[0]+flowerbed+[0]
        count=0
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1:i+2]==[0,0,0]:
                count+=1
                flowerbed[i]=1
        if count>=n:
            return True
        else: 
            return False