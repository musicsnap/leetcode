#coding:utf-8
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

        #记录下标
        i = 0
        items = []
        for a in nums:
            item = Item()
            item.index = i
            item.value = a
            items.append(item)
            i+=1

        #排序
        sorted_nums = sorted(items, key = lambda Item:Item.value) #列表排序，key参数要注意

        #求和
        i = 0
        while i < count:
            j = i+1
            while j < count:
                if sorted_nums[i].value  + sorted_nums[j].value == target:
                    return [sorted_nums[i].index , sorted_nums[j].index]
                j+=1
            i+=1


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    solution = Solution()
    print solution.twoSum(nums, target)
