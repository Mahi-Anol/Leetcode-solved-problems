class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        map={}
        for i,num in enumerate(nums):
            if num not in map:
                map[num]=[i]
            else:
                map[num].append(i)

        
        for i in range(len(nums)):
            # if i==map.get(target-nums[i+1]):
            #     if i !=map[target-nums[i+1]][0]:
            if map.get(target-nums[i]):
                for j in map.get(target-nums[i]):
                    if i != j:
                        return [i,j]
                # else:
                #     return [i, map[target-nums[i+1]][1]]
### solution 2 (Better one_)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map={}
        for i,element in enumerate(nums):
            if map.get(target-element)!=None:
                return [i,map[target-element]]
            else:
                map[element]=i
