sumlist(Ns, Sum) :- sumlist(Ns, 0, Sum).
sumlist([N|Ns], Temp, Sum) :- Temp1 is Temp + N, sumlist(Ns, Temp1, Sum).
sumlist([], Sum, Sum).
