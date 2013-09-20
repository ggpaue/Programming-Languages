(define (sum lis)
	(cond
		((NULL? lis) 0)
		((not (number? (car lis))) '())
		(else (+ (car lis) (sum (cdr lis))))
))

(define (sumsub sublis)
	(cond
		((NULL? sublis) 0)
		(else (+ (sum (car sublis)) (sumsub (cdr sublis))))
))
