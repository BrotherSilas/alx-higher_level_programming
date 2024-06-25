#!/usr/bin/node

const { argv } = require('process');

// If no argument is passed or the number of arguments is 1, print 0
if (argv.length <= 3) {
  console.log(0);
} else {
// Convert arguments to integers
  // then remove the first two elements (node and script path)
  const args = argv.slice(2).map(Number);

  // Find the highest integer
  const highest = Math.max(...args);

  // Remove all occurrences of the highest integer
  const filteredArgs = args.filter(numb => numb !== highest);

  // Find the second highest integer
  const secondHighest = Math.max(...filteredArgs);

  console.log(secondHighest);
}
