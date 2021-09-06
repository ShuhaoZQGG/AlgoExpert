/*
Sample Input
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Output
[1, 4, 9, 16, 25, 49, 64, 81]
*/
const sortedSquaredArray = function(array){
  array.sort((a,b) => a - b)
  return array.map(el => Math.pow(el,2));
}
const array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
const array_2 = [2, 10, 5, 3, 1, 9];

console.log(sortedSquaredArray(array));
console.log(sortedSquaredArray(array_2));