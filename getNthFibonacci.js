/*
 n = 0 : 1
 n = 1 : 1
 n = 2 : 1
 n = 3 : 2
 n = 4 : 3
 n = 5 : 5
 n = 6 : 8
*/
function getNthFib(n){
  let n0 = 0;
  let n1 = 1;
  if (n == 0){
    return n0;
  }
  else if (n == 1){
    return n1;
  }
  else{
    return getNthFib(n-1) + getNthFib(n-2);
  }
}


function getNthFib_2(n){
  let a = [0, 1];
  for (let i = 0; i <= n; i++){
    if (i >= 2){
      a.push(a[i-1] + a[i-2]);
    }
  }
  return a[n];
}

function getNthFib_3(n){
  let a = [0, 1];
  for (let i = 2; i <= n; i+=2){
      a[0] = a[0] + a[1];
      a[1] = a[0] + a[1];
  }
  if (n%2 == 0){
    return a[0];
  }
  else{
    return a[1];
  }
}
console.log(getNthFib(0));
console.log(getNthFib(1));
console.log(getNthFib(2));
console.log(getNthFib(3));
console.log(getNthFib(4));
console.log(getNthFib(5));
console.log(getNthFib(6));
console.log('-----');
console.log(getNthFib_2(2));
console.log(getNthFib_2(6));
console.log('-----');
console.log(getNthFib_3(2));
console.log(getNthFib_3(3));
console.log(getNthFib_3(4));
console.log(getNthFib_3(5));
console.log(getNthFib_3(6));
console.log(getNthFib_3(7));