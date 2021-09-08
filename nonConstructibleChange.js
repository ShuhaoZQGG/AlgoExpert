/*
Give an array of positive integers representing the values of coins in your progression,
write a function that returns the minimum amount of change (the minimum sum of money)
that you CANNOT create. The given coins can have any positive integer value and aren't
necessarily unique. (i.e you can have multiple coins of the same value)

For example, if you are given coins = [1, 2, 5], the minimum amount of change you cannout create
is 4. If you are given no coins, the minimum amount of change you cannot create is 1

Sample Input 
coins = [5, 7, 1, 1, 2, 3, 22]

Sample Output
20
*/

// Solution 1 has bug, should start from the smallest number instead of the largest
const nonConstructibleChange_1 = function(coins){
  if (coins[0] == null || undefined){
      return null;
    }

  else{
    coins = coins.sort((a,b) => a - b);
    let sum = 0;
    let max = coins[coins.length - 1];
    for (let i = 0; i < coins.length-1; i++){
      if (i>=0){
        sum += coins[i];
      }
    }
    coins.splice(coins.length-1, 1)

    if (sum + 1 >= max){
      return sum+max+1;
    }

    else{
      return nonConstructibleChange(coins);
    }
  }  
}

//Solution 2: correct answer
const nonConstructibleChange_2 = function(coins){
  coins.sort((a,b) => a-b);

  let currentChange = 0;
  for (const coin of coins){
    if (coin > currentChange + 1){
      return currentChange +1;
    }
    else{
      currentChange += coin;
    }
  }
  return currentChange + 1;
}
//const coins = [1, 2, 5, 6]

const coins = [5, 7, 1, 1, 2, 3, 21];  //20
const coins_1 = [109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4] //87
const coins_2 = [1, 2, 3, 4, 5, 6, 7] //29
const coins_3 = [1,1] //3
const coins_4 = [];  //0
const coins_5 = [0];  //1
const coins_6 = [6, 4, 5, 1, 1, 8, 9] // [1, 1, 4, 5, 6, 8, 9]

console.log(nonConstructibleChange_2(coins));
console.log(nonConstructibleChange_2(coins_1));
console.log(nonConstructibleChange_2(coins_2));
console.log(nonConstructibleChange_2(coins_3));
console.log(nonConstructibleChange_2(coins_4));
console.log(nonConstructibleChange_2(coins_5));
console.log(nonConstructibleChange_2(coins_6));