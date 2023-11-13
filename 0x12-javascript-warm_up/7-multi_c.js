#!/usr/bin/node

const times = process.argv[2];
const num = parseInt(times, 10);

if (!isNaN(num)) {
  for (let i = 0; i < num; i++) { console.log('C is fun'); }
} else {
  console.log('Missing number of occurrences');
}
