package main;

import java.math.BigInteger;

public class Problem_16 extends ProblemGenerator {

	@Override
	public String toString() {
		return super.toString() + "16";
	}
	
	public static BigInteger powDigitSum(int exp) {
		BigInteger sum = BigInteger.valueOf(2).pow(exp);
		BigInteger result = BigInteger.valueOf(0);
		
		//while(sum != 0)
		while (sum.compareTo(BigInteger.valueOf(0)) != 0) {
			result = result.add(sum.mod(BigInteger.valueOf(10)));
			sum = sum.divide(BigInteger.valueOf(10));
		}
		
		return result;
	}
	
	@Override
	public void compute() {
		int ex = 1000; //exponent value
		
		System.out.println(powDigitSum(ex));
	}
}
