(define(doithelper n rest)
( if(= n 0)
rest
(doithelper (- n 1)(+ n rest))
))
(
define(doit n)
(doithelper n 0)
)
