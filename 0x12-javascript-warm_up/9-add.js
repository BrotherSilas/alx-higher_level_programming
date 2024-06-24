#!/usr/bin/node

const { argv } = require('process');

function add (a, b) {
  return a + b;
}

// Get the first and second arguments and convert them to integers
const a = parseInt(argv[2], 10);
const b = parseInt(argv[3], 10);

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}
