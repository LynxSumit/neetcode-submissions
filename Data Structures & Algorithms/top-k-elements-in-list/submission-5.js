class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let map = {};
        nums.map(num => {
            if(map[num]){
                map[num] += 1;
            }else{
                map[num] = 1
            }
        })
        let res = Object.entries(map).sort((a, b) => b[1] - a[1]).map(item => item[0])
        return res.slice(0,k)
    }
}
