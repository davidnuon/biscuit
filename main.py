import sys
import time

LINE_ENDING = '\n'
text = sys.stdin.read().split(LINE_ENDING)[::-1]

buffy = ""
while len(text) > 0:
	current = text.pop()
	for c in current:
		buffy += c
		sys.stderr.write("\x1b[2J\x1b[H")
		print buffy
		time.sleep(1/24.0)
	buffy += LINE_ENDING
