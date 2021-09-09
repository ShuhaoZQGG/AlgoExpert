/*
Sample Input
array = [1, 2, 3]

Sample Output
[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
*/

const permutation = (inputArr) => {
  let result = [];

  const permute = (arr, permutated = []) => {
    if (arr.length === 0) {
      result.push(permutated)
    } else {
      for (let i = 0; i < arr.length; i++) {
        let current = arr.slice();
        let next = current.splice(i, 1);
        permute(current, permutated.concat(next))
     }
   }
 }

 permute(inputArr)

 return result;
}

const array_1 = [3];
const array_2 = [1,2,3,4]
const array_3 = ['a','b','c']

console.log(permutation(array_1));
console.log(permutation(array_2));
console.log(permutation(array_3));
