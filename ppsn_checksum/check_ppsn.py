#!/usr/bin/env python3
import re


def check_ppsn(ppsn):
	not_valid = f'{ppsn} is not a valid PPSN'
	valid = f'{ppsn} is valid'
	# validate the PPSN
	validation = re.search(r'^(\d{7})([a-zA-Z])([a-zA-Z]?)$', ppsn)
	if validation is None:
		return not_valid
	# validate the checksum
	count = 8
	sum = 0
	alphabet = 'wabcdefghijklmnopqrstuv?xyz'
	for digit in validation[1]:
		sum += int(digit) * count
		count -= 1
	if len(ppsn) == 9:
		sum += alphabet.index(validation[3].lower()) * 9
	if alphabet[sum % 23] != validation[2].lower():
		return not_valid
	return valid
