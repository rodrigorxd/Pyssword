import random
import encrypt
import api_check
import art

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "&", "*"]

password = []

finish = False

while not finish:
    art.menuPrincipal()
    #menu
    option = int(input("1 - Password Generator\n2 - Check password leak\n3 - Quit\n\nChoose an option:\n"))
    match option:
        #Password Generator - Gerador de senha
        case 1:
            try:
                qt_letters = int(input("Type the desired quantity of letters:"))
                if type(qt_letters) == int and qt_letters >= 0:
                    #Choose random letters (accordingly to quantity specified) - Escolher letras aleatórias de acordo com a quantidade especificada
                    for i in range(qt_letters):
                        chosen_digit = random.choice(letters)
                        password.append(chosen_digit)
                    qt_numbers = int(input("Type the desired quantity of numbers:"))
                    if type(qt_numbers) == int and qt_numbers >= 0:
                        for i in range(qt_numbers):
                            chosen_digit = random.choice(numbers)
                            password.append(chosen_digit)
                        qt_symbols = int(input("Type the desired quantity of symbols:"))
                        if type(qt_symbols) == int and qt_symbols >= 0:
                            for i in range(qt_symbols):
                                chosen_digit = random.choice(symbols)
                                password.append(chosen_digit)
                            #Shuffle digits - Ordem aleatória na senha gerada
                            random.shuffle(password)
                            #Password from list to plain text - Transformar senha gerada em texto comum
                            final_pass = ''.join(password)
                            print(f"\nHere is your password:\t{final_pass}\n")
            except ValueError:
                print("Invalid number, trying again...")
            input("- Press enter to continue -")
        #Check if password was leaked - API
        case 2:
            connection_status = api_check.connection()
            if connection_status == 200:
                pass_check = input("Type the password to check if it was leaked:")
                #Encrypt given password to SHA1
                encrypted = encrypt.encrypt_password(pass_check)
                #Store first 5 digits
                first_search = encrypt.first_five(encrypted)
                #Store remaining digits
                second_search = encrypt.second_part(encrypted)
                #First 5 digits ocurrencies
                first_report = api_check.first_content(first_search)
                #Final result - given password ocurrencies
                leak_result = api_check.second_content(second_search, first_report)
                if leak_result == True:
                    art.attentionLeak()
                    print(f"Check the hash (SHA1): {encrypted}")
                else:
                    art.safePassword()
            else:
                print("For some reason we couldn't connect to the database, check your connection or comeback later :)")
            input("- Press enter to continue -")
        case 3:
            print("\nThank you for using Pyssword!\ngithub.com/rodrigorxd")
            finish = True
        case _:
            print("Invalid option, trying again...")
