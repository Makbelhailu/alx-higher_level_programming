#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(1);
} else {
  const arg = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a + b);
  console.log(arg[1]);
}
