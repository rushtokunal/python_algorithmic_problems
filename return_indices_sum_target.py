def getIndices(nums,target):
    print(nums)
    res_indices={}
    for index,number in enumerate(nums):
        if target-number in res_indices:
            return (res_indices[target-number],index)
        res_indices[number]=index
input_data=[2,7,8,5,7]
target=9
res=getIndices(input_data,target)
print(res)
#expected o/p [0,1]