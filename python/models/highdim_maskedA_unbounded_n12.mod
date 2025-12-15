# Generated AMPL model

var x1;
var x2;
var x3;
var x4;
var x5;
var x6;
var x7;
var x8;
var x9;
var x10;
var x11;
var x12;

minimize obj: x1^8*((x2^2 + x3^2 + x4^2 + x5^2 + x6^2 + x7^2 + x8^2 + x9^2 + x10^2 + x11^2 + x12^2) - 1)^2 - (x1^2*(x2^2 + x3^2 + x4^2 + x5^2 + x6^2 + x7^2 + x8^2 + x9^2 + x10^2 + x11^2 + x12^2))^2 - x1;

subject to c1: x2^2 + x3^2 + x4^2 + x5^2 + x6^2 + x7^2 + x8^2 + x9^2 + x10^2 + x11^2 + x12^2 - x1 <= 0;
subject to c2: 1 - (x2^2 + x3^2 + x4^2 + x5^2 + x6^2 + x7^2 + x8^2 + x9^2 + x10^2 + x11^2 + x12^2) <= 0;
