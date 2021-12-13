#!/usr/bin/node
function add (a, b) {
  const sum = +a + +b;
  console.log(sum);
}
const args = process.argv;
if (args[2] && args[3]) {
  add(args[2], args[3]);
} else {
  console.log('NaN');
}
