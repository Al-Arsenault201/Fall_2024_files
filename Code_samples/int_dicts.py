# in-class coding from October 14

nums = {
        1: 3.14159,
        2: 2.7818,
        3: 42,
        4: 714
}
for key in nums.keys():
    nums[key] *= nums[key]
    print(nums[key])

for key in nums.keys():
    nums[key].append("or so")
    print(nums[key])