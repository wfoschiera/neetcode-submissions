class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        let count: Map<number, number> = new Map();
        let freq: number[][] = Array.from({ length: nums.length + 1 }, () => []);

        // cria um map entre o número e a quantidade de vezes que ele aparece
        for (const num of nums) {
            count.set(num, (count.get(num) || 0) + 1);
        }
        // no array de arrays, sobrescreve a posição(frequencia), pelo numero.
        // assim, consigo iterar do último valor para o primeiro até completar k valores
        count.forEach((value, key) => {
            freq[value].push(key);
        });

        let res: Array<number> = []
        for (let i = freq.length - 1; i >= 0; i--){
            for (const f of freq[i]){
                res.push(f)
                if (res.length == k) {
                    return res
                }
        
            }
        }
        return res
    }
}
