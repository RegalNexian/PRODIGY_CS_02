from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key, output_path):
    try:
        image = Image.open(image_path)
    except IOError:
        print(f"Error: Cannot open image file {image_path}")
        return
    
    pixels = np.array(image)
    
    # Encrypt by adding key to each pixel value
    encrypted_pixels = (pixels + key) % 256
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    
    if not os.path.splitext(output_path)[1]:
        output_path += ".png"  # Default to PNG if no extension provided
    
    try:
        encrypted_image.save(output_path)
        print(f"Image encrypted and saved to {output_path}.")
    except IOError:
        print(f"Error: Cannot save encrypted image to {output_path}")

def decrypt_image(image_path, key, output_path):
    try:
        image = Image.open(image_path)
    except IOError:
        print(f"Error: Cannot open image file {image_path}")
        return
    
    pixels = np.array(image)
    
    # Decrypt by subtracting key from each pixel value
    decrypted_pixels = (pixels - key) % 256
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    
    if not os.path.splitext(output_path)[1]:
        output_path += ".png"  # Default to PNG if no extension provided
    
    try:
        decrypted_image.save(output_path)
        print(f"Image decrypted and saved to {output_path}.")
    except IOError:
        print(f"Error: Cannot save decrypted image to {output_path}")

def main():
    choice = input("Do you want to encrypt or decrypt an image? (e/d): ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice! Please enter 'e' for encryption or 'd' for decryption.")
        return

    image_path = input("Enter the path to the image (e.g., C:\\Users\\psoum\\Desktop\\image.jpg): ").strip()
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
        return
    
    try:
        key = int(input("Enter the encryption/decryption key (an integer): "))
    except ValueError:
        print("Error: The key must be an integer.")
        return
    
    output_path = input("Enter the output path for the processed image (e.g., C:\\Users\\psoum\\Desktop\\output.jpg): ").strip()

    if choice == 'e':
        encrypt_image(image_path, key, output_path)
    elif choice == 'd':
        decrypt_image(image_path, key, output_path)

if __name__ == "__main__":
    main()
