#!/usr/bin/mode

exports.esrever = function (list) {
  const backwards = [];
  for (let i = list.length - 1; i >= 0; i--) {
    backwards.push(list[i]);
  }
  return backwards;
};
