#!/usr/bin/node
exports.addMeMaybe = function (x, back) {
  x = x + 1;
  back(x);
};
