class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
     longestConsecutive(nums) {
    let numSet = new Set(nums); // Add all numbers to a set for quick lookups
    let longestStreak = 0;

    for (let num of numSet) {
        // Start a sequence only if `num - 1` doesn't exist (i.e., it's the start of a sequence)
        if (!numSet.has(num - 1)) {
            let currentNum = num;
            let currentStreak = 1;

            // Count consecutive numbers
            while (numSet.has(currentNum + 1)) {
                currentNum += 1;
                currentStreak += 1;
            }

            // Update the longest streak
            longestStreak = Math.max(longestStreak, currentStreak);
        }
    }

    return longestStreak;
}

}
