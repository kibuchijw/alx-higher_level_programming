#!/usr/bin/node

exports.addMeMaybe = (number, theFunction) => {
  const incrementedNumber = number + 1;
  theFunction(incrementedNumber);
};
