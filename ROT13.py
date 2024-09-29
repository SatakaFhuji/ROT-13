import string
import getpass
import tkinter as tk
from tkinter import filedialog

def rot13(text):
    '''Encrypt text using the ROT13 method'''
    rot13_translation = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
        string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
    )
    return text.translate(rot13_translation)

def choose_file():
    '''memilih file yang akan di decript'''
    # membuat root window untuk dialog file (tanpa menampilkannya)
    root = tk.Tk()
    root.withdraw() # menyembunyikan jendela Tkinter utama

    # membuka dialog pemilihan file
    file_path = filedialog.askopenfilename(
        title="pilih File",
        filetypes=[("Text file", "*.txt"), ("All file", "*.*")]
    )

    # menampilkan path dari file yang dipilih
    if file_path:
        print(f"File yang dipilih: {file_path}")
    else:
        print("Tidak ada file yang dipilih")

def main():
    print('WELCOME TO PASSWORD GENERE USING ROT13 METHOD')

    # menanyakan user, encrypt to decrypt atau decrypt to encrypt
    print("what you want, encrypt to decrypt or decrypt to encrypt\n1.encrypt to decrypt\n2.decrypt to encrypt")
    ask_method = input("1 or 2\n")

    # mengambil input dari user
    original_text = getpass.getpass('masukkan password: ')

    # enkripsi dengan ROT13
    encrypted_text = rot13(original_text)

    # menanyakan apakah pengguna ingin melihat password yang didekripsi ?
    ask_show_decryp = input("do you want to show password decrypt ? [Y/N] : ").strip().lower()
    if ask_show_decryp == "Y" or ask_show_decryp == "y":    
        print(f"Decrypted text: {rot13(encrypted_text)}")
    elif ask_show_decryp == "N" or ask_show_decryp == "n":
        print("you chose not to display the decrypted password")
    elif ask_show_decryp == '':
        print("input tidak boleh kosong")
    else:
        print("input not valid")

    # menanyakan apakah pengguna ingin menyimpan password terenkripsi ke file? (untuk supaya tidak susah payah mengcopy-copy salinan encryp pass)
    ask_file = input("do you want output encrypt password to be a file.txt or not ? [Y/N] : ").strip().lower()
    if ask_file == "Y" or ask_file == "y":
        with open("coba.txt", "a") as f:
            f.write(f"encrypt pass : {encrypted_text}\n")
        print("Encrypted password has been saved to 'coba.txt'.")

        # open and read the file after appand
        # f = open("coba.txt", "r")
        # print(f.read())
    elif ask_file == "N" or ask_file == "n":
        print(f"Encrypted text: {encrypted_text}")
    elif ask_file == '':
        print("nggk boleh kosong ya....")
    else:
        print("input not valid")

if __name__ == "__main__":
    main()