class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # firstly, the element in the target must be contained in the triplets
        # next we need to have max function in our algorithm

        # we need to keep track of triplet that all elements are <= target

        found = [False, False, False]
        for triplet in triplets:
            if all(triplet[i] <= target[i] for i in range(len(target))):
                for j in range(len(triplet)):
                    if triplet[j] == target[j]:
                        found[j] = True
        return all(found)