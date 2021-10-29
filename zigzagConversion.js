const convert = function(s, numRows) {
    const arr = new Array(numRows);
    let answer = "";
    if (numRows === 1) {
      answer = s;
      return answer;
    }
    for (let i = 0; i < numRows; i++) {
      arr[i] = new Array(Math.ceil(s.length / 2));
    }

    for (let i = 0; i < numRows; i++) {
      for (let j = i; j < s.length; j += 2 * numRows - 2) {
        arr[i][(j-i) / 2] = s[j];
      }
    }
    
    for (let i = 1; i < numRows; i++) {
      for (let j = numRows - i - 1; j < s.length; j+= 2 * numRows - 2) {
        if (j <= numRows - i) arr[i][j] =  s[j+numRows-1];
        else arr[i][(j+ numRows - i -1) / 2] = s[j+numRows-1];
      }
    }
    
    for(let i = 0; i < arr.length; i++) {
      for(let j = 0; j < arr[i].length; j++) {
        if (arr[i][j]) answer += (arr[i][j])
      }
    }

    return answer;
};

console.log(convert("ABC", 1));