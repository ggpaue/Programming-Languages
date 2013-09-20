fun doitHelper(n, sum) = if n = 0 then sum
	else doitHelper(n-1, n + sum);
