#!/usr/bin/node
exports.callMeMoby = function (x, back) {
  for (let i = 0; i < x; i++) {
    back(x);
  }
};
