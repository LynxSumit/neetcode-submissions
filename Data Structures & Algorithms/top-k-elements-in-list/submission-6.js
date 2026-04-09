class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        // let map = {};
        // nums.map(num => {
        //     if(map[num]){
        //         map[num] += 1;
        //     }else{
        //         map[num] = 1
        //     }
        // })
        // let res = Object.entries(map).sort((a, b) => b[1] - a[1]).map(item => item[0])
        // return res.slice(0,k)

        let map = {};
    let freq = Array.from({ length: nums.length + 1 }, () => []);

    // Count frequency
    nums.forEach(num => {
        map[num] = (map[num] || 0) + 1;
    });

    // Bucket sort
    Object.entries(map).forEach(([num, count]) => {
        freq[count].push(parseInt(num));
    });

    let res = [];
    for (let i = freq.length - 1; i >= 0 && res.length < k; i--) {
        for (let num of freq[i]) {
            res.push(num);
        }
    }

    return res.slice(0, k);
    }
}
