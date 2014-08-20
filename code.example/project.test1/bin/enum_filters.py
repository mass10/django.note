#!/usr/bin/env python
# coding: utf-8

import sys
import subprocess
import time
import json

def _create_node(tree, name):

	if tree.has_key(name):
		return

	tree[name] = []

def main():

	command_text = [
		'sudo',
		'-u',
		'root',
		'/sbin/iptables',
		'--list',
		'-nvx',
		'--line-numbers' ]

	stream = subprocess.Popen(
		command_text,
		shell=False,
		stdout=subprocess.PIPE).stdout

	result = {}

	current_section = None

	for line in stream:

		line = line.strip()
		if line == '':
			continue

		fields = line.split()
		if fields[0] == 'num':
			continue
		elif fields[0] == 'Chain':
			if fields[1] == 'INPUT':
				current_section = 'INPUT'
				_create_node(result, current_section)
			elif fields[1] == 'FORWARD':
				current_section = 'FORWARD'
				_create_node(result, current_section)
			elif fields[1] == 'OUTPUT':
				current_section = 'OUTPUT'
				_create_node(result, current_section)
			else:
				pass
		else:
			if current_section == None:
				continue
			result[current_section].append(line)

	stream.close()

	json.dump(result, sys.stdout, indent=True)

	#改行の意味
	print

main()
