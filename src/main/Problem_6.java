package main;

public class Problem_6 extends ProblemGenerator {

	@Override
	public String toString() {
		return super.toString() + "6";
	}

	public static int solve(int n) {
		int sum_squares = 0;
		int square_of_sums = 0;

		for (int i = 1; i <= n; i++)
				sum_squares += (int)Math.pow(i, 2);

		for (int j = 1; j <= n; j++)
			square_of_sums += j;
		square_of_sums *= square_of_sums;

		return square_of_sums - sum_squares;
	}

	@Override
	public void compute() {
		int n = 100;

		System.out.println(solve(n));
	}
}
