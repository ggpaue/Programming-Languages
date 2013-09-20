fun sumlist([]) = 0
|	sumlist(h :: t) = h + sumlist(t);
fun sumsub([]) = 0
|	sumsub(h :: t) = sumlist(h) + sumsub(t);
