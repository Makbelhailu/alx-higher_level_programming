#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const X = 'X';
    for (let x = 0; x < this.height; x++) { console.log(X.repeat(this.width)); }
  }
};
