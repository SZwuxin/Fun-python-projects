class CaesarCipher():

    def cipher(self):
        inp = input('Do you want to (e)ncrypt or (d)ecrypt or (h)ack?')
        if inp != 'e' and inp != 'd' and inp != 'h':
            print('Invalid input, ending the cipher')
        elif inp == 'e':
            keyInput = input('Please enter the key (0 to 25) to use.')
            key = int(keyInput)
            messageInput = input('Enter the message to encrypt.')
            text = self.performEncrypt(messageInput, key)
            print(text)
        elif inp == 'd':
            keyInput = input('Please enter the key (0 to 25) to use.')
            key = int(keyInput)
            messageInput = input('Enter the message to decrypt.')
            text = self.performDecrypt(messageInput, key)
            print(text)
        else:
            keyInput = input('Enter the encrypted Caesar cipher message to hack.')
            self.performHack(keyInput)
    def performEncrypt(self, message, key):
        encText = []
        for i in message:
            newOrd = ord(i) + key
            char = chr(newOrd)
            encText.append(char)
        return ''.join(encText)


    def performDecrypt(self, message, key):
        decText = []
        for i in message:
            newOrd = ord(i) - key
            char = chr(newOrd)
            decText.append(char)
        return ''.join(decText)

    def performHack(self, message):
        for i in range(26):
            hackMessage = []
            for j in message:
                newOrd = ord(j) + i
                char = chr(newOrd)
                hackMessage.append(char)
            print('Key #' + str(i), ''.join(hackMessage))

CaesarCipher().cipher()
