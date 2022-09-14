#!/usr/bin/node
const filename = process.argv[2];
const fs = require('fs');

fs.readFile(filename, 'utf-8', function (err, result) {
  if (err) {
    console.log(err);
  } else {
    console.log(result);
  }
});
