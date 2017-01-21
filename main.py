#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A simple password generator

from random import randint, choice

def generate_password(length):
	l_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	l_num = [str(i) for i in range(10)]
	
	your_password = ""
	for i in range(length):
		rnd_num = randint(0, 1)
		if rnd_num == 0:
			your_password += choice(l_alpha)
		else:
			your_password += choice(l_num)
	
	return your_password
	
if __name__ == "__main__":
	length = 8
	password = generate_password(length)
	print("Your password :", password)
