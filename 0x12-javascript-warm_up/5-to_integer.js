#!/usr/bin/node
const args = process.argv;
if (Number(args[2])) {
  const x = parseInt(args[2]);
  console.log('My number:', x);
} else {
  console.log('Not a number');
}
