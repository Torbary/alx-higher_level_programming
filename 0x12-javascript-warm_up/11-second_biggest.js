#!/usr/bin/node

function secondBiggest (args) {
  const nums = Array.from(args).sort((a, b) => b - a);

  if (nums.length < 2) {
    return 0;
  }

  return nums[1];
}

const result = secondBiggest(process.argv.slice(2));
console.log(result);
