from collections import deque
    
def palindrome(string):
    string = string.replace(' ', '').lower()
    s = deque(string)
    while len(s) > 1:
        if s.popleft() != s.pop():
            print(f'The string is not palindrome')
            return
    print(f'The string is palindrome')


palindrome('Madam In Eden Im Adam')
        
