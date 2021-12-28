package main;

import java.math.BigInteger;
import java.util.Scanner;

public class Problem_13 extends ProblemGenerator {

	@Override
	public String toString() {
		return super.toString() + "13";
	}

	public static Long largeSum(int n) {
		Scanner scan = new Scanner(System.in);
		BigInteger sum = BigInteger.valueOf(0);
		String output = "";

		for (int i = 0; i < n; i++) {
			sum = sum.add(scan.nextBigInteger());
		}

		//Get first 10 digits (from left to right)
		char[] sumCharArr = sum.toString().toCharArray();
		for(int i = 0; i < 10; i++)
			output += sumCharArr[i];

		scan.close();

		//integer isn't sufficient to store 10 digits number
		return Long.parseLong(output);
	}

	@Override
	public void compute() {
		int n = 100; //number of lines
		System.out.println("Input:");
		System.out.println(largeSum(n));
	}
}
