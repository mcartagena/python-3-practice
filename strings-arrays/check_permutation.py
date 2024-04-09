# Check Permutation:  Given two strings, write a method to decide if one is a permutation
# of the other.  I considered the alphabet letters and lowercase

def check_permutation(word1, word2):
    if len(word1) != len(word2) :
        return False
    count_chars = [0]*26
    for char in word1:
        if ord(char) < ord('a') or ord(char) > ord('z'):
            print('Invalid word 1')
            return False
        count_chars[ord(char) - ord('a')] += 1

    for char in word2:
        if ord(char) < ord('a') or ord(char) > ord('z'):
            print('Invalid word 2')
            return False
        count_chars[ord(char) - ord('a')] -= 1
        if count_chars[ord(char) - ord('a')] < 0:
            return False
    return True

print(check_permutation("god","dog"))
print(check_permutation("car","dog"))
print(check_permutation("god","dogs"))
