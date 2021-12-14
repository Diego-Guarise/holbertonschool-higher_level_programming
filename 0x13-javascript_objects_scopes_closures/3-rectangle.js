#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (h < 0 && w < 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let a = '';
    for (let step = 0; step < this.height; step++) {
      for (let paso = 0; paso < this.width; paso++) {
        a += 'X' + '';
      }
      console.log(a);
      a = '';
    }
  }
};
