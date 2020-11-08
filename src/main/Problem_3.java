package main;

import java.util.ArrayList;

public class Problem_3 extends ProblemGenerator {

	@Override
	public String toString() {
		return super.toString() + "3";
	}
	
	
	public static ArrayList<Integer> getPrimeFactors(int n) {
		/* ArrayList primeFactors
		 * 
		 * for i <- 2 to n-1 do
		 * 		if n % i == 0 
		 * 			if i > 2 and i % 2 == 0
		 * 				pass
		 * 			if i > 3 and i % 3 == 0
		 * 				pass
		 * 			if i > 5 and i % 5 == 0
		 * 				pass
		 * 			if i > 7 and i % 7 == 0
		 * 				pass
		 * 			primeFactors <- i
		 * 
		 */
		
		ArrayList<Integer> primeFactors = new ArrayList<Integer>();
		for (int i = 2; i < n; i++) {
			if (n % i == 0) {
				if (i > 2 && i % 2 == 0)
					continue;
				if (i > 3 && i % 3 == 0)
					continue;
				if (i > 5 && i % 5 == 0)
					continue;
				if (i > 7 && i % 7 == 0)
					continue;
				primeFactors.add(i);
			}
		}
		
		return primeFactors;
	}
	
	@Override
	public void compute() {
		int n = 10; //Prime factors = 2, 3
		
		System.out.println(getPrimeFactors(n));
	}
}
