#!/usr/bin/node
function factorial (x) {
  if (x === 0 || isNaN(x)) {
    return 1;
  } else {
    return (factorial(x - 1) * x);
  }
}

console.log(factorial(parseInt(process.argv[2])));
