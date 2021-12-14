#!/usr/bin/node
const sq = require('./5-square');
module.exports = class Square extends sq {
  charPrint (c) {
    let a = '';
    for (let step = 0; step < this.height; step++) {
      for (let paso = 0; paso < this.width; paso++) {
        if (!c) {
          a += 'X' + '';
        } else {
          a += 'C' + '';
        }
      }
      console.log(a);
      a = '';
    }
  }
};
