class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        isPlantable = True

        amount = n

        for i in range(len(flowerbed)):
            if len(flowerbed) < 2 and flowerbed[0] == 0:
                return True
            if i < len(flowerbed) -1:
                if flowerbed[i] == 0 and isPlantable and flowerbed[i+1] == 0:
                    amount -= 1
                    isPlantable = False
                    continue
            if flowerbed[i] == 1:
                isPlantable == False
            if flowerbed[i] == 0:
                isPlantable = True
        print(amount)
        return amount < 1
