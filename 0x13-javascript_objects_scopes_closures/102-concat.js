#!/usr/bin/node

const fs = require('fs').promises;
async function concatFiles (pathFileA, pathFileB, pathFileC) {
  try {
    const fileA = await fs.readFile(pathFileA, 'utf8');
    const fileB = await fs.readFile(pathFileB, 'utf8');
    const fileC = fileA + fileB;

    await fs.writeFile(pathFileC, fileC);
    console.log('files have been concat successsfully.');
  } catch (error) {
    console.error('Error while concatenating files: ', error);
  }
}
concatFiles('fileA', 'fileB', 'fileC');
