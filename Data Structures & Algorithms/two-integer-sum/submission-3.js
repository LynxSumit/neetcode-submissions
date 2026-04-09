class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */

    // {
        // 3 : 0,
        // 4 : 1,
        // 5 : 2,
        // 6 : 3
    // }
    twoSum(nums, target) {
   let obj = {}
   for(let i = 0; i<nums.length; i++ ){
    let needed = target - nums[i];
    console.log(needed)
    if(obj[needed.toString()] ){
        
        return [ obj[needed.toString()] - 1, i]
    }else{
    
             obj[nums[i].toString()] = i +1
       
    }
   }
    return [-1,-1];
    }
}
