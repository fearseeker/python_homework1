a = int(input("введить першу сторону: "))
b = int(input("введить другу сторону: "))
c = int(input("введить третю: "))
nums = [a,b,c]
def Istriangl(nums):
    if (nums[0]*nums[0]) + (nums[1]*nums[1]) == nums[2]*nums[2] or (nums[1]*nums[1]) + (nums[2]*nums[2]) == nums[0]*nums[0] or (nums[2]*nums[2]) + (nums[1]*nums[1]) == nums[0]*nums[0]:
        print("True")
    else:
        print("False")
Istriangl(nums)
