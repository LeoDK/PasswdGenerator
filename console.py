# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import sys

class Console:

    NUMBERS=0
    PUNCTUATION=1
    LOWERCASE=2
    UPPERCASE=3
    LETTERS=4

    _args = None

    def __init__(self):
        argparser = ArgumentParser()

        #Positionnal argument
        argparser.add_argument("length", help="The password length", type=int)

        #Optionnal argument
        argparser.add_argument("-n", "--numbers", help="Include numbers", action="store_true")
        argparser.add_argument("-p", "--punctuation", help="Include punctuation", action="store_true")
        argparser.add_argument("-u", "--lowercase", help="Only lowercase letters (only with -l)", action="store_true")
        argparser.add_argument("-U", "--uppercase", help="Only uppercase letters (only with -l)", action="store_true")
        argparser.add_argument("-l", "--letters", help="Include letters", action="store_true")

        self._args = argparser.parse_args()

        if self._args.letters == True and self._args.uppercase == False and self._args.lowercase == False:
            self._args.uppercase = True
            self._args.lowercase = True

    def getPositionnalArgs(self):
        a = self._args

        tab = (a.numbers, a.punctuation, a.lowercase, a.uppercase, a.letters)

        return tab

    def getLength(self):
        return self._args.length
