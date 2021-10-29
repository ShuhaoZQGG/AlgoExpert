/*
5. Longest Palindromic Substring
Medium

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
*/
const getPalindrome = function(s, left, right) {
  let i = 0;
  while (s[left - i] && s[left - i] === s[right + i]) {
    i++;
  }
  i--;
  return s.slice(left - i, right + i + 1)
}

const longestPalindrome = function(s) {
  // if (s.length === 0) return "";

  let  longestPalidrome = "";

  for (let i = 0; i < s.length; i++) {
    let evenPalindrome = getPalindrome(s, i, i);
    let oddPalindrome = getPalindrome(s, i-1, i);

    if (evenPalindrome.length >= longestPalidrome.length) {
      longestPalidrome = evenPalindrome;
    } 
    
    if (oddPalindrome.length >= longestPalidrome.length) {
      longestPalidrome = oddPalindrome;
    }
  }

  return longestPalidrome;
}
 
console.log(longestPalindrome("abbba")) //true
console.log(longestPalindrome("mbaabm")) //true
console.log(longestPalindrome("abcddcab")) //false