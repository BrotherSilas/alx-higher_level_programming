#!/usr/bin/node

exports.logMe = function(list) {
	for (let i=0; i < list.length-1; i++) {
	  console.log(`${i}: ${list}`);
	}
};
