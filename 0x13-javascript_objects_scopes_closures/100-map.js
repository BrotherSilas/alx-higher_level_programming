#!/usr/bin/node

//  importing list
const { list } = require('./100-data.js');

// creating new array with map function
// current list values = old list value * index
const currentList = list.map((value, index) => value * index);

// print initial and new list
console.log(list);
console.log(currentList);
