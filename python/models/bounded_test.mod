# Generated AMPL model

var x >= -100 <= 100;
var y >= -100 <= 100;

minimize obj: x^4 + y^4 + x^2*y + 3*x;
