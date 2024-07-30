class Codex:
    @classmethod
    def generate_hashkey(cls):

        from random import randint
        codex = " qwertyuıopğüişlkjhgfdsazxcvbnmöçQAZWSXEDCRFVTGBYHNUJMIKÖOLÇPŞĞİÜ1234567890!'^+%&@/()=?_-|<>.,;:£#\n$½{[]}\"\\"
        hashkey = ""

        hashkey_index_list = []

        for i in range(len(codex)):
            index_in_list = True
            while index_in_list:
                random_index = randint(0,len(codex)-1)
                if not random_index in hashkey_index_list:
                    hashkey_index_list.append(random_index)
                    hashkey += codex[random_index]
                    index_in_list = False
        
        return hashkey


    @classmethod
    def convert_text(cls,hashkey,text):
        if len(hashkey)!=107:
            log = "Hashkey length must be 107 non repetitive characters!\nOtherwise the program will malfunction!"
            return log

        algorithm_controller = 19

        pair1 = {}
        pair2 = {}
        
        key_list = list(pair1.keys())
        val_list = list(pair1.values())


        for a in range(10):
            pair1[hashkey[a]] = hashkey[a+10]

        for b in range(20,30):
            pair1[hashkey[b]] = hashkey[b+algorithm_controller]
            algorithm_controller -= 2

        for x in range(40,45):
            pair1[hashkey[x]] = hashkey[x+5]


        pair1[hashkey[50]] = hashkey[52]
        pair1[hashkey[51]] = hashkey[53]
        pair1[hashkey[54]] = hashkey[56]
        pair1[hashkey[55]] = hashkey[57]
        pair1[hashkey[58]] = hashkey[60]
        pair1[hashkey[59]] = hashkey[61]


        algorithm_controller = 21       

        for x in range(62,73):
            pair1[hashkey[x]] = hashkey[x+algorithm_controller]
            algorithm_controller -= 2

        for x in range(84,95):
            pair1[hashkey[x]] = hashkey[x+11]
        #create the values of the keys
        for char in pair1:
            pair2[pair1.get(char)] = char

        output = ""

        for character in text:
            try:
                add_char = pair1.get(character,"") #add_char is the char that is decrypted
                if add_char=="":
                    add_char = pair2.get(character,"")

            except Exception as exce:
                print(f"Exception caught: {exce}")
               
            
            if add_char =="":
                output +=character
                print(character,end='')

            output+=add_char

        return output


    @classmethod
    def save_hashkey(cls,hashkey,filename):
        def write(hashkey,filename):
            try:
                with open(filename,'w') as writeFile:
                    pass
            except:
                print("An error occurred while creating file")

        hashkey+="\n"
        try:
            with open(filename,'a') as appendFile:
                appendFile.write(hashkey)
        except:
            try:
                write(hashkey,filename)
                with open(filename,'a') as appendFile:
                    appendFile.write(hashkey)
            except:
                print("Third except")



text = "merhaba ben hasan!'\n"
"""
while True:
    try:
        x = Codex.generate_hashkey()
        print("Generated")
        encrypted = Codex.convert_text(x,text)

        print("produced.",encrypted)

        decrypted = Codex.convert_text(x,encrypted)

        print("d:",decrypted)
        if decrypted!=text:
            break
    except Exception as f:
        print("****\n**\nException: ",end="")
        input(f)


"""





    


