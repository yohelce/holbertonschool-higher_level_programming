#!/usr/local/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const array = process.argv.slice(2);
  const secondBig = array.sort((a, b) => a - b);
  console.log(secondBig[secondBig.length - 2]);
}
