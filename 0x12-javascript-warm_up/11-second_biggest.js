#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const list = process.argv.slice(2);
  list.sort((a, b) => a - b);
  console.log(list[list.length - 2]);
}
