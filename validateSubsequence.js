/*
Sample Input
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

Sample Output
true
*/

const validateSubsequence = function(array, sequence){
  for (let i = 0; i < sequence.length; i++){
    if (array.indexOf(sequence[i]) == -1){
      return false;
    }
  }
  return true;
}
const array = [5, 1, 22, 25, 6, -1, 8, 10]
const sequence = [-1, 6, 22, 10]
console.log(validateSubsequence(array,sequence));