#!/usr/bin/node

// import dict
const { dict } = require('./101-data.js');
const newDict = {};

// Iterate through the original dictionary
for (const [userId, occurrences] of Object.entries(dict)) {
  // If the occurrence number doesn't exist as a key, create an empty array
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  // Add the user id to the array for this occurrence number
  newDict[occurrences].push(userId);
}

// Print the new dictionary
console.log(newDict);
