import sys


def encrypt(message, k):
    answer = ""

    # this traverses the message
    for c in range(len(message)):
        char = message[c]
        
        # adds the characters into the empty string variable after converting the characters from ASCII and adding the amount of them by k
        answer += chr((ord(char) + k - 97) % 26 + 97)

    return answer


def decrypt(message, k):
    answer = ""

    # this traverses the message
    for c in range(len(message)):
        char = message[c]
        
        # adds the characters into the empty string variable after converting the characters from ASCII and adding the negative amount of by k
        answer += chr((ord(char) -k - 97) % 26 + 97)
   
    return answer


if __name__ == "__main__":
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])

    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)