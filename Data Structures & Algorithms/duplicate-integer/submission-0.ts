class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const numSet = new Set<number>(nums);
        return !!(numSet.size !== nums.length);

        return;
    }
}
