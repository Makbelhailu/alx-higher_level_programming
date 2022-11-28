#!/us4/bin/node
// import { argv } from 'node:process';
const argv = process.argv;
const x = argv.length;
if (x === 2) {
  console.log('No argument');
} else if (x === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
