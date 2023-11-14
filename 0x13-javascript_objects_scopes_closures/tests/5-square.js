#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // Call constructor of Rectangle with sizes for both height and width
    super(size, size);
  }
}

module.exports = Square;
