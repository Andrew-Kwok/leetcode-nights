class Solution:
    def lower_bound(self, A: List[int], x: int) -> int:
        l, r = 0, len(A)
        while l < r:
            mid = (l + r) >> 1
            if ar[mid] <= x:
                r = mid
            else l = mid + 1
        return l

    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumAlice, sumBob = sum(aliceSizes), sum(bobSizes)
        diff = (sumAlice - sumBob) // 2
        bobSizes.sort()

        for x in aliceSizes:
            y = x - dif
