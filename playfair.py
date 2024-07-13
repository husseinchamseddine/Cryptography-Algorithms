class PlayfairCipher:
    def __init__(self):
        self.alphabet = "abcdefghiklmnopqrstuvwxyz"

    def create_matrix(self, key):
        matrix = [[0 for _ in range(5)] for _ in range(5)]
        filtered_key = []
        for char in key.lower().replace('j', 'i'):
            if char in self.alphabet and char not in filtered_key:
                filtered_key.append(char)
        key = filtered_key
        alphabet = [x for x in self.alphabet if x not in key]
        k, l, j = 0, 0, 0
        for i in range(5):
            while j < 5:
                if k < len(key):
                    if key[k] in alphabet or key[k] not in matrix[i]:
                        matrix[i][j] = key[k]
                        if key[k] in alphabet:
                            alphabet.remove(key[k])
                    else:
                        j -= 1
                    k += 1
                else:
                    matrix[i][j] = alphabet[l]
                    l += 1
                j += 1
            j = 0
        return matrix

    def encrypt(self, P, M1, M2):
        P = P.lower().replace(" ", "").replace("j", "i")
        P = [x for x in P]
        if len(P) % 2 != 0:
            P.append("x")
        n = len(P)
        C = [0 for x in range(n)]
        i = 0
        while i < n - 1:
            for j in range(5):
                for k in range(5):
                    if P[i] == M1[j][k]:
                        row1, col1 = j, k
                    if P[i+1] == M2[j][k]:
                        row2, col2 = j, k
            if col1 == col2:
                C[i] = P[i]
                C[i+1] = P[i+1]
            else:
                C[i] = M1[row1][col2]
                C[i+1] = M2[row2][col1]
            i += 2
        return "".join(str(x) for x in C)

    def decrypt(self, C, M1, M2):
        C = C.lower().replace(" ", "").replace("j", "i")
        C = [x for x in C]
        if len(C) % 2 != 0:
            C.append("x")
        n = len(C)
        P = [0 for x in range(n)]
        i = 0
        while i < n - 1:
            for j in range(5):
                for k in range(5):
                    if C[i] == M1[j][k]:
                        row1, col1 = j, k
                    if C[i+1] == M2[j][k]:
                        row2, col2 = j, k
            if col1 == col2:
                P[i] = C[i]
                P[i+1] = C[i+1]
            else:
                P[i] = M1[row1][col2]
                P[i+1] = M2[row2][col1]
            i += 2
        return "".join(str(x) for x in P)
