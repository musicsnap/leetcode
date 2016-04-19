class Item(object):
    def __init__(self):
        index = 0;
        value = 0;

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = len(nums)

        #
        i = 0
        items = []
        for a in nums:
            item = Item()
            item.index = i
            item.value = a
            items.append(item)
            i+=1

        #
        sorted_nums = sorted(items, key = lambda Item:Item.value)

        i = 0
        while i < count:
            j = i+1
            while j < count:
                if sorted_nums[i].value  + sorted_nums[j].value == target:
                    return [sorted_nums[i].index , sorted_nums[j].index]
                j+=1
            i+=1
