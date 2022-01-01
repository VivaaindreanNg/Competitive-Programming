package main;

import java.math.BigInteger;

public class Problem_48 extends ProblemGenerator{

	@Override
	public String toString() {
		return super.toString() + "48";
	}


	public static BigInteger selfPowers(int n, int digit) {
		BigInteger sum = BigInteger.valueOf(0);
		BigInteger result = BigInteger.valueOf(0);

		//find power i**i via loop
		for (int i = 1; i <= n; i++)
			sum = sum.add(BigInteger.valueOf(i).pow(i));


		System.out.println("Sum: " + sum);

		//find last x digits
		for (int j = 0; j < digit; j++) {
			//result += (sum % 10) * Math.pow(10, j);
			result = result.add(
					sum.mod(BigInteger.valueOf(10)).
					multiply(BigInteger.valueOf(10).
							pow(j)));

			sum = sum.divide(BigInteger.valueOf(10));
		}

		return result;
	}

	@Override
	public void compute() {
		int n = 1000;
		int last_digits = 10; //last x numbers of digits (from right to left)
		System.out.println(selfPowers(n, last_digits));
	}

}
