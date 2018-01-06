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


# functie deschide, memoreaza si inchide fisierul sursa
def read_file(fisier):
  try:
    f = codecs.open(fisier, 'r', 'iso8859-2')
    fileData = f.read()
    f.close()
    return fileData
  except:
    logging.error ('Nu am putut deschide fisierul sursa: %s', fisier)
    raise

# functie seteaza fisiere subtitrare OUT si noua limba in functie de prezenta/absenta limbi 'Ro'
def set_lang(fisier):
  try:
    if fisier[len(fisier)-6:len(fisier)-4] in 'Ro':
      fileOut = ''.join([fisier[:-6], 'Eo.srt'])
    else:
      fileOut = ''.join([fisier[:-4], '.Eo.srt'])
    return fileOut
  except:
    logging.error ('Nu am putut seta nume fisier nou')
    raise

# functie replace in baza directorului cu diacritice
def replace_all(text, dic):
  for i, j in dic.iteritems():
    try:
      text = text.replace(i, j)
      return text
    except:
      logging.error ('Eroare la inlocuire!')
      raise

# functie scrie fisierul nou
def write_file(fisier, data):
  try:
    f = codecs.open(fisier, 'w', 'iso8859-2')
    f.write(data)
    f.close()
  except:
    logging.error ('Nu am putut salva fisierul generat: %s', fisier)
    raise

fileOut = set_lang(fileIn)
fileData = read_file(fileIn)
newData = replace_all(fileData, reps)
write_file(fileOut, newData)


logging.info('Succes! S-a generat fisierul: %s', fileOut)
print '\nSucces! S-a generat fisierul:', fileOut