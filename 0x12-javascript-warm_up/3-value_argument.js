#!/usr/bin/node

const { argv } = require('process');

const initialArg = argv[2];

if (initialArg === undefined) {
  console.log('No argument');
} else {
  console.log(initialArg);
}
