clc; clear all;
theta_star= 54.7356;

e=theta_star-180;
i=-60;

n1_1 = (-1/sqrt(3) * cos(e)) + (sqrt(2/3) * cos(i) * sin(e))
n2_1 = (-1/sqrt(3) * cos(e)) - (1/sqrt(6) * cos(i) * sin(e)) - (1/sqrt(2)* sin(i) *sin(e))
n3_1 = (-1/sqrt(3) * cos(e)) - (1/sqrt(6) * cos(i) * sin(e)) + (1/sqrt(2)* sin(i) *sin(e))


e_2=theta_star;
i_2=-60;
n1_2 = (-1/sqrt(3) * cos(e_2)) + (sqrt(2/3) * cos(i_2) * sin(e_2))
n2_2 = (-1/sqrt(3) * cos(e_2)) - (1/sqrt(6) * cos(i_2) * sin(e_2)) - (1/sqrt(2)* sin(i_2) *sin(e_2))
n3_2 = (-1/sqrt(3) * cos(e_2)) - (1/sqrt(6) * cos(i_2) * sin(e_2)) + (1/sqrt(2)* sin(i_2) *sin(e_2))

