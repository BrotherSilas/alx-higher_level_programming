#!/usr/bin/node

let count = 0; // to keep track of the number of calls

exports.logMe = function(item) {
	console.log(`${count}: ${item}`);
	count++; // count increment after previous printing
};
