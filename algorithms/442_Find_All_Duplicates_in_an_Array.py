#---------Tags---------
#Array
#----------------------

#---------Notes---------
# Trick to use minus to note the status
#-----------------------

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """        
        res = []
        for n in nums:
            if nums[abs(n) - 1] < 0:
                res.append(abs(n))
            else:
                nums[abs(n)-1] *= -1
        
        return res


# C version
# /**
#  * Return an array of size *returnSize.
#  * Note: The returned array must be malloced, assume caller calls free().
#  */
# int* findDuplicates(int* nums, int numsSize, int* returnSize) {
    
#     if(nums==NULL||numsSize<2)
#     {
#         *returnSize=0;
#         return NULL;
#     }
#     int *result = (int *)malloc(sizeof(int)*numsSize);
#     int idx = 0;
#     for(int i=0;i<numsSize;i++){
#         if(nums[abs(nums[i])-1] < 0){
#             result[idx] = abs(nums[i]); 
#             idx += 1;
#         }else{
#             nums[abs(nums[i])-1] *= -1;
#         }
#     }
#     *returnSize = idx;
#     return result;
# }