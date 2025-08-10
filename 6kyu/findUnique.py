# This function finds the unique number in an aray of similar numbers

def find_uniq(nums: list):
    identicalNum = nums[0] if nums[0] == nums[1] else (nums[0] if nums[0] == nums[2] else nums[2])
    for num in nums:
        if num != identicalNum:
            return num

uniq = find_uniq([ 0, 10, 0, 0, 0 ])
print(uniq)