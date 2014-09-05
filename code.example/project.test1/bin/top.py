#!/usr/bin/env python
# coding: utf-8
#
# root による top の実行
#
#

import sys
import json
import subprocess
import time

def main():

	command_text = [ 'sudo', '-u', 'root', '/usr/bin/top', '-b', '-n', '1' ]

	stream = subprocess.Popen(
		command_text,
		shell=False,
		stdout=subprocess.PIPE).stdout

	result = []

	for line in stream:
		line = line.strip()
		if line == '':
			continue
		result.append(line)

	stream.close()

	json.dump(result, sys.stdout, indent=4)
	print

main()
