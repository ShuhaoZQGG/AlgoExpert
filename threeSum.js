const twoSum_2 = function(array, targetSum){
  let reminder;
  for (let i = 0; i < array.length; i++){
    reminder = targetSum - array[i];
    if (array.indexOf(reminder) != i){
     if (array.indexOf(reminder) != -1){
        return [array[array.indexOf(reminder)],array[i]];
     }
   }
  }
}
function multiDimensionalUnique(arr) {
  var uniques = [];
  var itemsFound = {};
  for(var i = 0, l = arr.length; i < l; i++) {
      var stringified = JSON.stringify(arr[i]);
      if(itemsFound[stringified]) { continue; }
      uniques.push(arr[i]);
      itemsFound[stringified] = true;
  }
  return uniques;
}

const threeSum = function(array, targetSum){
  let answer = [];
  let reminder = [];
  for (let i = 0; i < array.length; i++){
    reminder.push(targetSum - array[i]);
  }
  // reminder = [-12, -3, -1, -2, 6, -5, 8, -6];
  console.log(reminder.length);
  for (let i = 0; i < reminder.length; i++){
    let arrayCopy = array.slice(0, i).concat(array.slice(i+1,array.length));
    if (twoSum_2(arrayCopy, reminder[i]) != undefined){
      answer.push(twoSum_2(arrayCopy, reminder[i]));
      answer.push(array[i])
    };

  }

  for (let i = 0; i < answer.length; i+=2){
    answer[i].push(answer[i+1]);
  }

  for (let i = 0; i < answer.length; i++){
    answer.splice(i+1,1)
  }

  for(let i = 0; i < answer.length; i++){
    answer[i].sort((a,b)=>a-b);
  }

  answer = multiDimensionalUnique(answer);

  
  return answer;
}

/*
Sample Input
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

Smaple Output
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
*/

// [-3, -1, -2, 6, -5, 8, -6], -12, [12, , ]
// [-12, -1, -2, 6, -5, 8, 6], -3   [3, ,]
/*
 [3, 1, 2, -6, 5, -8, 6], 8, [-8, ,]
 [5, 7, 6, 14, 3, 16, 6], [-8, 2, 6], [-8, 3, 5]
*/

const array = [12, 3, 1, 2, -6, 5, -8, 6];
const targetSum = 0;
console.log(threeSum(array, targetSum))