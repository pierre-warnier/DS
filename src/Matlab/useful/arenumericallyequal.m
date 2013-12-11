function b = arenumericallyequal(A,B)
    b = sum(sum((abs(A - B) * 10 ^-9) / 10^-9)) == 0;
end