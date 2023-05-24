#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2]; // Read the file path from command line arguments
const content = process.argv[3]; // Read the string to write from command line arguments

fs.writeFile(filePath, content, 'utf8', function (error) {
  if (error) {
    console.error(error);
    return;
  }
  console.log('File has been written.');
});
