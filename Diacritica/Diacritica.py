#!/usr/local/python
#-*- coding: iso8859-2 -*-

'''
Executa:
python /home/matei/Documents/Python/Diacritica/Diacritica.py 

Coduri de lang. ref. subtitrari:
https://www.facebook.com/help/1528795707381162?helpref=faq_content

Coduri python pentru diacritice:
ă = u'\u0103'
Ă = u'\u0102'
â = u'\u00E2'
Â = u'\u00C2'
î = u'\u00EE'
Î = u'\u00CE'
ş = u'\u015F'
Ş = u'\u015E'
ţ = u'\u0163'
Ţ = u'\u0162'
'''

import sys
import codecs
import logging

reload(sys)  
sys.setdefaultencoding('iso8859-2')

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', filename='/home/matei/Documents/Python/Diacritica/Diacritica.log', datefmt='%Y/%m/%d %I:%M:%S %p', level=logging.INFO)

reps = {u'\u0103':'a', u'\u0102':'A', u'\u00E2':'a', u'\u00C2':'A', u'\u00EE':'i', u'\u00CE':'I', u'\u015F':'s', u'\u015E':'S', u'\u0163':'t', u'\u0162':'T'}


# seteaza fisiere subtitrare IN
fileIn  = '/media/MoviesNSA310/incoming/Blade.Runner.2049.2017.1080p.BluRay.x264-SPARKS/Blade.Runner.2049.2017.1080p.BluRay.x264-SPARKS.Ro.srt'


# seteaza fisiere subtitrare OUT si noua limba in functie de prezenta/absenta limbi 'Ro'
if fileIn[len(fileIn)-6:len(fileIn)-4] in 'Ro':
  fileOut = ''.join([fileIn[:-6], 'Eo.srt'])
else:
  fileOut = ''.join([fileIn[:-4], '.Eo.srt'])


# functie replace in baza directorului cu diacritice
def replace_all(text, dic):
  for i, j in dic.iteritems():
    try:
      text = text.replace(i, j)
    except:
      logging.error ('Eroare la inlocuire!')
  return text


# deschide, memoreaza si inchide fisierul sursa
try:
  f = codecs.open(fileIn, 'r', 'iso8859-2')
  filedata = f.read()
  f.close()
except:
  logging.error ('Nu am putut deschide fisierul sursa: %s', fileIn)


# inlocuieste diacriticele
newdata = replace_all(filedata, reps)


# scrie fisierul nou
try:
  f = codecs.open(fileOut, 'w', 'iso8859-2')
  f.write(newdata)
  f.close()
except:
  logging.error ('Nu am putut salva fisierul generat: %s', fileOut)

logging.info('Succes! S-a generat fisierul: %s', fileOut)
print '\nSucces! S-a generat fisierul:', fileOut