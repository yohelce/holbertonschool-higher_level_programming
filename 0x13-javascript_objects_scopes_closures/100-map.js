#!/usr/local/bin/node
const { list } = require('./100-data');

const newArray = list.map((num, i) => num * i);

console.log(list);
console.log(newArray);
