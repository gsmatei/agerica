import sys
import codecs
import logging

# functie deschide, memoreaza si inchide fisierul sursa
def read_file(fisier):
  try:
    f = codecs.open(fisier, 'r', 'iso8859-2')
    fileData = f.read()
    f.close()
    return fileData
  except:
    logging.error ('Nu am putut deschide fisierul sursa: {0}'.format(fisier))
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

# functie replace in baza dictionarului cu diacritice
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
    logging.error ('Nu am putut salva fisierul generat: {0}'.format(fisier))
    raise