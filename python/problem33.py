import time
from fractions import Fraction

start = time.time()

def find_denominator():
    product = 1
    #'for' loops to generate Numerator and Denominator
    for i in range(10,1000):
        for j in range(i+1,1000):
            #Intersection of Two sets(Common number between the two)
            common = list(set(str(i))&set(str(j)))
            #Check if the list is not empty
            if len(common) != 0:
                #Check if the common number is not 0
                if common[0] != '0':
                    num = list(str(i))
                    den = list(str(j))
                    #Remove the common element from numerator
                    num.remove(common[0])
                    #Remove the common element from Denominator
                    den.remove(common[0])
                    #Check if the value of num and den are not equal to 0
                    if num[0]!='0' and den[0]!='0':
                        #Check if they satisfy the question condition
                        if Fraction(int(num[0]),int(den[0])) == Fraction(i,j):
                            #multiply to the product
                            product *= Fraction(i,j)
                            print(Fraction(i,j))
                            print(i, j)
    
    print(product)

def main():
    find_denominator()
    pass

if __name__ == '__main__':
    main()

print("Time elapsed: {} seconds".format(time.time() - start))