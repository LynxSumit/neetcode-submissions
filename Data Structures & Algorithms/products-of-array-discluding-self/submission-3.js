class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let productOfAll  = 1;
        let zerosCount = 0;
        nums.map(num => {
            if(num == 0){
                zerosCount++
            }else{
            productOfAll = productOfAll * num
            }
        })
        let output = nums.map(num => {
            if(zerosCount > 1){
                return 0
            }
            if(zerosCount == 1){
                return num == 0 ? productOfAll : 0
            }
            return productOfAll / num
        })
        return output
    }
}
