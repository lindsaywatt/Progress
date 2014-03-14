from sys import stdout
from timeit import timeit

class Progress(object):
	def __init__(self, iterations, columns = 50, char = "|"):
		if iterations <= 0:
			raise ValueError("Iterations must be greater than 0")
		if columns <= 0:
			raise ValueError("Number of bars must be greater than 0")
		if type(char) != str:
			raise TypeError("Character must be a character")
		self._iters = iterations
		self._num_bars = columns
		self._char = char
		if self._iters > self._num_bars:
			self._tick = float(self._iters) / self._num_bars
			self._num_print = 1
		else:
			self._tick = 1
			self._num_print = self._num_bars / float(self._iters)
		self._excess = 0
		self._iter = 0
		self._first_tick = True

	def tick(self, stdoutDisplay = True):
		"""call tick() each iteration, if display => updates progress bar in console"""
		self._iter += 1
		if self._iter % self._tick < 1 and stdoutDisplay:
			if self._first_tick:
				stdout.write("   " + self._char)
				self._first_tick = False
			num_print = self._num_print
			if self._num_print > 1:
				num_print = int(self._num_print)
				self._excess += self._num_print % 1
				if self._excess >= 1:
					num_print += int(self._excess)
					self._excess = self._excess % 1
			stdout.write(num_print * self._char)

	def bar(self):
		"""bar() => str (returns a progress bar header)"""
		return "0% " + self._char + ((self._num_bars - 1) * len(self._char) * " ") + self._char + " 100%"

	def progress(self):
		return (float(self._iter) / self._iters) * 100

	def __str__(self):
		return str(int(self.progress())) + "%"



if __name__ == "__main__":
	
	from time import sleep
	#lengthy tasks simulated by "sleep()"

	print "Example 1:\n" 
	repeats = 35
	p = Progress(repeats, 50, "*")
	print p.bar()
	for iteration in range(repeats):
		p.tick()
		sleep(0.03)

	print "\n\nExample 2:\n"
	repeats = 1000
	p = Progress(repeats)
	for iteration in range(repeats):
		p.tick(False)
		prog = p.progress()
		if prog % 25 == 0:
			print p, " done"
		sleep(0.003)
	raw_input()
