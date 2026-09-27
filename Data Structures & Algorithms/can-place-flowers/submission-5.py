class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0#

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                emptyLeft = (i == 0 or flowerbed[i-1] == 0)
                emptyRight = (i == len(flowerbed) -1 or flowerbed[i+1] == 0)

                if emptyLeft and emptyRight:
                    count += 1
                    flowerbed[i] = 1
        
        return count >= n