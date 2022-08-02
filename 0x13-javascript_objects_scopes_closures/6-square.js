#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    const char = !c ? 'X' : c;
    for (let i = 0; i < this.width; i++) {
      console.log(char.repeat(this.width));
    }
  }
}
module.exports = Square;
