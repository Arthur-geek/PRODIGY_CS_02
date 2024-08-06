from PIL import Image

def encrypt_image(input_path, output_path, key=None):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            encrypted_pixel = (b, g, r)
            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key=None):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            decrypted_pixel = (b, g, r)
            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

def main():
    print("Welcome to the Image Encryption Tool")

    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt an image? (E/D): ").lower()

        if choice in ['e', 'd']:
            input_path = input("Enter the path of the input image: ")
            output_path = input("Enter the path to save the output image: ")

            if choice == 'e':
                encrypt_image(input_path, output_path)
            else:
                decrypt_image(input_path, output_path)

        another = input("Do you want to process another image? (yes/no): ").lower()
        if another != 'yes':
            break

    print("Thank you for using the Image Encryption Tool. Goodbye!")

if __name__ == "__main__":
    main()
