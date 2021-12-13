#!/usr/bin/node
const args = process.argv.length;
if (args === 3) {
  console.log('Argument found');
} else if (args === 4) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
