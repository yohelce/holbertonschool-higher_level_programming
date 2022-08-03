#!/usr/local/bin/node

const { dict } = require('./101-data');

const newArray = Object.entries(dict);
const newObj = {};
for (const elem of newArray) {
  if (newObj[elem[1]]) {
    newObj[elem[1]].push(elem[0]);
  } else {
    newObj[elem[1]] = [elem[0]];
  }
}
console.log(newArray);
