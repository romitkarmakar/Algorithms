# Quin-Mccluskey Algorithm

The Quine–McCluskey algorithm or the method of prime implicants is a method used for minimization of boolean functions.
It is functionally identical to Karnaugh mapping, but the tabular form makes it more efficient for use in computer 
algorithms, and it also gives a deterministic way to check that the minimal form of a Boolean function has been
reached. It is sometimes referred to as the tabulation method.  

It is implemented using python  version 3.

## Methods

- Finding all prime implicants of the function.
- Use those prime implicants in a prime implicant chart to find the essential prime
implicants of the function, as well as other prime implicants that are necessary to cover
the function.

## Installation

- Clone the repos
- Open the folder in your terminal
- Run the code using this command
<pre>$ python qm.py</pre>

## Working

- Enter the number of variables (must be between 1 and 11)
- It will take random number of min terms between 1 and 2^(number of variables)
- The minterms will also be generated randomly
- Then using the quin-mccluskey reducing algorithm it will solve the expression and print it in SOP form.
- Press 1 to run another expression.
- Any other number to exit the programm.

## Documentation

- getVars() - function to get the boolean term letters.
- decToBin() - convert decimal to binary
- pad() - function to pad zeros to the binary equivalent of digits. Eg: If there are 4 variables, 2, that is 10 in binary is represented as 0010
- isGrayCode() - function to check if two terms differ by just one bit
- replace_compliments() - function to replace complement terms with don't cares Eg: 0110 and 0111 becomes 011-
- reduce() - function to reduce minterms(first a loop runs which checks every single minterms with another minterm, if a graycode is found then it groups the minterms into a new minterm vector and then returns it.)
- getValue() - Convert the boolean minterm into the variables for output to the user.