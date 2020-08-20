import xml.etree.ElementTree as ET

archivo_xml = ET.parse('profesores.xml')

raiz = archivo_xml.getroot()

print(raiz)
print()

for i in raiz:
    print(i)
    for j in i:
        print(j)
        print(j.text)
    print()