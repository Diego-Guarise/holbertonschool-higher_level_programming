#!/usr/bin/node
exports.esrever = function (list) {
  const listar = [];
  if (list) {
    for (let i = 0; i < list.length; i++) {
      listar.unshift(list[i]);
    }
    return listar;
  }
};
