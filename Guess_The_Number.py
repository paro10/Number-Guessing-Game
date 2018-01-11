from random import randint
import pandas
import sys
import math

def isPrimeUnder1000(m):
    """
    Function to check if m is less than 1000 and also if it is prime.
    If m is equal to 1, then we set the message that m is not prime. If m =2, then prime. Checking with 2 is done since it
    is the smallest prime number. For the rest of the numbers from 2 to m-1, the mod is taken, such that, if there is no remainder, then
    flag is set to False (i.e. number divisible and not prime). Else, the number is considered prime.
    """

    flag=False
    if m>1000 or m<=0: #first condition
        flag=False #condition not satisfied
        print("Divisor(m) cannot be greater than 1000 or less than/equal to 0")
    else:
        if m==1:
            flag=False
            print("1 is not prime")
        elif m==2:
            flag=True
        else:
            for x in range(2,int(m)):
                if(m%x)==0: #no remainder, implies number is not prime
                    flag=False
                    print(m,"is not prime. Please enter a prime number")
                    break
                else: #remainder implies number is prime
                    flag=True
    return(flag)


def is_k_in_range(k,m):
    """
    This function checks if k is in the range of 0<=k<m, i.e. k is greater than/equal to 0 and less than m. If the
    conditions are satisfied, a flag is set to true. Else false.
    """

    flag=0
    if k>=0: #checking if k greater than/equal to 0
        if k<m: #checking if k less than m
            flag=1
        else:
            flag=0
    else:flag=0
    if flag==0: #condition not satisfied
        return(False)
    else:
        return(True) #all conditions satisfied


def run_Guess_My_Number(n,count,var):
    """
    Top-level wrapper to guess the number.
    It takes in var, which is the user's input to the original question (Ask/Guess/Quit)
    If var is equal to Ask, then it calls function compute_Ask to determine if all conditions for asking a question are
    satisfied.
    If all conditions for asking a question are satisfied, then the function is_n_minus_k_divisible_by_m() is called to
    check if the condition entered by the user is true or false.

    If var is equal to guess, the user is prompted to enter their guess. The number entered by the user is then checked with
    n(number generated) to see if there's a match. If there is a match, a flag is set to True to indicate the game is over. Also,
    the score of the user is calculated as ceiling(n/count) where n is the secret number, and count is the number of turns
    taken by the user to determine the number, including the correct "guess".
    Else the user is notified that the guess is wrong.
    """
    flag=False
    if var.lower()=='ask':
        var2=input("Please ask your question:")
        #print("You entered: " + str(var2))
        s=var2.replace('?', '')
        l=[] #list to store k and m values
        for t in s.split(): #splitting the string to extract the numbers
            try:
                l.append(float(t))
            except ValueError:
                pass
        k=l[0]
        m=l[1]
        correct_input=compute_Ask(k,n,m)
        if correct_input==False:
            print("Incorrect Input. Please enter again")
        else:
            print(is_n_minus_k_divisible_by_m(n,k,m))

    elif var.lower()=='guess':
        g=input("Please enter your guess:")
        if int(g)==n:
            print("Correct Guess. The number is",n,"Your score is: ",math.ceil(n/count)) #ceiling(n/count) where n is the secret number, and count is the number of turns taken by the user to determine the number, including the correct "guess".
            flag=True
        else:print("Wrong guess")
        count=count+1
    return(flag,count)



def compute_Ask(k,n,m):
    """
    Function to compute the answer to the "Ask" option. It returns True or False if the conditions are satisfied or not.
    The first is the call to function is_k_in_range() which checks if k is within the range 0 to m.
    The second is the call to isPrimeUnder1000() which checks whether m is a prime number less than 1000.
    """
    ans=is_k_in_range(k,m)
    is_prime=isPrimeUnder1000(m)
    if ans==False:
        print(k,"is not in range. Please enter a value of k (number to be subtracted) greater than/equal to 0 and less than",m)
        return(False)
    elif is_prime==False:
        print("Please enter a proper divisor(m) value")
        return(False)
    else:
        return(True)


def is_n_minus_k_divisible_by_m(n,k,m):
    """
    Function that checks if the condition entered by the user is True or False
    If a user asks the following question:
    "If we subtract k from n, is the result divisible by m?", then the function computes it and returns True/False
    The rules here are that n is the secret number, k is in the range 0 to m, and m is a prime number less than 1000.
    """
    output=(n-k)%m
    if output== 0:return(True)
    else:return(False)


def main():
    """
    Main method. The following are the initial variables:
    score: random value assigned
    n: Secret number generated by system, which the user has to guess
    A user is given the option to enter any one of the available options:
    Input to Program needs to be (case insensitive): Ask OR Guess OR Quit

    Function run_Guess_My_Number is called which takes as input the number generated, the initial number of times
    the program is run and the input entered by user (Ask/Guess/Quit)

    If the value entered by the user is quit, then the game exits and the user's score is set to 0.
    """
    score=10000000
    n=randint(0,1000)
    print("Original Number:",n) #The original number is printed so that it becomes easier to test the code and verify if number guessed = number generated
    count=1

    while True:
        #var!= 'Quit':
        var=input("Please enter one of the following: 1.Ask 2.Guess 3.Quit") # only enter Ask, Guess or Quit without the numbers
        print("You entered "+str(var))
        if var.lower()=='quit':
            print("Your score is: ",0)
            break
        else:
            f,count=run_Guess_My_Number(n,count,var)
        if f==True:break




if __name__ == '__main__':
    main()