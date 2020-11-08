package main;

public class Problem_1 extends ProblemGenerator {
	//Ans: 233168
	@Override
	public String toString() {
		return super.toString() + "1";
	}

	@Override
	public void compute() {
		int n = 1000;
		int sum = 0;
		
		for (int i = 0; i < n; i++) {
			if (i % 3 == 0 || i % 5 == 0)
				sum+=i;
		}
		
		System.out.println(sum);
	}
	

}
