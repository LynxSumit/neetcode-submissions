class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length != t.length){
            return false;
        }
        let char_freq = {}

        s.split("").map((el) => {
            if(char_freq[el.toString()]){
                char_freq[el.toString()] += 1
            }else{
                char_freq[el.toString()] = 1
            }
        })

        // by here we get all the characters of s and their respected frequencies in char_freq e.g.

        // char_freq = {
        //     's' : 5,
        //     'g' : 2,
        //     ...
        // } // now we'll simply decrement this while looping out the t string

        t.split("").map((el) => {
             if(char_freq[el.toString()]){
                char_freq[el.toString()] -= 1
            }else{
                char_freq[el.toString()] = 1
            }
        })

        // now that in ideal condition there should be all the characters frequesncies will be zero 

        let converted_char_freqs_into_arr = Object.keys(char_freq).map((key) => [key, char_freq[key]]);
        for(let el of converted_char_freqs_into_arr){
            if(el[1] != 0){
                return false
            }
        }

        return true;
    }
}

