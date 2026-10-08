class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length != t.length) {
            return false;
        }
        let countS: Map<string, number> = new Map();
        let countT: Map<string, number> = new Map();

        for (let i=0; i<s.length; i++) {
            countS[s[i]] = (countS[s[i]] || 0) + 1;
            countT[t[i]] = (countT[t[i]] || 0) + 1; 
        } 
        for (const key in countS) {
            if (countS[key] !== countT[key]) {
                return false;
            }
        }
        return true;
    }
}
//         let hashmap: Map<String, number> = new Map();
//         t.split("").forEach((char) => {
//             let exists = hashmap.has(char);
//             if (exists) {
//                 let cnt = hashmap.get(char);
//                 hashmap.set(char, cnt + 1);
//             } else {
//                 hashmap.set(char, 1);
//             }
//         });
//         console.log(hashmap)
//         for (const c of s) {
//             let exists = hashmap.has(c);
//             if (!exists) {
//                 return false;
//             } else {
//                 let cnt = hashmap.get(c);
//                 if (cnt <= 0) {
//                     return false;
//                 }
//                 hashmap.set(c, cnt - 1);
//             }
//         }
//         return true;
//     }
// }
