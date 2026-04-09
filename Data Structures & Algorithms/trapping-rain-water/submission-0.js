class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        if(height.length == 0){
            return 0
        }
     let l = 0; 
     let r = height.length - 1;
     let res = 0;
    let leftMax = height[l], rightMax = height[r];
    while(l < r){
        if(leftMax < rightMax){
            l +=1;
            leftMax = Math.max(leftMax, height[l])
            res += leftMax - height[l]
        }else{
            r -= 1
            rightMax = Math.max(rightMax , height[r])
            res += rightMax - height[r];
                    }
    }
    return res;

    }
}
