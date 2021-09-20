function powerset(inputArray) {
  // Write your code here.
  let result = []
  result.push(inputArray);
  const doPowerSet = function(array){
	for (let i =0; i < array.length; i++) {
		const right = array.slice(0, i).concat(array.slice(i+1, array.length));
			result.push(right);
			doPowerSet(right);
	}
  }
  doPowerSet(inputArray);
  let newResult = [];
  for (const el of result){
    if (el.length !== 0){
    newResult.push(el.join(','));
    }
  }
  newResult = [...new Set(newResult)];
  let finalResult = [];
  for (const el of newResult){
    finalResult.push(el.split(','));
  }
  finalResult = finalResult.map(el => el.map(el => Number(el)))
  finalResult.push([]);
	return finalResult;
}

// Do not edit the line below.
exports.powerset = powerset;

console.log(powerset([1,2,3,4]))