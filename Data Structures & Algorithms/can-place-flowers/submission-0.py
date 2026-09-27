class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        isPlantable = False

        amount = n

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and isPlantable and flowerbed[i+1] == 0:
                amount -= 1
                isPlantable = False
                continue
            if flowerbed[i] == 1:
                isPlantable == False
            if flowerbed[i] == 0:
                isPlantable = True

        return amount < 1
