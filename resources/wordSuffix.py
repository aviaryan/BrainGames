# removes words which are different by suffixes from the list

fname = 'corncob_caps.txt'
# assumes word list is sorted

suffixes = ['S'] # other suffixes like -ing are ok.. but this seriously hurts

words = set()

def rtrim(string, wordarray):
	for i in wordarray:
		if string.endswith(i):
			return string[:-1 * len(i)]
	return string

with open(fname) as f:
	for line in f:
		if not line[:-1].isalpha():
			continue
		line = line.strip() # remove \n
		trimline = rtrim(line, suffixes)
		if trimline not in words:
			words.add(line)

out = '\n'.join( sorted(words) )
open(fname + '.txt', 'w').write(out)