class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        l = list(s)
        l.sort()
        n = len(l)
        nums[:n]=l
        return n
#####java#####
class Solution {
    public int removeDuplicates(int[] nums) {
        // 使用双指针
        if(nums==null || nums.length == 1){
            return nums.length;
        }
        int i = 0,j =1;
        while(j<nums.length){
            if(nums[i]==nums[j]){
                j++;
            }else{
                i++;
                nums[i]=nums[j];
                j++;
            }
        }
        return i+1;
    }
}