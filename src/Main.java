import java.util.ArrayList;
import java.util.HashMap;
import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.math.BigInteger;

public class Main {
	static String path = "/home/sat/eclipse-workspace/B0red/PrimeNumberFactorization/src/";
	static String[][] MultTbl = ExtractMultiplicationTable();
	static HashMap <Integer, Integer> Indices = new HashMap<Integer, Integer>();
	
	static BigInteger [][] primes = ExtractPrimes();
	public static void main(String[] args) {
		Indices.put(3, 0);
		Indices.put(7, 1);
		Indices.put(1, 2);
		Indices.put(9, 3);
		ArrayList <BigInteger> PrimeFactors = Factorization(convertToBig("26"));
		for(int i = 0; i<PrimeFactors.size()-1; i++) {
			System.out.println(PrimeFactors.get(i).toString());
		}
	}

	public static BigInteger convertToBig(String num) {
		return new BigInteger(num);
	}
	
	public static ArrayList<BigInteger> Factorization(BigInteger num) {
		ArrayList<BigInteger> PrimeFactors = new ArrayList<BigInteger>();
		String AnalizeNum = num.toString();
		char LastCharacter = AnalizeNum.charAt(AnalizeNum.length()-1);
		
		while(num.mod(convertToBig("2")).equals(BigInteger.ZERO)) {
			System.out.println("2");
			num = num.divide(convertToBig("2"));
		}
		while(num.mod(convertToBig("3")).equals(BigInteger.ZERO)) {
			System.out.println("3");
			num = num.divide(convertToBig("3"));
		}
		while(num.mod(convertToBig("5")).equals(BigInteger.ZERO)) {
			System.out.println("5");
			num = num.divide(convertToBig("5"));
		}
		while(num.mod(convertToBig("7")).equals(BigInteger.ZERO)) {
			System.out.println("7");;
			num = num.divide(convertToBig("7"));
		}
		
		while(num.intValue() != 1) {
			String Snum = String.valueOf(num);
			BigInteger [] results = FindSingleFactors(Snum);
			BigInteger prevnum = num;
			PrimeFactors.add(results[0]);
			num = results[1];
			if(num == null) {
				System.out.println(prevnum);
				break;
			}
		}
		
		return PrimeFactors;
	}
	
	public static String[][] FindMultiples(char num) {
		String[][] Multiples = new String[5][2];
		
		int count = 0;
		
		for(int i = 0; i<MultTbl.length; i++) {
			char lastDigit = MultTbl[i][2].charAt(MultTbl[i][2].length()-1);
			if(lastDigit == num) {
				Multiples[count][0] = MultTbl[i][0];
				Multiples[count][1] = MultTbl[i][1];
				count += 1;
			}
		}
		
		return Multiples;
	}
	
	public static String[][] ExtractMultiplicationTable() {
		String[][] MultTable = new String[15][3];
		
		try {
		      File myObj = new File(path + "calc_nums.txt");
		      Scanner myReader = new Scanner(myObj);
		      int count = 0;
		      while (myReader.hasNextLine()) {
		        String[] data = myReader.nextLine().split(" ");
		        for(int i = 0; i<MultTable[count].length; i++) {
		        	MultTable[count][i] = data[i];
		        }
		        count += 1;
		      }
		      myReader.close();
		    } catch (FileNotFoundException e) {
		      System.out.println("An error occurred.");
		      e.printStackTrace();
		    }
		
		return MultTable;
	}
	
	public static BigInteger[][] ExtractPrimes() {
		String spec_path = "primes/";
		File fFolder = new File(path + spec_path);
		BigInteger[][] primes = new BigInteger[6][19665];
		String[] SFileNames = fFolder.list();
		
		for(int i = 0; i<SFileNames.length; i++) {
			try {
			      File myObj = new File(path + spec_path + SFileNames[i]);
			      Scanner myReader = new Scanner(myObj);
			      int count = 0;
			      while (myReader.hasNextLine()) {
			        primes[i][count] = new BigInteger(String.valueOf(Integer.parseInt(myReader.nextLine())));
			        count += 1;
			      }
			      myReader.close();
			    } catch (FileNotFoundException e) {
			      System.out.println("An error occurred.");
			      e.printStackTrace();
			    }
		}
		
		return primes;
	}
	
	public static BigInteger[] FindSingleFactors(String num) {
		BigInteger[] SingleFactors = new BigInteger[2];
		char LastDigit = num.charAt(num.length()-1);
		
		BigInteger Inum = new BigInteger(num);
		
		String [][] Mults = FindMultiples(LastDigit);
		
		for(int i = 0; i<Mults.length; i++) {
			if(Mults[i][0] != null) {
				int mult1 = Integer.valueOf(Integer.parseInt(Mults[i][0]));
				for(int j = 0; j<primes[Indices.get(mult1)].length-1; j++) {
					if(primes[Indices.get(mult1)][j] != BigInteger.valueOf(0) && primes[Indices.get(mult1)][j] != null) {
						float result = Inum.floatValue() / primes[Indices.get(mult1)][j].floatValue();
						if(result % 10 == Integer.parseInt(Mults[i][1])) {
							SingleFactors[0] = primes[Indices.get(mult1)][j];
							SingleFactors[1] = new BigInteger(String.valueOf((int)result));
							break;				
							}
					}
				}
			}
			if(SingleFactors[0] != null) {
				if(SingleFactors[0].intValue() != 0) {
					break;
				}
			}
		}
		
		return SingleFactors;
	}
}
