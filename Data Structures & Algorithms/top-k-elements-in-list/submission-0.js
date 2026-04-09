class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let map = {}
        
        nums.forEach(el => {
            if(map[el.toString()]){
               map[el.toString()] += 1
            }else{
                map[el.toString()] = 1
            }
        });
            console.log(map)
        let sortedArr =  Object.entries(map).sort((a, b) => b[1] - a[1]);
        let res = []
        for(let i = 0; i<k ; i++){
            res.push(sortedArr[i][0])
        }

      return res;
    }
}
