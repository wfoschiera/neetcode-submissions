class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        let difMap: Map<number, number> = new Map();

        for (let i = 0; i < nums.length; i++) {
            let dif = target - nums[i]
            let exists = difMap.has(nums[i])
            if (!!exists) {
                return [difMap.get(nums[i]), i]
            }
            difMap.set(dif, i);
        }
    }
}
