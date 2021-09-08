  /*
  [x,[y,z]] => x * 2 * (y + z)
  [x,[y,[z]]]

  Sample Input:
  array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

  Sample Output:
  12

  5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 2 * (-13 + 8) + 4) 
  */
const levelOfDepth = function(array){
  return array[0] ? Math.max(...array.map(levelOfDepth)) + 1 : 0
}
let n = 1;
const productSum = function(array, n = 1){
  let sum = 0;

  for (let i = 0; i < array.length; i++){
    if (typeof(array[i]) == 'number'){
      sum +=  array[i];
    }
    else if (typeof(array[i]) == 'object'){
      sum += (n+1) * productSum(array[i], n + 1);
    }
    
  }
  return sum;
}

const array = [5, 2, [7, -1]] //19
const array_1 = [5, 2, [7, -1], 3] //22
const array_2 = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]; //12

console.log(productSum(array));
console.log(productSum(array_1));
console.log(productSum(array_2));
//console.log(levelOfDepth([6, [-13, 8], 4]));
