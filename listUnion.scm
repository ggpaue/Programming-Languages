(define (unionlists l1 l2)
	(cond
		((NULL? l1) l2)
		((member(CAR l1) l2)(unionlists (CDR l1) l2))
		(else (CONS (CAR l1)(unionlists(CDR l1) l2)))
))
