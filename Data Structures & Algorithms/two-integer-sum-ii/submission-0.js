class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
          let i = 0;
    let j = nums.length - 1;
    while(i  < j){
        if(nums[i] + nums[j] > target){
            j-= 1
        }else if(nums[i] + nums[j] < target){
            i += 1
        }else{
            return [i+1, j+1]
        }
    }

    return []
    }
}
