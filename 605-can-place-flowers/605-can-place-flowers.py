class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_flowerbed = [0] + flowerbed + [0]
        
        for i in range(len(new_flowerbed)-2):
            if new_flowerbed[i] == new_flowerbed[i+2] == 0 and new_flowerbed[i+1] == 0:
                new_flowerbed[i+1] = 1
                n -= 1
            
        return n <= 0
    