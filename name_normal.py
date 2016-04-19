# coding=utf-8
import unicodedata

dictionnary = {
          ord(u'ä'): u'ae',
          ord(u'ö'): u'oe',
          ord(u'ü'): u'ue',
          ord(u'ß'): u'ss',
          ord(u'.'): None,
          ord(u':'): None
        }
        
def normalize_name(name):
	fullName = name.split()
	normalizedName = ""
	if len(fullName) > 1:
		for i in range(len(fullName)-1):
			initial = fullName[i][0]
			normalizedName += initial + " "
	normalizedName += fullName[-1]

	normalizedName = normalizedName.translate(dictionnary)
	normalizedName = unicodedata.normalize('NFKD', normalizedName).encode('ascii','ignore')
	return normalizedName