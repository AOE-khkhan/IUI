from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import unidecode
def hasNumbers(inputString):
    l = 0
    return any(char.isdigit() for char in inputString)

def is_ascii(s):
    try:
        s.decode('ascii')
        return True
    except UnicodeDecodeError:
        return False

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text
l1 = []
l2 = []
for i in range(626,627):
    m = convert('AI4.pdf', pages=[i])
    m = m.split('\n\n')
    for mm in m:
        if len(mm)<7 or hasNumbers(mm)==False:
            continue
        else:
            #print mm
            
            if '\n' in mm:
              mm = mm.split('\n')
              #clprint mm
              for mmm in mm:
                if ',' in mmm:
                  #print mmm
                  mmm = mmm.split(',')
                  if len(mmm)>1 and hasNumbers(mmm[1]):
                    temp = mmm[0].split(' ')
                    for fack in range(1,len(mmm)):
                      mmm[fack] = unicode(mmm[fack], "utf-8")
                      mmm[fack] = unidecode.unidecode(mmm[fack])
                      if '-' in mmm[fack]:
                        print "Hi"
                        baba = mmm[fack].split('-')
                        l1.append(temp)
                        l2.append(baba[0])
                        print temp
                        print baba[0]
                        l1.append(temp)
                        l2.append(baba[1])
                        print temp
                        print baba[1]
                      else:
                        l1.append(temp)
                        l2.append(mmm[fack])
                        print temp
                        print mmm[fack]

            else:
              print mm
              mmm = mm.split(',')
              if len(mmm)>1 and hasNumbers(mmm[1]):
                temp = mmm[0].split(' ')
                for fack in range(1,len(mmm)):
                  mmm[fack] = unicode(mmm[fack], "utf-8")
                  mmm[fack] = unidecode.unidecode(mmm[fack])
                  if '-' in mmm[fack]:
                    #print "Hi"
                    baba = mmm[fack].split('-')
                    l1.append(temp)
                    l2.append(baba[0])
                    print temp
                    print baba[0]
                    l1.append(temp)
                    l2.append(baba[1])
                    print temp
                    print baba[1]
                  else:
                    l1.append(temp)
                    l2.append(mmm[fack])
                    print temp
                    print mmm[fack]

            #print mm
            #mm = mm.split(' ')
            #for mmm in range(len(mm)):
            #    mm[mmm] = unicode(mm[mmm], "utf-8")
            #    mm[mmm] = unidecode.unidecode(mm[mmm])

            #s = []
            #for t in mm:
             #   if 'pr' in t or 'ex' in t:
             #       continue
             #   else:
             #       s.append(t)
           # s = " ".join(s)

            #s = s.split('\n')
            #for sss in s:
         #   sss = s.split(',')
          #  te = []
         #   for ttt in sss:
         #     if len(ttt)>=2:
          #      te.append(ttt)
         #   sss = te
                
         #   if len(sss)>=2:
          #    if hasNumbers(sss[1])==True:
           #     fish = sss[0].split(' ')
            #    fish2 = []
           #     for fff in fish:
            #      if len(fff)>1:
             #       fish2.append(fff)
            #    fish = fish2
             #   for fack in range(1,len(sss)):
              #    l1.append(fish)
              #    l2.append(sss[fack].strip())
               #   print fish
               #   print sss[fack].strip()

                  #print sss
                #    if hasNumbers(sss[1])==True:



                  #      if len(sss[1].strip())<=7:
                            #print sss
                   #         temp = sss[0].split(' ')
                            #l1.append(temp)
                    #        if len(sss[1].strip())<=4:
                     #           l1.append(temp)
                      #          l2.append(sss[1])
                       #         print temp
                        #        print sss[1]
                        #    elif len(sss[1].strip())==7 and sss[1][3].strip()=='-':
                         #       l1.append(temp)
                          #      print l1.append(temp)
                          #      l2.append(sss[1][:3])
                          #      print l2.append(sss[1][:3])
                          #      l1.append(temp)
                          #      print l1.append(temp)
                          #      l2.append(sss[1][4:7])
                          #      print l2.append(sss[1][4:7])


            #print s
            #if len(s)==2:
                #print s
            #    if hasNumbers(s[1])==True:
             #       if len(s[1].strip())<=4:
              #          s[0] = s[0].split(' ')
               #         temp = []
                #        for ff in s[0]:
                 #           if is_ascii(ff):
                  #              temp.append(ff)


                   #     print temp
                    #    print s[1]
                     #   if len(temp)>0:
                      #      l1.append(temp)
                       #     l2.append(s[1])





        #if '\n' in mm and is_ascii(mm)==True:
            #print "True"
        #    mm = mm.split('\n')
        #    for mmm in mm:

         #       if hasNumbers(mmm):
          #          temp = []

           #         l = mmm.split(' ')
            #        for ff in l:
             #           if ff[-1:]==',':
              #              ff = ff[:-1]
               #         if len(ff)>1:
                #            temp.append(ff.lower())
                #    money = []    
                 #   for tt in temp:
                  #      if hasNumbers(tt)==False:
                   #         money.append(tt)
               #     for tt in temp:
                #        if hasNumbers(tt)==True:
                 #           l1.append(money)
                  #          l2.append(tt)
                    #print temp

      #  elif hasNumbers(mm) and is_ascii(mm)==True:
       #     temp = []
        #    l = mm.split(' ')
         #   for ff in l:
          #      if ff[-1:]==',' or ff[-1:]=='.':
           #         ff = ff[:-1]
            #    if len(ff)>1:
        #            temp.append(ff.lower())
         #   money = []    
          #  for tt in temp:
           #     if hasNumbers(tt)==False:
            #        money.append(tt)
          #  for tt in temp:
           #     if hasNumbers(tt)==True:
            #        l1.append(money)
             #       l2.append(tt)
            #print temp
            #print mm
print l1
print len(l1)
print l2
print len(l2)