"""
Author: Eric Chio
Contact: im.ckieric@gmail.com
Initial commit date: 1/26/2013

Original Problem Statement:

When John was a little kid he didn't have much to do. There was no internet, no Facebook, and no programs to hack on. So he did the only thing he could... he evaluated the beauty of strings in a quest to discover the most beautiful string in the world.
Given a string s, little Johnny defined the beauty of the string as the sum of the beauty of the letters in it.
The beauty of each letter is an integer between 1 and 26, inclusive, and no two letters have the same beauty. Johnny doesn't care about whether letters are uppercase or lowercase, so that doesn't affect the beauty of a letter. (Uppercase 'F' is exactly as beautiful as lowercase 'f', for example.)
You're a student writing a report on the youth of this famous hacker. You found the string that Johnny considered most beautiful. What is the maximum possible beauty of this string?

Input
The input file consists of a single integer m followed by m lines.

Output
Your output should consist of, for each test case, a line containing the string "Case #x: y" where x is the case number (with 1 being the first case in the input file, 2 being the second, etc.) and y is the maximum beauty for that test case.

Constraints
5 ¡Ü m ¡Ü 50
2 ¡Ü length of s ¡Ü 500



Problem:
Given a string with alphabets, and with each character assigned a value of 1 to 26. Find the maximum value among the possible assignment choices.

Solution:
Just assign from 26 to 1 according to the count of characters, then do a summation.

INPUT:
5
ABbCcc
Good luck in the Facebook Hacker Cup this year!
Ignore punctuation, please :)
Sometimes test cases are hard to make up.
So I just go consult Professor Dalves

Case #1: 152
Case #2: 754
Case #3: 491
Case #4: 729
Case #5: 646

"""

import string
from collections import Counter

def solve(s):
	c = Counter(filter(lambda x : x in string.lowercase, list(reversed(sorted(s.lower())))))
	sum = 0
	count = 26
	for i in c.most_common(100):
		sum += count * i[1]
		count -= 1
	return sum

def main(input):
	data = file(input).read().split('\n')
	n = int(data[0].strip())
	for i in xrange(n):
		print 'Case #%d: %d' % (i+1, solve(data[i+1]))

if __name__ == '__main__':
    main('beautiful_stringstxt.txt')