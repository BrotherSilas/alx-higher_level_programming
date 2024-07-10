#!/usr/bin/node

const fs = require('fs').promises;
async function concatFiles (pathFileA, pathFileB, pathFileC) {
  try {
    const fileA = await fs.readFile(pathFileA, 'utf8');
    const fileB = await fs.readFile(pathFileB, 'utf8');
    const fileC = fileA + fileB;

    await fs.writeFile(pathFileC, fileC);
  } catch (error) {
    process.exit(1);
  }
}

if (process.argv.length !== 5) {
  process.exit(1);
}

const [,, pathFileA, pathFileB, pathFileC] = process.argv;

concatFiles(pathFileA, pathFileB, pathFileC);
