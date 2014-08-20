#!/usr/bin/env python
# coding: utf-8

import sys
import json
import subprocess
import time

def main():

	command_text = [ 'sudo', '-u', 'root', '/bin/cat', '/etc/passwd' ]

	stream = subprocess.Popen(
		command_text,
		shell=False,
		stdout=subprocess.PIPE).stdout

	result = []

	for line in stream:
		line = line.strip()
		if line == '':
			continue
		if line.index(':') == -1:
			continue
		fields = line.split(':')
		result.append(fields[0])

	stream.close()

	json.dump(result, sys.stdout, indent=4)

	# 改行の意味
	print

main()
