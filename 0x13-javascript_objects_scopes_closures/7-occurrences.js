#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, more) => more === searchElement ? count++ : count, 0);
};
