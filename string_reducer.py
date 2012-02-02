import sys
from collections import defaultdict

transforms = defaultdict(str)
transforms['ab'] = 'c'
transforms['ba'] = 'c'
transforms['ac'] = 'b'
transforms['ca'] = 'b'
transforms['bc'] = 'a'
transforms['cb'] = 'a'

finals = set()
for i in range(1, 101):
    finals.add('a'*i)
    finals.add('b'*i)
    finals.add('c'*i)
    
def greedy_reducer(string):
    m = len(string)
    i = 0
    while i < len(string)-1:   
        if string[i] != string[i+1]:
            parts = (string[:i], transforms[string[i:i+2]], string[i+2:])
            n_string = ''.join(parts)
            if len(n_string) == 1:
                return 1
            elif n_string in finals:
                m = min(m, len(n_string))
                i += 1
            else:
                string = n_string
                i = 0                
        else:
            i += 1                    
    return min(m, len(string))

def main(string):
    if len(set(string)) == 1:
        return len(string)
    return greedy_reducer(string)

if __name__ == '__main__':
    line = sys.stdin.readline()
    num_tests = int(line.strip())
    tstrings = []
    for i in range(num_tests):        
        test_string = sys.stdin.readline()
        tstrings.append(test_string.strip())
    for x in tstrings:
        print "%d" % (main(x),)