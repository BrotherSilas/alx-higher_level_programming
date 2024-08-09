#!/usr/bin/node

const { argv } = require('process');

const initialArg = argv[2];
const nextArg = argv[3];

if (initialArg === undefined) {
  console.log('undefined is undefined');
} else if (nextArg === undefined) {
  console.log(initialArg + ' is undefined');
} else {
  console.log(initialArg + ' is ' + nextArg);
}
