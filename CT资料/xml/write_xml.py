import xml.etree.ElementTree as ET
from xml.dom import minidom
import datetime
import pytz


def saveXML(root, filename, indent="\t", newl="\n", encoding="utf-8"):
    rawText = ET.tostring(root)
    dom = minidom.parseString(rawText)
    with open(filename, 'w') as f:
        dom.writexml(f, "", indent, newl, encoding)


def ctBarcodeMessage():#分拣线发送包裹数据
    root = ET.Element("Envelope")

    Header = ET.SubElement(root, 'Header')
    MessageName = ET.SubElement(Header, 'MessageName')
    MessageName.text = 'ctBarcodeMessage'
    MessageTime = ET.SubElement(Header, 'MessageTime')
    MessageTime.text = datetime.datetime.now(
        pytz.timezone('Asia/Shanghai')).isoformat()

    Body = ET.SubElement(root, 'Body')
    Barcode = ET.SubElement(Body, 'Barcode')
    Barcode.text = '123456789'
    BillNo = ET.SubElement(Body, 'BillNo')
    BillNo.text = 'c12345682'
    saveXML(root, "write/ctBarcodeMessage.xml")


def ctConclusionResult():#判图结果
    root = ET.Element("Envelope")

    Header = ET.SubElement(root, 'Header')
    MessageName = ET.SubElement(Header, 'MessageName')
    MessageName.text = 'ctBarcodeMessage'
    MessageTime = ET.SubElement(Header, 'MessageTime')
    MessageTime.text = datetime.datetime.now(
        pytz.timezone('Asia/Shanghai')).isoformat()

    Body = ET.SubElement(root, 'Body')
    Barcode = ET.SubElement(Body, 'Barcode')
    Barcode.text = '123456789'
    BillNo = ET.SubElement(Body, 'BillNo')
    BillNo.text = 'c12345682'
    PRN = ET.SubElement(Body, 'PRN')
    PRN.text = 'XT2080AD0120170427000036'
    UserId = ET.SubElement(Body, 'UserId')
    UserId.text = '0000001'
    Department = ET.SubElement(Body, 'Department')
    Department.text = '1'
    JudgeResult = ET.SubElement(Body, 'JudgeResult')
    JudgeResult.text = 'c'

    JudgeCategory = ET.SubElement(Body, 'JudgeCategory')
    JudgeCategory.text = '0'

    JudgeTime = ET.SubElement(Body, 'JudgeTime')
    JudgeTime.text = datetime.datetime.now(
        pytz.timezone('Asia/Shanghai')).isoformat()

    saveXML(root, "write/ctConclusionResult.xml")


def ctDeviceStatus():#ct状态改变信息
    root = ET.Element("Envelope")

    Header = ET.SubElement(root, 'Header')
    MessageName = ET.SubElement(Header, 'MessageName')
    MessageName.text = 'ctDeviceStatus'
    MessageTime = ET.SubElement(Header, 'MessageTime')
    MessageTime.text = datetime.datetime.now(
        pytz.timezone('Asia/Shanghai')).isoformat()

    Body = ET.SubElement(root, 'Body')
    Status = ET.SubElement(Body, 'Status')
    Status.text = '4'

    saveXML(root, "write/ctDeviceStatus.xml")


def ctHeartBeatRequest():
    root = ET.Element("Envelope")

    Header = ET.SubElement(root, 'Header')

    MessageName = ET.SubElement(Header, 'MessageName')
    MessageName.text = 'ctHeartBeatRequest'
    MessageTime = ET.SubElement(Header, 'MessageTime')
    MessageTime.text = datetime.datetime.now(
        pytz.timezone('Asia/Shanghai')).isoformat()

    Body = ET.SubElement(root, 'Body')

    Source = ET.SubElement(Body, 'Source')
    Source.text = 'ss'

    Target = ET.SubElement(Body, 'Target')
    Target.text = 'c12345682'

    saveXML(root, "write/ctHeartBeatRequest.xml")


def ctHeartBeatResponse():
    root = ET.Element("Envelope")

    Header = ET.SubElement(root, 'Header')

    MessageName = ET.SubElement(Header, 'MessageName')
    MessageName.text = 'ctHeartBeatResponse'
    MessageTime = ET.SubElement(Header, 'MessageTime')
    MessageTime.text = datetime.datetime.now(
        pytz.timezone('Asia/Shanghai')).isoformat()

    Body = ET.SubElement(root, 'Body')

    Source = ET.SubElement(Body, 'Source')
    Source.text = 'CT'

    Target = ET.SubElement(Body, 'Target')
    Target.text = 'SS'

    saveXML(root, "write/ctHeartBeatResponse.xml")


def ctImageMessage():
    root = ET.Element("Envelope")

    Header = ET.SubElement(root, 'Header')
    MessageName = ET.SubElement(Header, 'MessageName')
    MessageName.text = 'ctImageMessage'
    MessageTime = ET.SubElement(Header, 'MessageTime')
    MessageTime.text = datetime.datetime.now(
        pytz.timezone('Asia/Shanghai')).isoformat()

    Body = ET.SubElement(root, 'Body')
    PRN = ET.SubElement(Body, 'PRN')
    PRN.text = 'XT2080AD0120170427000036'

    Barcode = ET.SubElement(Body, 'Barcode')
    Barcode.text = '123456789'
    BillNo = ET.SubElement(Body, 'BillNo')
    BillNo.text = 'c12345682'

    Length = ET.SubElement(Body, 'Length')
    Length.text = '500'
    ForceSplit = ET.SubElement(Body, 'ForceSplit')  
    ForceSplit.text = '0'

    saveXML(root, "write/ctImageMessage.xml")


def ctSortingResult():
    root = ET.Element("Envelope")

    Header = ET.SubElement(root, 'Header')
    MessageName = ET.SubElement(Header, 'MessageName')
    MessageName.text = 'ctSortingResult'
    MessageTime = ET.SubElement(Header, 'MessageTime')
    MessageTime.text = datetime.datetime.now(
        pytz.timezone('Asia/Shanghai')).isoformat()

    Body = ET.SubElement(root, 'Body')

    Barcode = ET.SubElement(Body, 'Barcode')
    Barcode.text = '123456789'
    BillNo = ET.SubElement(Body, 'BillNo')
    BillNo.text = 'c12345682'

    Result = ET.SubElement(Body, 'Result')
    Result.text = '1'
    saveXML(root, "write/ctSortingResult.xml")

'''
ctBarcodeMessage.xml（分拣线向包ct发的包裹信息）,
ctConclusionResult.xml,（判图结果）
ctDeviceStatus.xml,（ct状态改变信息）
ctHeartBeatRequest.xml（分拣线向ct发的心跳信息）,
ctHeartBeatResponse.xml（ct向返回的心跳信息）
ctImageMessage.xml（ct向分拣线发的图像信息）
ctSortingResult.xml（分拣线向ct发的分拣结果信息）
'''