# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# I considered only alphabet letters and lowercase

def is_unique(word):
    alphabet_count = [0]*26
    for char in word:
        if ord(char) < ord('a') or ord(char) > ord('z'):
            print('Invalid word')
            return False
        if alphabet_count[ord(char) - ord('a')] == 1:
            return False
        alphabet_count[ord(char) - ord('a')] = 1
    return True

print(is_unique("hello"))
print(is_unique("Hello"))
print(is_unique("car"))