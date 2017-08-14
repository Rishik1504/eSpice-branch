'''BrainfuckCompiler'''
A = open('filedata.txt','r')
B = open('OPFile.txt','w')
C = B.read()
D = 0
E = 0
F = [0]
while D < len(C):
    if C[D] == '+':
        if F[E] == 255:
            print 'ERROR'
            break
        F[E] += 1
    elif C[D] == '-':
        if F[E] == 0:
            print 'ERROR'
            break
        F[E] -= 1
    elif C[D] == '>':
        E += 1
        if E == len(F):
            F.append(0)
    elif C[D] == '<':
        if E == 0:
            print 'ERROR'
            break
        E -= 1
    elif C[D] == ',':
        I = raw_input("INPUT:\t")
        F[E] = ord(I[0])
    elif C[D] == '.':
        C.write(chr(F[E]))
    elif C[D] == '[':
        if F[E] == 0:
            G = 0
            D += 1
            while D < len(C):
                if C[D] == "]" and G == 0:
                    break
                elif C[D] == "[":
                    G += 1
                elif C[D] == "]":
                    G -= 1
                D += 1
    elif C[D] == ']':
        if F[E] != 0:
            H = 0
            D -= 1
            while D >= 0:
                if C[D] == "[" and H == 0:
                    break
                elif C[D] == "[":
                    H -= 1
                elif C[D] == "]":
                    H += 1
                D -= 1
    D += 1
A.close()
B.close()
