# PRIME NUMBER FACTORIZATION #

**1.Intention for this project**

This project is meant as an attempt to create an algorithm for prime number factorization that works in O(n²) timecomplexity. Due to my lack of experience calculating time complexities I am not aware wether or not I have actually managed this(see explanation of algorithm for further explanation). Although this might be one of the fastest way to theoretically perform prime number factorization, it is not viable due to the slow generation method of prime numbers. I'm still toying aroung with some ideas on how to make the generation of these faster, but as of right now this is the fastest algorythm i have found.

**2.Explanation of algorithm**

When a number is entered, the program first looks at how many of the prime factors are 2, 3, 5 and 7. These are the first 4 prime numbers and thus the most likely. Checking for these the same way we check for other factors is not very efficient, since each division by one of these factors does not even eliminate one digit for sure from the number we're trying to get the factors of.

Once we've eliminated all of the small factors, we now look at the last digit of the number. There's only a certain amount of numbers that multiplied with each other can give a number with that last digit. We now search through these in order to find the next factor.

To visualize this, lets take for example the number 129. This is not a one to one example since we will skip the first step of searching through one digit long prime numbers. Now, the last digit of this number is 9. The number nine can only be achieved through multiplication when multiplying either 3 * 3 or 1 * 9. We first try the option 3 * 3. Since both of these numbers only describe the last digits of the factors we create a formula to describe this:

### (10x + 3) * (10y + 3) = 129 ###

This formula basically means that a number with last digit 3 multiplied by a number with last digit 3 will result in 129. In order to solve this equation we reformulate it like this:

### 10y + 3 = 129 / (10x + 3) ###

10x + 3 is now bruteforced with all prime numbers with the last digit 1(which have been saved under src/primes/3.txt). This will result in us finding that the number 3 is the next prime factor. We now divide 129 by 3 and add 3 to our list of primes. The result of the division is 43. A quick run of the same algorythm will not find any result, telling us that 43 is also a prime number, which makes our prime factors 3 and 43.

Now this algorythm might be O(n²) for all I know because for each prime factor there is one nested loop, where we first loop through each possible multiplication method and for each multiplication method brute force the prime factor. Given n prime factors, where each has k multiplication methods and each multiplication method has g number of possible primes, I believe that the time complexity would theoretically be O(kn * gn) = O(kgn²) which would be reduced to O(n²).

**3.Possible ways of improvement**

Although I'm proud of my algorythm, there's definitely room for improvement, especially in the way to generate prime numbers. As of right now I have found no way to generate prime numbers in a way with time complexity lower than O(n²), which is detremental since in order to crack 128 bit keys reliably we would need prime numbers up to 33 digits long. I have found one theoretical way to make this algorythm O(n) but I doubt it would make it any quicker, since the factor of the n would also be 33 digits long.

Another problem arises with the unexactness of computers, which for example causes 2+1 to result in 3.000000000000004. The issue hereby lies in the fact that a number that is technically a float might be seen as a full number when the digits behind the coma approach 1. If the resulting number of one of the divisions in the algorythm is, for example, 3.99998 it might simply be interpreted as 4, which would make it, in the eyes of the algorythm, a valid prime factor.

Lastly, if there was a way to solve the aformentioned formula without brute force this would result in an algorythm with time complexity O(n), which would obviously be much better. However, I don't think there's a mathematical way to solve a formula with two coordinates.

If there's any ideas on how to fix any of these issues, I would love to hear them!
