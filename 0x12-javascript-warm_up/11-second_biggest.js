#!/usr/bin/node

// Convert command-line arguments to integers and sort them in descending order
const args = process.argv.slice(2).map(num => parseInt(num, 10)).sort((a, b) => b - a);

if (args.length <= 1) {
  console.log(0);
} else {
  // Create a set of unique integers to find the second largest
  const uniqueNums = [...new Set(args)];
  console.log(uniqueNums[1]);
}
