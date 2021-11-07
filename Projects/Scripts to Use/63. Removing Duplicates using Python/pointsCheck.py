import xml.etree.ElementTree as ET
with open("RS5O_E_CAR_W04_M3_01_PRO.xml", "r") as f:
    data=f.read()
# This is the parent (root) tag
# onto which other tags would be
# created
import xml.etree.ElementTree as ET
tree = ET.parse("C:\\Users\\139\\Desktop\\DSA Python\\RS5O_E_CAR_W04_M3_01_PRO.xml")
root = tree.getroot()
rootTag = root.tag[:-7]
surfaces = root.find(rootTag+"Surfaces")
SurfName="W04"
surfList = []
surfListResult = []
for s in surfaces.findall("*"):
	surfList.append(s.attrib.get('name'))
	if s.attrib.get('name') == SurfName:
		surfListResult.append(s)
try:
	surf = surfListResult[0]
except:
    pass

xmlUnits = root.find(".//"+rootTag+"Units")
lUnits = xmlUnits.find("*").attrib.get("linearUnit")

Pnts = []
Faces = []

for p in surf.findall(".//"+rootTag+"P"):
	Pnts.append(p.text)
for f in surf.findall(".//"+rootTag+"F"):
	Faces.append(f.text)
id = surf.findall(".//"+rootTag+"P")[0].attrib.get("id")

XYZPnts = []
if lUnits == 'meter':
	for i in range(0, len(Pnts)):
		XYZPnts.append((float(Pnts[i].rsplit()[0]),float(Pnts[i].rsplit()[1]),float(Pnts[i].rsplit()[2])))
else:
	for i in range(0, len(Pnts)):
		XYZPnts.append(float(Pnts[i].rsplit()[0]),float(Pnts[i].rsplit()[1]),float(Pnts[i].rsplit()[2]))
final=[]



for i in XYZPnts:
	final.append([round(i[0],2),round(i[1],2),round(i[2],2)])

print(len(final))
X=[]
Y=[]
Z=[]
lst1=[]
for i in final:
    X.append(i[0])
    Y.append(i[1])
    Z.append(i[2])
    lst1.append([X,Y,Z])
print(len(X))    
sub=[]
out=[]    

def f5(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for ind, item in enumerate(seq):
       #s2=seq2[ind]
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(ind)
   return result

zipped=zip(X,Y)
#zipped2=zip(X,Y,Z)
out=f5(zipped)
#print(out)

'''
import pandas as pd

df=pd.DataFrame(out,columns=['x','y','z'])
writer=pd.ExcelWriter('W04.xlsx')
df.to_excel(writer)
writer.save()
'''