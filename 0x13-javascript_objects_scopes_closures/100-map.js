#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const mapa = list.map(function (x, index) {
  return x * index;
});
console.log(mapa);
