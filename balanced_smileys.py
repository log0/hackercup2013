"""
Author: Eric Chio
Contact: im.ckieric@gmail.com
Initial commit date: 1/26/2013

Original Problem Statement:

Your friend John uses a lot of emoticons when you talk to him on Messenger. In addition to being a person who likes to express himself through emoticons, he hates unbalanced parenthesis so much that it makes him go :(

Sometimes he puts emoticons within parentheses, and you find it hard to tell if a parenthesis really is a parenthesis or part of an emoticon.

A message has balanced parentheses if it consists of one of the following:

- An empty string ""
- One or more of the following characters: 'a' to 'z', ' ' (a space) or ':' (a colon)
- An open parenthesis '(', followed by a message with balanced parentheses, followed by a close parenthesis ')'.
- A message with balanced parentheses followed by another message with balanced parentheses.
- A smiley face ":)" or a frowny face ":("
Write a program that determines if there is a way to interpret his message while leaving the parentheses balanced.

Input
The first line of the input contains a number T (1 ¡Ü T ¡Ü 50), the number of test cases. 
The following T lines each contain a message of length s that you got from John.

Output
For each of the test cases numbered in order from 1 to T, output "Case #i: " followed by a string stating whether or not it is possible that the message had balanced parentheses. If it is, the string should be "YES", else it should be "NO" (all quotes for clarity only)

Constraints
1 ¡Ü length of s ¡Ü 100



Problem:
Recursion to match parenthesis, except that you need to consider you can consider a parenthesis as part of the smileys, branching.

Solution:
Standard parenthesis matching but with branching (pick whichever that can return true).

INPUT:
5
:((
i am sick today (:()
(:)
hacker cup: started :):)
)(

OUTPUT:
Case #1: NO
Case #2: YES
Case #3: YES
Case #4: YES
Case #5: NO

"""

def r(s, k = 0):
    if k < 0: return False
    if s == '':
        if k == 0:
            return True
        else:
            return False
    
    if s[0] == '(':
        return r(s[1:], k+1)
    elif s[0] == ':':
        if s[1] in ['(', ')']:
            return r(s[2:], k) or r(s[1:], k)
        else:
            return r(s[1:], k)
    elif s[0] == ')':
        return r(s[1:], k-1)
    else:
        return r(s[1:], k)

def main(input):
    data = file(input).read().split('\n')
    n = int(data[0].strip())
    for i in xrange(n):
        if r(data[i+1]):
            print 'Case #%d: YES' % (i+1)
        else:
            print 'Case #%d: NO' % (i+1)

if __name__ == '__main__':
    main('balanced_smileystxt.txt')