#!/usr/bin/node
const args = process.argv;
let a = '';
if (parseInt(args[2])) {
  for (let step = 0; step < args[2]; step++) {
    for (let paso = 0; paso < args[2]; paso++) {
      a += 'X' + '';
    }
    console.log(a);
    a = '';
  }
} else {
  console.log('Missing size');
}
