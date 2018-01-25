def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # First trial - beat 27%
        '''
        for x in range(0,len(nums)):
            diff = target - nums[x]
            if diff in nums[x+1:]:
                return [x, nums[x+1:].index(diff)+1+x]
        '''

        # Second trial - beat 57.53%
        '''
        dict_nums = {nums[x]:x for x in range(len(nums))}
        for num in range(len(nums)):
            diff = target - nums[num]
            if diff in dict_nums and num != dict_nums[diff]:
                return [num, dict_nums[diff]]
        return False
        '''

        # Sample
        
        diff = {}
        for ind, num in enumerate(nums):
                if target-num in diff:
                    return [diff[target-num],ind]
                diff[num] = ind
                print(diff)
        return False

