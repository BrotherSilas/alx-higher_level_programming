#!/usr/bin/node

const { argv } = require('process');

// Get the first argument and convert it to an integer
const size = parseInt(argv[2], 10);

// checks if the conversion to an integer was successful
if (isNaN(size)) {
  console.log('Missing size');
} else {
// If the size is valid, use a for loop to print the square
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
