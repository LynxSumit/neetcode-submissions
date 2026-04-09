class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
         const res = []
         nums.sort((a,b) => a-b)
        for(let i = 0; i<nums.length; i++){
            if(i > 0 && nums[i] == nums[i-1])
            continue;
            let j = i+1; let k = nums.length - 1;
            while(j < k){
                if(nums[i] + nums[j] + nums[k] > 0){
                        k -= 1
                }else if(nums[i] + nums[j] + nums[k] < 0){
                    j += 1
                }
                else{

                res.push([nums[i], nums[j], nums[k]])
                j += 1
                while(nums[j] == nums[j-1] && j < k){
                    j+=1
                }
                }
            }
        }
        return res
    }

}
