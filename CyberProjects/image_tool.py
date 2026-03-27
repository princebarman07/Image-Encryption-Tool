import os
from cryptography.fernet import Fernet

def initialize_security():
    """Ensures a master key exists for encryption/decryption."""
    if not os.path.exists("master.key"):
        key = Fernet.generate_key()
        with open("master.key", "wb") as key_file:
            key_file.write(key)
    
    with open("master.key", "rb") as key_file:
        return key_file.read()

def process_image(file_path, mode="encrypt"):
    """Handles both encryption and decryption of image files."""
    try:
        key = initialize_security()
        cipher = Fernet(key)

        # Read the source file
        with open(file_path, "rb") as file:
            data = file.read()

        if mode == "encrypt":
            # Protect data
            processed_data = cipher.encrypt(data)
            output_name = "protected_asset.enc"
            message = f"Done! Encrypted file saved as: {output_name}"
        else:
            # Restore data
            processed_data = cipher.decrypt(data)
            output_name = "restored_image.jpg"
            message = f"Done! Image restored as: {output_name}"

        # Save result
        with open(output_name, "wb") as output_file:
            output_file.write(processed_data)
        
        print(f"\n[+] {message}")

    except FileNotFoundError:
        print("\n[!] Error: The specified image file was not found.")
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("--- Pinnacle Labs Cybersecurity Tool ---")
    print("1. Encrypt Image (Lock)")
    print("2. Decrypt Image (Unlock)")
    
    user_choice = input("\nSelect an option (1/2): ")
    
    if user_choice == '1':
        target = input("Enter the full image name (e.g., panda.jpeg): ")
        process_image(target, mode="encrypt")
    elif user_choice == '2':
        process_image("protected_asset.enc", mode="decrypt")
    else:
        print("Invalid selection. Exiting.")
        
              