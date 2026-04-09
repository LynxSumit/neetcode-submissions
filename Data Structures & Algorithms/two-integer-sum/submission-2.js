class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let res = [];

       for(let i = 0; i < nums.length; i++ ){
            let el = nums[i];
            for(let j = i+1; j<nums.length; j++){
                let el2 = nums[j]
                if(el + el2 == target){
                    return [i, j]
                }
            }    
        
       }

       return res;
    }
}
