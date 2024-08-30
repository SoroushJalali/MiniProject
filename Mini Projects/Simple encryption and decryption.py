while True:
    print("Choose the option you want")
    chosen = input("\t1)encryption\n\t2)decryption\n\t3)exit\n\t")
    if chosen == "1":
        text = input("Send the message you want encrypted:\n")
        encrypted_text = ""
        for i in text:
            encrypted_text += chr(int(str((ord(i) * 7) - 13)))
        print(encrypted_text)
        print("*" * 40, "\n")
    elif chosen == "2":
        text = input("Send the message you want to be decoded:\n")
        decrypted_text = ""
        for i in text:
            decrypted_text += chr(int(str((ord(i) + 13) // 7)))
        print(decrypted_text)
        print("*" * 40, "\n")
    elif chosen == "3":
        print("The operation is over")
        print("*" * 40)
        break
    else:
        print("The selected option is not correct,try again")
        print("*" * 40, "\n")
