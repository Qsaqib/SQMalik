import xml.etree.ElementTree as ET
with open("Bin Pari L2_rev1.xml", "r") as f:
    data=f.read()
# This is the parent (root) tag
# onto which other tags would be
# created
import xml.etree.ElementTree as ET
tree = ET.parse("C:\\Users\\139\\Desktop\\DSA Python\\Bin Pari L2_rev1.xml")
root = tree.getroot()
#print(root)
rootTag = root.tag[:-7]
#print(root.attrib)
#print(rootTag)

# XML Functions
'''
for child in root:
	print(child.tag,child.attrib)
'''
print([elem.tag for elem in root.iter()][0:100])

surfaces = root.find(rootTag+"Alignments")
#print(surfaces)
SurfName='Bin Pari L2'
if not(surfaces):
	print('Error! This file does not contain surfaces')
surfList = []
surfListResult = []


SurfName="Bin Pari L2"
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
#print(surfList)


xmlUnits = root.find(".//"+rootTag+"Units")
lUnits = xmlUnits.find("*").attrib.get("linearUnit")
#print(xmlUnits)
Pnts = []
Faces = []

for p in surf.findall(".//"+rootTag+"Feature"):
	Pnts.append(p.text)
for f in surf.findall(".//"+rootTag+"End"):
	Faces.append(f.text)


#print(Pnts)
#print(Faces)
#id = surf.findall(".//"+rootTag+"P")[0].attrib.get("id")
'''
XYZPnts = []
if lUnits == 'meter':
	for i in range(0, len(Pnts)):
		XYZPnts.append((float(Pnts[i].rsplit()[0]),float(Pnts[i].rsplit()[1]),float(Pnts[i].rsplit()[2])))
else:
	for i in range(0, len(Pnts)):
		XYZPnts.append(float(Pnts[i].rsplit()[0]),float(Pnts[i].rsplit()[1]),float(Pnts[i].rsplit()[2]))
final=[]


print(XYZPnts)
'''