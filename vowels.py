s = 'azcbobobegghakl'

def checkVowels(string):
    vowel_count = 0
    for x in string:
        if x in ('a', 'e', 'i', 'o', 'u'):
            vowel_count += 1
            print vowel_count
    print 'Number of vowels:', vowel_count

checkVowels(s)
