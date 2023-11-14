#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width !== 0 && this.height !== 0) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate () {
    if (this.width !== 0 && this.height !== 0) {
      // Exchange width and height
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double () {
    if (this.width !== 0 && this.height !== 0) {
      // Double width and height
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
