import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.png")

# Get the password for decryption
password = input("Enter passcode for Decryption: ")

# Original password used during encryption
original_password = input("Enter the original passcode used for encryption: ")

# Dictionary to map values to characters
c = {i: chr(i) for i in range(255)}

# Initialize pixel positions
n, m, z = 0, 0, 0

message = ""

# Decrypt the message if the password matches
if password == original_password:
    while True:
        try:
            char = c[img[n, m, z]]
            if char == "\0":  # Stop at null character (optional)
                break
            message += char
            n += 1
            m += 1
            z = (z + 1) % 3  # Cycle through RGB channels
        except KeyError:
            break  # Stop if we reach an invalid character
    print("Decryption successful! Message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
