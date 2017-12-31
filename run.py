#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from console import Console
from generator import Generator

c = Console()

g = Generator(c.getPositionnalArgs(), c.getLength())

print(g.generatePassword())
