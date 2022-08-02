#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const char = !c ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}
module.exports = Square;
