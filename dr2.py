import mechanize
br = mechanize.Browser()

def clearPage(s) :
    new=""
    start = s.find(tableclrstart)
    end = s.find(tableclrend, 1900) + len(tableclrend)
    old=s[start : end]
    return s.replace(old,new)

def writeFile(s, e="") :
    f = open('total' + str(e) + '.html' ,'w+')
    f.write(s)
    files.append(s)
    f.close()

# vars
hebmeta = "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1255\">"
appendstring = "<td width=100% height=\"5\">"
trailerstr = "<p align=\"center\"><font SIZE=\"2\" face=\"Arial\" color=\"#005BB7\">"
filestr=[]
files=[]
urltmplt = "http://www.old.health.gov.il/oskimbbriut/rufim/DoctorSearch.asp?p=XXX&Yshuv&FirstName&LastName&RegNum"
tableclrstart="align=\"right\" bgcolor=\"#F3F7F8\" colspan=\"8\" width=100%>"
tableclrend= "<td align=\"center\" width=\"20\" bgcolor=\"#369CCD\"><font color=\"#FFFFFF\" face=\"Arial\" size=\"2\"><b>&nbsp;</b></font></td>"
e=1

for i in xrange(1, 1849):  # 1849
    index = str(i)
    print 'index = ' + index
    url = urltmplt.replace('XXX', index)
    r = br.open(url)
    html = r.read()
    r.close()
    rmheader = html.split(appendstring)
    rmtrailer = rmheader[2].split(trailerstr)
    filestr.append(rmtrailer[0])
    if (i % 400 == 0) :
        s = (hebmeta + '\n' + ''.join(filestr))
        filestr=[]
        s = clearPage(s)
        writeFile(s, e)
        e+=1

s = (hebmeta + '\n' + ''.join(filestr))
s = clearPage(s)
writeFile(s, e)


