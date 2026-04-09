class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(nums) {
        let max = 0;
        for(let i = 0; i<nums.length; i++){
            for(let j = i+1; j<nums.length;j++){
               let curr_max  = Math.min(nums[i], nums[j]) * (j - i)
                max = Math.max(curr_max, max)
            }
        }
        return max
    }
}
