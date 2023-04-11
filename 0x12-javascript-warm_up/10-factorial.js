#!/usr/bin/node

const factorial = (num) => {
  if (isNaN(num) || num < 0) {
    return 1;
  }

  if (num === 0 || num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
};

const num = process.argv[2];
const result = factorial(parseInt(num));
console.log(result);
