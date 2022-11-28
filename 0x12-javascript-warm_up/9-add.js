#!/usr/bin/node
const num1 = process.argv[2];
const num2 = process.argv[3];

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return a + b;
}

console.log(add(num1, num2));
