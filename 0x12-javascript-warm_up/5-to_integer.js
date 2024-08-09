#!/usr/bin/node

const { argv } = require('process'); // Importing argv from the process module

// Check if there's at least one argument provided after the script name
if (argv.length < 3) {
  console.log('Not a number');
} else {
  const initialArg = argv[2]; // Get the first argument
  const numberConverted = parseInt(initialArg, 10); // Convert the first argument to an integer using base 10

  // Check if the conversion resulted in a number or NaN (Not a Number)
  if (isNaN(numberConverted)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${numberConverted}`); // Print the converted number
  }
}
