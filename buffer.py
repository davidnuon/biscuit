class Buffer(object):
	"""docstring for Buffer"""
	def __init__(self):
		super(Buffer, self).__init__()
		self.lines = []	
		self.line = -1
		self.col  = 0

	def add_line(self, line):
		self.lines += [line]
		self.line += 1
		self.col = len(line) 
		return

	def add_char(self, char):
		cur = self.col
		edit_line = list(self.lines[self.line])
		edit_line = edit_line[0:cur] + list(char) + edit_line[cur:]
		self.lines[self.line] = "".join(edit_line)
		self.col += 1
		return self

	def __str__(self):
		buffy = ""
		for n in xrange(0, len(self.lines)):
			rendered_line = self.lines[n]
			if n == self.line:
				for c in xrange(0, len(rendered_line)):
					if(c == self.col - 1):
						buffy += "\033[47;1;30m"
						buffy += rendered_line[c]
						buffy += "\033[0m"
					else:
						buffy += rendered_line[c]
				buffy += '\n'
			else:
				buffy += rendered_line + '\n'

		return buffy

if __name__ == '__main__':
	import time
	import sys

	def frame():
		sys.stderr.write("\x1b[2J\x1b[H")
		print buffy
		time.sleep(1/24.0)

	buffy = Buffer()

	buffy.add_line("This is a test.")
	frame()
	buffy.add_line("This is a test.")
	frame()
	buffy.add_line("This is a test.")
	frame()
	buffy.add_line("This is a test.")
	frame()
	buffy.add_line("This is a test.")

	print buffy
	print 

	print buffy.line

	for c in " map :: (a -> b) -> [a] -> b":
		buffy.add_char(c)
		frame()
