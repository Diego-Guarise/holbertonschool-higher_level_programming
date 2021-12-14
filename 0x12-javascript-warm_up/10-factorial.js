#!/usr/bin/node
function factorial (i) {
  const num = parseInt(i);
  if (isNaN(num) || i === 1) {
    return 1;
  }
  return (i * factorial(num - 1));
}
console.log(factorial(process.argv[2]));
