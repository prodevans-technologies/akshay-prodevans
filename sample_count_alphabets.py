str=raw_input("Enter String\n")

vowel_count=0
consonant_count=0
other_words_count=0

#print "\n"

for char in str:
    if char.isalpha():
        if char in "aeiouAEIOU":
            vowel_count += 1
        else:
            consonant_count += 1
    else:
        other_words_count += 1

print "Vowel Count :- %i" % (vowel_count)
print "Consonant :- %i" % (consonant_count)
print "Other Words :- %i" % (other_words_count)
