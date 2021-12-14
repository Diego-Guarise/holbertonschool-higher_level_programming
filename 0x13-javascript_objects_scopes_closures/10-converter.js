#!/usr/bin/bash
exports.converter = function (base) {
  function Number (n) {
    return n.toString(base);
  }
  return Number;
};
