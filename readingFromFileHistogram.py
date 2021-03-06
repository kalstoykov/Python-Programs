# Python program to read a histogram from a file

from matplotlib import pyplot


filename = 'times_1201.txt'
lines = open(filename).readlines()
x = [int(line.strip()) for line in lines]
bins = [i * 1000 for i in range(10)]

pyplot.hist(x, bins=bins, facecolor='green', alpha=0.75)
pyplot.xlabel('Time (ms)')
pyplot.ylabel('Count')
pyplot.suptitle(r'Sup title')
pyplot.title(r'Title')
pyplot.grid(True)
pyplot.savefig(filename + '.png')
