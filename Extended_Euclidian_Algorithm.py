def extendedEuclid(a,mod):
    A1,A2,A3 = 1,0,mod
    B1,B2,B3 = 0,1,a

    while True:
        if B3 == 0:
            return 'no inverse'
        if B3 == 1:
            return (B2 + mod) % mod
        Q = A3 // B3
        T1,T2,T3 = A1 - Q*B1,A2 - Q*B2,A3 - Q*B3
        A1,A2,A3 = B1,B2,B3
        B1,B2,B3 = T1,T2,T3
