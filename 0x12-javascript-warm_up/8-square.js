#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
const X = 'X';
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < num; x++) {
    let all = '';
    for (let c = 0; c < num; c++) {
      all += X;
    }
    console.log(all);
  }
}
