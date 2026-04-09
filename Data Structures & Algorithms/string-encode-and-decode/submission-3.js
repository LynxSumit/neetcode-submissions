class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let res = ""
        strs.forEach(str => {
            res += str.length.toString() + "#" + str
        })
        return res
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        console.log(str)
        let i = 0
        let res = []
        while(i < str.length){
            let j = i;
            while(str[j] != "#"){
                j += 1
            }
            let length = parseInt(str.substring(i,j))
            res.push(str.substring(j+1, j+1+ length))
            i = j + 1 + length;
        }
        return res
    }
}
