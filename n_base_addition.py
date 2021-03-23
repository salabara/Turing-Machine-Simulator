# This file is a collection of methods for
# generating the TM code for addition in base n

# generate rules start with s0 and S+
def rule_generator_1(n):
    print("s0,ff")
    print("s0,B,s0,B,R")
    print("s0,+,s1,+,L")
    for dig in range(n):
        dig = str(dig)
        print("s0," + dig + ",s1," + dig + ",L")

    print("s1,B,S+,B,R")
    print("S+,+,M1,+,L")
    for dig in range(n):
        dig = str(dig)
        print("S+," + dig + ",S+," + dig + ",R")


# generate rules start with M1, and S0 to S9
def rule_generator_2(n):
    print("M1,B,Cl,B,R");
    for dig in range(n):
        print("M1," + str(dig) + ",S" + str(dig) + ",X,R")
    for dig in range(n):
        s = "S" + str(dig)
        a = "A" + str(dig)
        print(s + ",B," + a + ",B,L")
        print(s + ",+," + s + ",+,R")
        for d in range(n):
            print(s + "," + str(d) + "," + s + "," + str(d) + ",R")
        for d in range(n):
            c = chr(d+97)
            print(s + "," + c + "," + a + "," + c + ",L")


# generate rules start with A0 to A9
def rule_generator_3(n):
    for dig in range(n):
        A = "A" + str(dig)
        print(A + ",+,Re," + chr(dig+97) + ",L")
        for c in range(n):
            if (dig+c) < n:
                print(A + "," + str(c) + ",Re," + chr(dig + c + 97) + ",L")
            else:
                print(A + "," + str(c) + ",Of," + chr(dig + c - n + 97) + ",L")


# generate rules start with Re, Of, Cl and M2
def rule_generator_4(n):
    print("Re,+,Re,+,L")
    for dig in range(n):
        c = str(dig)
        print("Re," + c + ",Re," + c + ",L")
    print("Re,X,M1,0,L")

    print("Of,+,Re,1,L")
    for dig in range(n-1):
        c1 = str(dig)
        c2 = str(dig+1)
        print("Of," + c1 + ",Re," + c2 + ",L")
    print("Of," + str(n-1) + ",Of,0,L")

    print("Cl,+,Cl,B,R")
    print("Cl,0,Cl,B,R")
    for dig in range(1, n):
        c = str(dig)
        print("Cl," + c + ",M2," + c + ",R")
    print("Cl,a,Cl,B,R")
    for dig in range(1, n):
        c1 = chr(dig + 97)
        c2 = str(dig)
        print("Cl," + c1 + ",M2," + c2 + ",R")

    print("M2,B,ff,B,L")
    for dig in range(n):
        c = str(dig)
        print("M2," + c + ",M2," + c + ",R")
    for dig in range(n):
        c = str(dig)
        print("M2," + chr(dig+97) + ",M2," + c + ",R")


# generate the TM code for addition in base n
def generate_n_base_addition(n):
    rule_generator_1(n)
    rule_generator_2(n)
    rule_generator_3(n)
    rule_generator_4(n)