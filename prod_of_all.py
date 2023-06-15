def product(nums):
    prefix = [nums[0]]
    postfix = [nums[-1]]
    ans = []
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] * nums[i])
    for i in range(len(nums) - 2, -1, -1):
        postfix.insert(0, postfix[0] * nums[i])
    for i in range(len(nums)):
        if i == 0:
            ans.append(1*postfix[i+1])
        elif i == len(nums)-1:
            ans.append(prefix[i-1]*1)
        else:
            ans.append(prefix[i-1]*postfix[i+1])
    return ans

nums = [1,2,3,4] 
print(product(nums))