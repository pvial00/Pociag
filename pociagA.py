from Crypto.Util import number

def genBase(size):
    A = number.getPrime(size)
    B = number.getPrime(size)
    while B == A:
        B = number.getPrime(size)
    return A, B

def keygen(size):
    N, M = genBase(size)
    sk = number.getRandomRange(1, (N - 1))
    return sk, N, M

def pociag_demo(size):
    print "Generating Alice and Bob's keys"
    skA, nA, MA = keygen(size)
    skB, nB, MB = keygen(size)
    print skA, nA, MA
    print skB, nB, MB
    print "Exchanging the umbrella and generating secret umbrellas"
    U = nA * nB
    S = MA * U
    SB = MB * U
    print U
    print S, SB
    print "Each choose a number in secret umbrellas"
    y = number.getRandomRange(1, (S - 1))
    yB = number.getRandomRange(1, (SB - 1))
    print y, yB
    print "Each choose a temporary key in the umbrella"
    TkA = number.getRandomRange(1, (U - 1))
    TkB = number.getRandomRange(1, (U - 1))
    print TkA, TkB
    print "Exchange phase1"
    p1 = pow(y, TkA, U)
    p1B = pow(y, TkB, U)
    print p1, p1B
    print "Exchange phase2"
    p2 = pow(p1B, TkA, S)
    p2B = pow(p1, TkB, SB)
    print p2, p2B
    print "Exchange phase3"
    p3 = pow(p2B, skA, S)
    p3B = pow(p2, skB, SB)
    print p3, p3B
    print "Exchange phase 4"
    p4 = pow(p3B, TkA, U)
    p4B = pow(p3, TkB, U)
    print p4, p4B
    print "Exchange phase 5"
    p5 = pow(p4B, TkA, U)
    p5B = pow(p4, TkB, U)
    print p5, p5B
    print "Arrive at the shared modulus"
    p6 = pow(p5B, skA, U)
    p6B = pow(p5, skB, U)
    print p6, p6B
    print "Exchange phase 7"
    p7 = pow(yB, skA, p6)
    p7B = pow(yB, skB, p6B)
    print p7, p7B
    print "Arrive at the shared key phase8"
    p8 = pow(p7B, skA, p6)
    p8B = pow(p7, skB, p6B)
    print p8, p8B

pociag_demo(16)
