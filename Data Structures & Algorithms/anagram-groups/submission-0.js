class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
   

        let res = {}
        strs.forEach((el) => {
           let sorted_str =  el.split('').sort().join('')
            if(!res[sorted_str]){
                res[sorted_str] = []
            }
            res[sorted_str].push(el)
        })

        return Object.values(res);
       
    }
}
