package main;

public class Problem_2 extends ProblemGenerator{
	//Ans:4613732
	@Override
	public String toString() {
		return super.toString() + "2";
	}

	public static long fib(int n) {
		//Fibonacci general formula is based on fib(n-1) + fib(n-2) for nth term
		if (n <= 1)
			return 1;
		else
			return fib(n-1) + fib(n-2);
	}

	@Override
	public void compute() {
		/* do-while loop:
		 * 		n <- 1, sum <- 0
		 * 		obtain fibValue <- fib(n)
		 * 		n++
		 *
		 * 		while (fibValue < 4mil)
		 * 			if fibValue % 2 == 0
		 * 				sum += fibValue
		 *
		 */

		int limit = 4000000;
		int n = 1;
		long sum = 0;
		long fibValue;

		do {
			fibValue = fib(n);

			if (fibValue % 2 == 0)
				sum += fibValue;
			n++;

		} while (fibValue < limit);



		System.out.println(sum);
	}
}
