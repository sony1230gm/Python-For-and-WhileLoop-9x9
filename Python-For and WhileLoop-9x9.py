#for loop
for i in range(1,10):
    for j in range(1,10):
        s=  i*j
        print ('%d * %d = %d   ' %(i, j , s), end="")

    print('\n')


# while loop
i=1;
while i < 10:
    j=1
    while j < 10:
        s=  i*j
        print ('%d * %d = %d ' %(i, j , s))
        j += 1

    i += 1
    print('\n')