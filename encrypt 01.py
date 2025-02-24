import cv2
import os

# Load the image
img = cv2.imread("harsh.png")  # Replace with the correct image path

# Get user input
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Dictionary to map characters to values
d = {chr(i): i for i in range(255)}

# Initialize pixel positions
n, m, z = 0, 0, 0

# Encrypt the message into the image
for char in msg:
    img[n, m, z] = d[char]
    n += 1
    m += 1
    z = (z + 1) % 3  # Cycle through RGB channels

# Save the encrypted image
cv2.imwrite("encryptedImage.png", img)

# Open the image (Windows-specific, modify for other OS)
os.system("start encryptedImage.png")

print("Encryption successful! Encrypted image saved as 'encryptedImage.png'.")
