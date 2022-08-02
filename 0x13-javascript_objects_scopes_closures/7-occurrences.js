#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let flag = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      flag += 1;
    }
  }
  return (flag);
};
