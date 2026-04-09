class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let arr = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase(); 
        console.log(arr)
             let i  = 0;
        let j = arr.length - 1
        while(i < j){
            if(arr[i] != arr[j]){
                return false
            }else{
                i++;
                j--;
            }
        }
        return true
    }
}
