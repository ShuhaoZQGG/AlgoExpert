/*
Sample Input
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample Output
[28,26]
*/

const smallestDifference = function(arrayOne, arrayTwo){
  arrayOne = arrayOne.sort((a,b) => a - b);
  arrayTwo = arrayTwo.sort((a,b) => a - b);

  let smallestDifference = Infinity;
  let min1 = 0;
  let min2 = 0;
  let answer = [];
  // Sorted
  // [-1, 3, 5, 10, 20, 28]
  // [15, 17, 26, 134, 135]
  let i = 0;
  let j = 0;
  let oneLength = arrayOne.length;
  let twoLength = arrayTwo.length;

  while(i < oneLength && j < twoLength){
    if (Math.abs(arrayOne[i] - arrayTwo[j]) < smallestDifference){
      smallestDifference = Math.abs(arrayOne[i] - arrayTwo[j]);
      min1 = arrayOne[i];
      min2 = arrayTwo[j];
    }
    if (arrayOne[i] < arrayTwo[j]){
      i++;
    }
    else{
      j++;
    }
   }
   return [min1, min2];
  }

let array1 = [-1, 5, 10, 20, 28, 3];
let array2 = [26, 134, 135, 15, 17];
console.log(smallestDifference(array1, array2))
