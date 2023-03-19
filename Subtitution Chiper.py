alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "fcpevqkzgmtrayonujdlwhbxsi"
text = "akim"

result = ""
for letter in text:
    if letter.lower() in alphabet:
        result += key[alphabet.find(letter.lower())]
    else:
        result += letter

print(result)