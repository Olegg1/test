def moveZeroes(nums) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            print(nums)
        
        return nums

# Пример использования
array = [1, 0, 3, 12]
result = moveZeroes(array)
result