(define (sum lis)
	(cond
		((NULL? lis) 0)
		(else (+ (car lis)(sum (cdr lis))))
))
