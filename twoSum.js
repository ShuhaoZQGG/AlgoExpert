
//Solution 1
const twoSum_1 = function(array, targetSum){
  let compliment = [];
  let reminder;
  for (let i = 0; i < array.length; i++){
    compliment.push(targetSum - array[i]); 
    // [7, 5, 14, 2, -1, 9, 11, 4]
    // [3, 5, -4, 8, 11, 1, -1, 6]  
    for (let j = 0; j < compliment.length; j++){
      if(i != j){
        if (array[i] == compliment[j]){
          return [array[i],array[j]];
        }
      }
    }
  }
}


// Solution 2
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

const twoSum_3 = function(array, targetSum){
  array.sort((a,b)=> a-b);
  let left = 0;
  let right = array.length-1;
  let answer = new Array();
  while(right > left){
    if (array[right] + array[left] > targetSum){
      right--;
    }
    else if (array[right] + array[left] < targetSum){
      left ++;
    }
    else{
      answer.push(array[left],array[right])
      return answer;
    }
    }
  
}
/*
Sample input
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

Sample output
[-1, 11]
*/
const array = [3, 5, -4, 8, 11, 1, -1, 6];
const targetSum = 10;
console.log(twoSum_1(array,targetSum))
console.log(typeof(twoSum_1(array,targetSum)))

console.log(twoSum_2(array,targetSum))
console.log(twoSum_3(array,targetSum))
