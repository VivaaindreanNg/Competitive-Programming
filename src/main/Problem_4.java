package main;

public class Problem_4 extends ProblemGenerator {

	@Override
	public String toString() {
		return super.toString() + "4";
	}

	public static int palin(int n) {
		return 100;
	}

	@Override
	public void compute() {
		int n = 10; //Prime factors = 2, 3

		System.out.println(palin(n));
	}
}
