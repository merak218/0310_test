def twoSum(nums, target):
    mapped = {}
    if target >109 or target < -109:
        print('target must >= -109 and <=109')
    else:
        if len(nums) >103 or len(nums) < 2:
            print("nums's length must >=2 and <= 103")
        else:
            for i, n in enumerate(nums):
                if nums[i] > 109 or nums[i] < -109:
                    print(nums[i], 'is not <=109 and >= -109')
                else:
                    diff = target - nums[i]
                    if diff in mapped:
                        return [mapped[diff], i]
                    mapped[n] = i
    
target = int(input('target: '))
nums = list(map(int, input('nums: ').split(' ')))
print(twoSum(target=target, nums=nums))