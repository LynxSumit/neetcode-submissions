class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(nums) {
        // Brute Force Approach
        // let max = 0;
        // for(let i = 0; i<nums.length; i++){
        //     for(let j = i+1; j<nums.length;j++){
        //        let curr_max  = Math.min(nums[i], nums[j]) * (j - i)
        //         max = Math.max(curr_max, max)
        //     }
        // }
        // return max
        let max = 0;
         let i = 0; 
         let j = nums.length - 1;
         while(i  < j){
            let curr_area = Math.min(nums[i], nums[j]) * (j - i)
            max = Math.max(max , curr_area);
            if(nums[j] > nums[i]){
                i++
            }else{
                j--
            }
         }
         
   return max
    }
}
