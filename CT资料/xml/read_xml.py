import xml.etree.ElementTree as ET

# 获取 XML 文档对象 ElementTree
tree = ET.parse('ctBarcodeMessage.xml')
root = tree.getroot()
for child in root:
    for children in child:
        print(child.tag,':',children.tag, ":", children.text)

