# Generated AMPL model

var x >= -1000 <= 1000;
var y >= -1000 <= 1000;

minimize obj: x^4 + y^4 + 2*x^2*y^2 - 3*x^3 + 4*x*y^2 - 6*y;
