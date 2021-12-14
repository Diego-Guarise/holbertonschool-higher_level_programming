#!/usr/bin/node
const Square = require('./5-square');
module.exports = class Square extends Re {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
};
