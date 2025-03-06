class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hashmap = defaultdict(int)
        total_length = len(arr)
        threshold = total_length // 2 + 1
        ans = 1
        for num in arr:
            hashmap[num] += 1
        
        frequencies = list(hashmap.values())
        frequencies.sort(reverse=True)
        
        for freq in frequencies:
            total_length -= freq
            if total_length >= threshold:
                ans += 1
                
        return ans



        