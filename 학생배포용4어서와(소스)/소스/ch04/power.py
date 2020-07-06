for a in range(1, 101, 1):
    for b in range(1, 101, 1):
        for c in range(1, 101, 1):
            if( (a*a+b*b)==c*c ):
                print(a, b, c)
