// 3. Longest Substring Without Repeating Characters
// Given a string s, find the length of the longest substring without repeating characters.

/*
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
*/
// Brute force method
const lengthOfLongestSubstring = function(s) {
  let len = 1;

  if (s.length === 0) return 0;

  for (let i = 0; i < s.length; i++) {
    let c = s[i];
    let arr = [c];

    for (let j = i+1; j < s.length; j++) {
      let c = s[j];
      if (arr.includes(c)) {
        break;
      } else {
        arr.push(c);
      }

      len = Math.max(len, arr.length);
    }
  }

  return len;
};

// Sliding Window method

const lengthOfLongestSubstring_2 = function(s) {
  let len = 0;
  let leftPtr = 0;
  let rightPtr = 0;
  let set = new Set();

  while (leftPtr < s.length && rightPtr < s.length) {
    if (!set.has(s[rightPtr])) {
      set.add(s[rightPtr]);
      rightPtr ++;
      len = Math.max(len, rightPtr - leftPtr);
    } else {
      set.delete(s[leftPtr]);
      leftPtr ++;
    }
  }

  return len;
};

console.log(lengthOfLongestSubstring("abcabcbb"))
console.log(lengthOfLongestSubstring("bbbbb"))
console.log(lengthOfLongestSubstring("pwwwkewwww"))
console.log(lengthOfLongestSubstring("aab"))
console.log(lengthOfLongestSubstring("dvdf"))
console.log(lengthOfLongestSubstring(""))