#!/usr/bin/node
const p = 'C is fun';
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < num; x++) {
    console.log(p);
  }
}
