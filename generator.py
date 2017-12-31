# -*- coding: utf-8 -*-

import random
from console import Console

class Generator:

    LOWERCASE = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    NUMBERS = ['0', '1','2','3','4','5','6','7','8','9']
    PUNCTUATION = ['.',';','/','^','%','$','!',':','?','#','~','-','+','*','\\']

    _letters = False
    _numbers = True
    _lowercase = False
    _uppercase = False
    _punctuation = False

    _length = 0

    def __init__(self, args, length=10):

        try:
            assert type(args) is tuple
            
            for boolean in args:
                assert type(boolean) is bool
            
            assert type(length) is int

        except:
            print("Generator error.")
                                  
        self._length = length

        self._numbers = False
        self._letters = False
        self._uppercase = False
        self._lowercase = False
        self._punctuation = False

        if (args[Console.NUMBERS] == True):
            self._numbers = True
        if (args[Console.LETTERS] == True):
            self._letters = True
        if (args[Console.LOWERCASE] == True):
            self._lowercase = True
        if (args[Console.UPPERCASE] == True):
            self._uppercase = True
        if (args[Console.PUNCTUATION] == True):
            self._punctuation = True

        ok = False

        for arg in args:
            if arg == True:
                ok = True

        if ok == False:
            self._numbers = True

    def setLength(self, length):
        if length==0:
            self._length = 10
        else:
            self._length = length
                    

    def generatePassword(self):
        code = ""
        
        for i in range(self._length):
            
            while True:

                ran = random.randint(0, 4) #On a le choix entre numbers, punctuation, lowercase et uppercase
    
                if (self._letters == True):
                    ran2 = random.randint(0,25)
    
                    if (ran == Console.LOWERCASE and self._lowercase == True):
                        code += Generator.LOWERCASE[ran2]
                        break

                    if (ran == Console.UPPERCASE and self._uppercase == True):
                        code += str.upper(Generator.LOWERCASE[ran2])
                        break
                        
                if (ran == Console.NUMBERS and self._numbers == True):
                    ran2 = random.randint(0,9)
                    code += Generator.NUMBERS[ran2]
                    break

                if (ran == Console.PUNCTUATION and self._punctuation == True):
                    ran2 = random.randint(0, len(Generator.PUNCTUATION)-1)
                    code += Generator.PUNCTUATION[ran2]
                    break
                
        return code   
