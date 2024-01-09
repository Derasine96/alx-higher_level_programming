#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint(c) {
    let row = '';
    for (let i = 0; i < this.height; i++) {
      row += c === undefined ? 'X' : c;
    }
    for (let i = 0; i < this.width; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
