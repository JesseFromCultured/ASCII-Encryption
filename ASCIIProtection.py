# password conditions---------------------------------------------------------------------------------------------------

print("""
-------------------------------------------------------
Welcome To My Application, Please Create A Password
-------------------------------------------------------
Password Needs to:                                
   - Have At least 1 Capital                     
   - Have At least 1 Number                      
   - Have No Spaces                              
   - Be At least 5 characters                    
-------------------------------------------------------""")

# vars------------------------------------------------------------------------------------------------------------------

passwordGood = False

# conformation = "y"

# conformationD = "y"

conformationE = "y"

done = False

doneD = False

doneE = False

selectAgain = True
your_pass = ''
# Checking password conditions------------------------------------------------------------------------------------------

while not passwordGood:

    passwordHaveUpper = False

    passwordHasDigits = False

    passwordLengthGood = False

    passwordNoSpaces = False

    spaceCount = 0
    your_pass = input("What would you like your password to be: ")
    if len(your_pass) >= 5:
        passwordLengthGood = True

    for x in your_pass:
        if x == " ":
            spaceCount += 1
        if x.isupper():
            passwordHaveUpper = True
        if x.isdigit():
            passwordHasDigits = True

    if spaceCount > 0:
        passwordNoSpaces = False
    else:
        passwordNoSpaces = True

    if passwordLengthGood and passwordHasDigits and passwordHaveUpper and passwordNoSpaces:
        passwordGood = True
        print("\nPassword Satisfies Reqs!\n")

    # One thing wrong-------------------------------------------------------------------------------------------------------

    elif passwordLengthGood and passwordHasDigits and passwordHaveUpper and not passwordNoSpaces:
        print("Password Has Spaces, Please Try Again")
    elif not passwordLengthGood and passwordHasDigits and passwordHaveUpper and passwordNoSpaces:
        print("Password is too Short, Please Try Again")
    elif passwordLengthGood and not passwordHasDigits and passwordHaveUpper and passwordNoSpaces:
        print("Password Requires a Number, Please Try Again")
    elif passwordLengthGood and passwordHasDigits and not passwordHaveUpper and passwordNoSpaces:
        print("Password Requires an Uppercase Letter, Please Try Again")

    # Two things wrong -----------------------------------------------------------------------------------------------------

    elif passwordLengthGood and passwordHasDigits and not passwordHaveUpper and not passwordNoSpaces:
        print("Password Has Spaces and Requires an Uppercase Letter, Please Try Again")
    elif passwordLengthGood and not passwordHasDigits and passwordHaveUpper and not passwordNoSpaces:
        print("Password Has Spaces and Requires a Number, Please Try Again")
    elif passwordLengthGood and not passwordHasDigits and not passwordHaveUpper and passwordNoSpaces:
        print("Password Requires an Uppercase Letter and a Number, Please Try Again")
    elif not passwordLengthGood and passwordHasDigits and passwordHaveUpper and not passwordNoSpaces:
        print("Password is too Short and Has Spa/lkces, Please Try Again")
    elif not passwordLengthGood and passwordHasDigits and not passwordHaveUpper and passwordNoSpaces:
        print("Password Requires an Uppercase Letter and is too Short, Please Try Again")
    elif not passwordLengthGood and not passwordHasDigits and passwordHaveUpper and passwordNoSpaces:
        print("Password Requires a Number and is too Short, Please Try Again")

    # Three things wrong ---------------------------------------------------------------------------------------------------

    elif not passwordLengthGood and not passwordHasDigits and not passwordHaveUpper and passwordNoSpaces:
        print("Password is too short, and Requires a number and an Uppercase Letter, Please Try Again")
    elif passwordLengthGood and not passwordHasDigits and not passwordHaveUpper and not passwordNoSpaces:
        print("Password Has Spaces, and Requires a Number and an Uppercase Letter, Please Try Again")
    elif not passwordLengthGood and passwordHasDigits and not passwordHaveUpper and not passwordNoSpaces:
        print("Password is too Short, Has Spaces, and Requires an Uppercase Letter, Please Try Again")
    elif not passwordLengthGood and not passwordHasDigits and passwordHaveUpper and not passwordNoSpaces:
        print("Password is too Short, Has Spaces, and Requires a Number, Please Try Again")

    # Four things wrong ----------------------------------------------------------------------------------------------------

    elif not passwordLengthGood and not passwordHasDigits and not passwordHaveUpper and not passwordNoSpaces:
        print("""Password Needs to:
       - Have At least 1 Capital
       - Have At least 1 Number
       - Have No Spaces
       - Be At least 5 characters\n""")

