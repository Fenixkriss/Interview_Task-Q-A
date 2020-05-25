# Capitalize string consisting of words separated by _ or - and returns a string in camel case
# Example:
# the_phantom_menace -> thePhantomMenace The-Phantom-Menace -> ThePhantomMenace

phrase = 'the_phantom_menace'
#phrase = 'Phantom-oF-the-oPera' #Test phrase. Uncomment for test

# split-capitalize-connect
words = phrase.split('_') if '_' in phrase else phrase.split('-')
result = words[0]
for word in words[1:]:
	result += word.title()

print(result)