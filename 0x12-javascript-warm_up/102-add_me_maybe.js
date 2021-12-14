#!/usr/bin/node
exports.callMeMoby = function (x, back) {
  x = x + 1;
  back(x);
};
