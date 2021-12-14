#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (h <= 0 || w <= 0 || !h || !w) {
      return;
    }
    this.width = w;
    this.height = h;
  }
};