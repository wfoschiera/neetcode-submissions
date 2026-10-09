class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {

        let hashmap: Map<string, string[]> = new Map();
        for (let i = 0; i < strs.length; i++) {
            const word = strs[i]
            let count = new Array<number>(26).fill(0)

            for (let i = 0; i < word.length; i++) {
                count[word.charCodeAt(i) - 'a'.charCodeAt(0)]++;
            }
            const key = count.toString()
            hashmap.set(key, (hashmap.get(key) ||[]).concat([word]))
        }
        return Array.from(hashmap.values())
    }
}