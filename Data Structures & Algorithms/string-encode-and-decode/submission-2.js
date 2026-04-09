class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let finalString = ""
         strs.map(el => {
            finalString = finalString + el + "0xC0"
         })
         return finalString
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
       if(str.length == 4){
        return [""]
       }
        let convertedArr = str.split("0xC0")
        console.log(convertedArr)
       return convertedArr.slice(0, convertedArr.length - 1)
    }
}
