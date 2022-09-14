#!/usr/bin/node
const filename = process.argv[2];
const string = process.argv[3];

const fs = require('fs');

try {
  fs.writeFile(filename, string, 'utf-8', function (err, result) { if (err) console.log(err); });
} catch (err) {
  console.log(err);
}