correct_pass = False

# Function for decoding The Encrypted Message from before --------------------------------------------------------------


def decode_function(emessage):

    characterslist = []

    tempStr = ''

    for c in emessage:
        if c == '_':
            characterslist.append((chr(int(tempStr))))
            tempStr = ""
        else:
            tempStr += c
    decrypted = ''
    for f in characterslist:
        decrypted += f

    print(decrypted)


# Checking if the password is correct-----------------------------------------------------------------------------------


while not correct_pass:

    passwordInput = input("Enter Password To Access Unicode Application: ")

    if passwordInput == your_pass:
        while selectAgain:
            correct_pass = True
            selection = input("Would you like to Translate, Decode, or Use the Enigma Machine?('t' or 'd' or 'e'): ")

            # Enigma----------------------------------------------------------------------------------------------------------------

            if selection == "e":

                print("\n\n\n     Enigma Machine      \n\n\n")

                while conformationE == "y":

                    while not doneE:

                        # EnigmaMachine--------------------------------------------------------------------------------------------------------

                        # Consists of three rotors and a reflector, settings can be entered manually

                        # The starting rotors and their step settings as tuples
                        alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

                        # Enigma 1 Rotors 1, 2, 3
                        rotor_1_list = (list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), 17)
                        rotor_2_list = (list("AJDKSIRUXBLHWTMCQGZNPYFVOE"), 5)
                        rotor_3_list = (list("BDFHJLCPRTXVZNYEIWGAKMUSQO"), 22)

                        # Enigma Navy Reflector B
                        refl_b_list = list("YRUHQSLDPXNGOKMIEBFZCWVJAT")


                        # The rotor class represents a single rotor in the enigma machine
                        # The constructor takes an array representing the starting settings, a step, and
                        # a current count
                        class rotor:
                            def __init__(self, inner_rotor, step, count=0):
                                self.count = count
                                self.step = step
                                self.inner_map = dict(zip(alpha, inner_rotor))
                                self.refl_map = dict(zip(inner_rotor, alpha))
                                self.input_map = dict(zip(alpha, rotate(alpha, self.count)))
                                self.output_map = dict(zip(alpha, rotate(alpha, -self.count)))

                            def __repr__(self):
                                return "Count: {!r}\nInner Map: {!r}\n".format(self.count, self.inner_map)

                            # Increments the rotor count by one and updates the input and output maps
                            def update(self):
                                self.count = (self.count % 26) + 1
                                self.input_map = dict(zip(alpha, rotate(alpha, self.count)))
                                self.output_map = dict(zip(alpha, rotate(alpha, -self.count)))

                            # Passes a single letter through the input map, inner ring, and output map
                            def rotor_enc(self, let, reflected=False):
                                let = self.input_map[let]

                                # if the letter has been reflected, use the reflector ring
                                if reflected:
                                    let = self.refl_map[let]
                                else:
                                    let = self.inner_map[let]
                                return self.output_map[let]


                        # The enigma class represents the enigma machine
                        # The enigma constructor initializes all three rotors and the reflector
                        class enigma:
                            def __init__(self, settings=[0, 0, 0]):
                                self.r1 = rotor(rotor_1_list[0], rotor_1_list[1], settings[0])
                                self.r2 = rotor(rotor_2_list[0], rotor_2_list[1], settings[1])
                                self.r3 = rotor(rotor_3_list[0], rotor_3_list[1], settings[2])
                                self.refl = refl_b_list

                            def __repr__(self):
                                return "---Rotor1---\n{!r}\n---Rotor2---\n{!r}\n---Rotor3---\n{!r}\n".format(
                                    self.r1, self.r2, self.r3
                                )

                            # Updates the enigma machine and rotors accordingly, then encrypts a single
                            # letter
                            def enc_letter(self, let):

                                # always updates rotor three
                                self.r3.update()

                                if self.r2.count == self.r2.step: self.r1.update()
                                if self.r3.count == self.r3.step + 1 and self.r2.count == self.r2.step:
                                    self.r2.update()
                                # rotors 1 and 2 are updated if the count equals the step
                                if self.r3.count == self.r3.step: self.r2.update()

                                # The letter passes through rotor 3 -> rotor 2 -> rotor 1 -> reflector
                                # rotor 1 -> rotor 2 -> rotor 3
                                let = self.r1.rotor_enc(self.r2.rotor_enc(self.r3.rotor_enc(let)))
                                let = alpha[self.refl.index(let)]

                                # letter passes through 1 -> 2 -> 3 after hitting the reflector
                                let = self.r3.rotor_enc(self.r2.rotor_enc(self.r1.rotor_enc(let, True), True), True)
                                return let


                        # Main method, deals with user IO and initializing the enigma machine
                        def main():
                            set = input("\nInput start settings (ex. 5, 26, 12): ")

                            # checks if valid start settings have been entered
                            while not set.replace(", ", "").isnumeric() or len(set.split(",")) != 3:
                                set = input("NOT VALID\nInupt start settings (ex. 5, 26, 12): ")
                            set = set.split(",")
                            enig_ma = enigma([int(set[i]) for i in range(3)])

                            # loops until the user inputs "quit"
                            while True:
                                print("\nSETTINGS: {!r}, {!r}, {!r}".format(enig_ma.r1.count,
                                                                            enig_ma.r2.count, enig_ma.r3.count))
                                inp = input("Input a word to be encoded(type 'quit' to quit): ")
                                while not inp.replace(" ", "").isalpha():
                                    inp = input("NOT VALID\nInput a word to be encoded: ")
                                if inp == "quit":
                                    print("EXITING ENIGMA....")
                                    break
                                if inp == "reset":
                                    print("RESETTING")
                                    enig_ma = enigma([int(set[i]) for i in range(3)])
                                    continue
                                print(enigma_enc(enig_ma, inp.upper().replace(" ", "")))


                        # encodes all the letters in a given input
                        def enigma_enc(enig_ma, inp):
                            return "".join(enig_ma.enc_letter(c) for c in inp)


                        # rotates a list by an amount n
                        def rotate(list, n):
                            return list[n:] + list[:n]


                        if __name__ == "__main__":
                            main()

                        conformationE = input("Would you like to encrypt another message?('y' or 'n'): ")

                        if conformationE == "n":

                            selectAgainE = input("Would You Like to Run Another Program?('y' or 'n'): ")

                            if selectAgainE == "y":
                                selection = ''
                                selectAgain = True
                                doneE = False
                            elif selectAgainE == "n":
                                selectAgain = False
                                doneE = True
                                selection = ''
                            else:
                                print("Not An Option, Try Again")

            # Encrypting------------------------------------------------------------------------------------------------------------

            elif selection == "t":

                print("\n\n\n         Jesse's ASCII Cipher          \n\n\n")
                conformation = 'y'
                doneE = False
                while not doneE:
                    while conformation == "y":

                        your_message = input("What Would You Like Your Message to Be: ")

                        encrypted_string = ''.join(str(ord(c)) + '_' for c in your_message)

                        print(encrypted_string)

                        conformation = input("Would you like to translate another?('y' or 'n'): ")

                        if conformation == "n":

                            selectAgainT = input("Would you like to run another program?('y' or 'n'): ")

                            if selectAgainT == "y":
                                selection = ''
                                selectAgain = True
                                doneE = True
                            elif selectAgainT == "n":
                                selectAgain = False
                                doneE = True
                                selection = ''
                            else:
                                print("Not An Option, Try Again")

            # Decoding--------------------------------------------------------------------------------------------------------------

            elif selection == "d":

                print("\n\n\n       Jesse's ASCII Decoder         \n\n\n")
                conformationD = 'y'
                doneD = False
                while conformationD == "y":

                    while not doneD:

                        your_message_to_decode = input("What Would You Like to Decode: ")

                        decode_function(your_message_to_decode)

                        conformationD = input("Would you like to Decode Another Message?('y' or 'n'): ")

                        if conformationD == "n":
                            selectAgainD = input("Would you like to run another program?('y' or 'n'): ")

                            if selectAgainD == "y":
                                selection = ''
                                selectAgain = True
                                doneD = True
                            elif selectAgainD == "n":
                                selectAgain = False
                                doneD = True
                                selection = ''
                            else:
                                print("Not An Option, Try Again")

    else:
        print("Incorrect Password Try Again")
        correct_pass = False











