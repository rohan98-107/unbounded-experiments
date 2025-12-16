# Generated AMPL model

var x1;
var x2;

minimize obj: (x1^2 - x2^2)^2 - x2^3;

subject to c1: (x1^2 - x2^2)^2 <= 0;
subject to c2: 1 - x1^2 - x2^2 <= 0;
