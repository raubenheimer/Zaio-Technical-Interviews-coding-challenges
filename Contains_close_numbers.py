def containsCloseNums(nums, k):
    z = 0
    for i in range((len(nums)-k)):
        if nums[i] == nums[i+k]:
            print('True')
            z = 1
            break
    if z == 0:
        print('False')

containsCloseNums([0,1,2,3,5,2], 3)
containsCloseNums([0,1,2,3,5,2], 2)
containsCloseNums([0,1,2,3,5,0], 5)
containsCloseNums([0,1,2,3,5,6,2,0,9,10,11,12], 7)
containsCloseNums([1,1,1,1,1,1,0,0,0,0,0,0], 7)
