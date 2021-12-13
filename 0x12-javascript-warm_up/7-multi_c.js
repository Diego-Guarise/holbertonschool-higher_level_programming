#!/usr/bin/node
const args = process.argv;
if (parseInt(args[2])) {
  for (let step = 0; step < args[2]; step++) {
    console.log('C is fun');
  }
} else if (!args[2]) {
  console.log('Missing number of occurrences');
}
