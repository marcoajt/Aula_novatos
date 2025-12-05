from random import choice


class Cipher:
    def __init__(self, key=None):
        self.letters = "abcdefghijklmnopqrstuvwxyz"

        if key is None:
            # gera uma chave aleatória de 100 letras minúsculas
            self.key = "".join(choice(self.letters) for _ in range(100))
        else:
            self.key = key

    def encode(self, text: str) -> str:
        """Encryption

        Args:
            text: word

        Returns:
            str: word encryption
        """
        resultado = ""

        for i in range(len(text)):
            letra_texto = text[i]
            letra_chave = self.key[i % len(self.key)]
            indice_texto = self.letters.index(letra_texto)
            indice_chave = self.letters.index(letra_chave)
            novo_indice = (indice_texto + indice_chave) % 26
            resultado += self.letters[novo_indice]

        return resultado

    def decode(self, text):
        """Reverse encryption

        Args:
            text: word encryption

        Returns:
            str: word
        """
        resultado = ""

        for i in range(len(text)):
            letra_texto = text[i]
            letra_chave = self.key[i % len(self.key)]
            indice_texto = self.letters.index(letra_texto)
            indice_chave = self.letters.index(letra_chave)
            novo_indice = (indice_texto - indice_chave) % 26
            resultado += self.letters[novo_indice]

        return resultado
