# Polynomial

## Aim

The aim of this checkpoint to write a Python class to represent a polynomial and to use this class to perform simple mathematical operations on polynomials.

## Task

Write a Python class to represent a polynomial of the form:

$P(x)=∑_{i=0}^n a_ix^i=a_0+a_1x+a_2x^2+⋯+a_nx^n$

where the coefficients ai are real numbers.

In the task description below we have assumed that the class name is Polynomial.

Your class should include:

- A list instance variable to hold the coefficients of $P(x)$.
- An __init__() method to set the values of the coefficients ai, which should be supplied as a list.
- Methods to:
  - Calculate and return the order of $P(x)$.
  - Add another Polynomial object to $P(x)$ and return the result as a new Polynomial object (it is not sufficient to return the result as a list of coefficients). Your code should include the case where the polynomials being added are of different order.
    #### Adding polynomials
    For example:
    
    $(a_0+a_1x+a_3x^3)+(b_0+b_2x^2+b_3x^3+b_4x^4)=(a_0+b_0)+a_1x+b_2x^2+(a_3+b_3)x^3+b_4x^4$

  - Calculate the derivative of $P(x)$ and return the result as a new Polynomial object.
    #### Differentiating polynomials
    The derivative of a polynomial $P(x)$ is:
    
    $dP(x)/dx=∑_{i=1}^nia_ix^{i−1}=a_1+2a_2x+3a_3x^2+⋯+na_nx^{n−1}$
  - Calculate the antiderivative (indefinite integral) of $P(x)$ and return the result as a new Polynomial object. A numerical value for the constant of integration should be supplied to the method.
    #### Integrating polynomials
    The indefinite integral of a polynomial $P(x)$ is:
    
    $∫P(x)dx=c+∑_{i=0}^n\frac{a_i}{i+1}x^{i+1}=c+a_0x+\frac{a_1}{2}x^2+\frac{a_2}{3}x^3+⋯+\frac{a_n}{n+1}x^{n+1}$
    where c is a constant, called the constant of integration.
  - Print a sensible String representation of $P(x)$, for example in the form:
  
    $P(x) = a_0x^0 + a_1x^1 + a_2x^2 + .... + a_nx^n$

You should also write a test code to check that your class works. This should have a main() method that creates Polynomial objects to represent the following polynomials:

- $P_a(x)=2+4x^2−x^3+6x^5$
- $P_b(x)=−1−3x+4.5x^3$

and then:

- Calculates the order of Pa(x)
- Adds $P_b(x)$ to $P_a(x)$
- Calculates the first derivative of Pa(x)
- Calculates the antiderivative of this result, i.e. the antiderivative of $dP_a(x)/dx$. The constant of integration c should be set to c=2.

### Check your result!
The coefficients of this antiderivative should be the same as those of $P_a(x)$, as you have differentiated $P_a(x)$ then taken the antiderivative of the result (and set the constant of integration equal to the value of $a_0$ for $P_a(x)$). Although you may find that the coefficients are floating point numbers rather than integers.

In each case your code should print the results to the screen, using your String representation of a Polynomial object where appropriate.