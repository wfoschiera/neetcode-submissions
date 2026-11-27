class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs: string[]): string {
        let res = ""
        for (let i=0; i<strs.length; i++) {
            res = res + strs[i] + "#_#"
        }
        return res
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str: string): string[] {
        let res = str.split("#_#")
        res.pop()
        return res
    }
}
