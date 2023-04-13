#!/usr/bin/node

const fs = require('fs');
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destFile = process.argv[4];

// Read contents of the first file
const fileContents1 = fs.readFileSync(sourceFile1, 'utf8');

// Read contents of the second file
const fileContents2 = fs.readFileSync(sourceFile2, 'utf8');

// Concatenate the contents of both files
const combinedContents = fileContents1 + fileContents2;

// Write the concatenated contents to the destination file
fs.writeFileSync(destFile, combinedContents);
