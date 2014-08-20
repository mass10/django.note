#!/usr/bin/env python
# coding: utf-8

import sys
import json
import subprocess
import time

def main():

	command_text = ['sudo', '-u', 'root', '/bin/netstat', '-ntlp']

	stream = subprocess.Popen(
		command_text,
		shell=False,
		stdout=subprocess.PIPE).stdout

	result = []

	current_section = None

	for line in stream:

		line = line.strip()

		if line == '':
			continue

		print(line)
		# result.append(line)

	stream.close()

	# json.dump(result, sys.stdout, indent=True)

main()
