class HillCipher:
    def __init__(self, key):
        self.key = key

    @staticmethod
    def extended_euclid(a, mod):
        A1, A2, A3 = 1, 0, mod
        B1, B2, B3 = 0, 1, a

        while True:
            if B3 == 0:
                return 'no inverse'
            if B3 == 1:
                return (B2 + mod) % mod
            Q = A3 // B3
            T1, T2, T3 = A1 - Q * B1, A2 - Q * B2, A3 - Q * B3
            A1, A2, A3 = B1, B2, B3
            B1, B2, B3 = T1, T2, T3

    def invert_matrix(self):
        key = self.key
        det = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % 26
        if det == 0 or self.extended_euclid(det, 26) == 'no inverse':
            return 'the matrix key is not invertible'
        inv = self.extended_euclid(det, 26)
        return [
            [(inv * key[1][1]) % 26, (-1 * inv * key[0][1]) % 26],
            [(-1 * inv * key[1][0]) % 26, (inv * key[0][0]) % 26]
        ]

    def hill_cipher_2_enc(self, text):
        key = self.key
        matkey = self.matrix(key)

        if type(matkey) == str:
            return matkey

        text = text.lower()
        extras = []
        i = 0
        while i < len(text):
            if ord(text[i]) < 97 or ord(text[i]) > 122:
                extras.append([i, text[i]])
            i += 1
        for i in extras:
            text = text.replace(i[1], '')

        if len(text) % 2 == 1:
            text += 'x'
        C = []
        i = 0
        while i < len(text):
            C.append(chr((matkey[0][0] * (ord(text[i]) - 97) + matkey[0][1] * (ord(text[i + 1]) - 97)) % 26 + 97))
            C.append(chr((matkey[1][0] * (ord(text[i]) - 97) + matkey[1][1] * (ord(text[i + 1]) - 97)) % 26 + 97))
            i += 2

        for i in extras:
            C.insert(i[0], i[1])

        return ''.join(C)

    def hill_cipher_2_dec(self, text):
        key = self.key
        matkey = self.invert_matrix()

        if type(matkey) == str:  # if matrix is not invertible, return error message
            return matkey

        text = text.lower()
        extras = []
        i = 0
        while i < len(text):
            if not text[i].isalpha():
                extras.append([i, text[i]])
            i += 1
        text = ''.join(ch for ch in text if ch.isalpha())

        # Ensure text length is even for correct decoding
        if len(text) % 2 != 0:
            text += 'x'  # Padding if necessary, might choose a better method depending on context

        P = []
        i = 0
        while i < len(text) - 1:  # Ensure we don't go out of range
            # Calculate the decoded characters using the matrix
            decoded_first = (matkey[0][0] * (ord(text[i]) - 97) + matkey[0][1] * (ord(text[i + 1]) - 97)) % 26 + 97
            decoded_second = (matkey[1][0] * (ord(text[i]) - 97) + matkey[1][1] * (ord(text[i + 1]) - 97)) % 26 + 97
            P.append(chr(decoded_first))
            P.append(chr(decoded_second))
            i += 2

        for index, char in extras:
            P.insert(index, char)

        return ''.join(P)


    def matrix(self, key):
        det = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % 26
        if det == 0 or self.extended_euclid(det, 26) == 'no inverse':
            return 'the matrix key is not invertible'
        return key


