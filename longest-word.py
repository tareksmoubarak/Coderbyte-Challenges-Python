def longestWord(string):
    array = string.split()
    max = ''
    for word in array:
        if (len(word) > len(max)):
            max = word
    return max

print longestWord(raw_input())