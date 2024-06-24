#!/usr/bin/node

// Getting the first argument from command line
const {argv} = require('process');

// Converting the first argument to an integer
const x = parseInt(argv[2], 10);

// can argument be converted to an integer?
if (isNaN(x)) {
	console.log('Missing number of occurrences');
} 

else {
// Using for loop to print "C is fun" x times
    for (let i = 0; i < x; i++) {
        console.log("C is fun");
    }
}
