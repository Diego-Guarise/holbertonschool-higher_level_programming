#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let sum = 0;
  for (let i = 0; list[i]; i++) {
    if (searchElement === list[i]) {
      sum++;
    }
  }
  return (sum);
};
