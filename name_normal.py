# coding=utf-8
import unicodedata

dictionnary = {
          ord(u'ä'): u'ae',
          ord(u'ö'): u'oe',
          ord(u'ü'): u'ue',
          ord(u'ß'): u'ss',
          #ord(u'.'): None
        }
        
def normalize_name(name):
	name = name.translate(dictionnary)
	name = unicodedata.normalize('NFKD', name).encode('ascii','ignore')
	return name