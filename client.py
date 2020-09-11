import socket
import struct
import xml.etree.ElementTree as ET
from xml.dom import minidom
import datetime
import pytz
from operator import methodcaller
import time
import threading
import os
from apscheduler.schedulers.blocking import BlockingScheduler

class xml_write:
    # ctBarcodeMessage.xml（分拣线向包ct发的包裹信息）
    # ctConclusionResult.xml,（判图结果）
    # ctDeviceStatus.xml,（ct状态改变信息)
    # ctHeartBeatRequest.xml（分拣线向ct发的心跳信息）
    # ctHeartBeatResponse.xml（ct向返回的心跳信息）
    # ctImageMessage.xml（ct向分拣线发的图像信息）
    # ctSortingResult.xml（分拣线向ct发的分拣结果信息)
    def saveXML(self, root, filename, indent="\t", newl="\n", encoding="utf-8"):
        rawText = ET.tostring(root)
        dom = minidom.parseString(rawText)
        with open(filename, 'w') as f:
            dom.writexml(f, "", indent, newl, encoding)

    def ctBarcodeMessage(self):  # 分拣线发送包裹数据
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
        self.saveXML(root, "ctBarcodeMessage.xml")

    def ctConclusionResult(self):  # 判图结果
        root = ET.Element("Envelope")

        Header = ET.SubElement(root, 'Header')
        MessageName = ET.SubElement(Header, 'MessageName')
        MessageName.text = 'ctConclusionResult'
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

        self.saveXML(root, "ctConclusionResult.xml")

    def ctDeviceStatus(self):  # ct状态改变信息
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

        self.saveXML(root, "ctDeviceStatus.xml")

    def ctHeartBeatRequest(self):
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

        self.saveXML(root, "ctHeartBeatRequest.xml")

    def ctHeartBeatResponse(self):
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

        self.saveXML(root, "ctHeartBeatResponse.xml")

    def ctImageMessage(self):
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

        self.saveXML(root, "ctImageMessage.xml")

    def ctSortingResult(self):
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
        self.saveXML(root, "ctSortingResult.xml")

class socket_Communication():
    def __init__(self,Host,Port):
        self.Host=Host
        self.Port=Port
        # Host = '127.0.0.1'
        # Port = 6789  # 端口号
        self.sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockClient.connect((Host, Port))

    def send(self,pathfile,Packet_header = "NTCTTP/1.0 NOTIFY(CRLF)Content-Type:text/xml(CRLF)Content-Length:456(CRLF)(CRLF)"):  
        # 发送通信传输信息函数,Packet_header是固定报可以不进行定义，pathfile是要传输给服务器的文件名（不包后缀名：.xml），
        # 该函数主要作用是应用xml_write类生成对应的.xml文件在通过文件读取进行传输
        myxml_write = xml_write()
        methodcaller(str(pathfile))(myxml_write)
        pathfile = str(pathfile + '.xml')
        pkgHead = Packet_header.encode('utf8')
        self.sockClient.sendall(pkgHead)
        with open(pathfile, mode='rb') as f:
            buf = f.read(1024)
            self.sockClient.sendall(buf)
    def accept(self,read_path_name):
        #接受并读取通信文档的主要信息
        xml_dist_Header = {}
        xml_dist_Body = {}

        read_path_name=str(read_path_name + '.xml')#自己的设置写入文件和读取的文件名
        res = self.sockClient.recv(80)  # 接受报文头，报文头的固定字节（80）
        cmds = res.decode('utf-8')#报文头有进行加密所以要进行解码
        print(cmds)
        with open(read_path_name, 'wb') as f:
            line = self.sockClient.recv(1024)
            f.write(line)
        print ('接受完成')
        time.sleep(1)
        tree = ET.parse(read_path_name)# 把传输后保存的文件进行数据的读取，并返回 头部Header，信息主体部分Body  以字典的方式进行返回
        root = tree.getroot()
        for child in root:
            for children in child:
                if child.tag == 'Header':
                    xml_dist_Header[children.tag] = children.text
                if child.tag == 'Body':
                    xml_dist_Body[children.tag] = children.text
        print (xml_dist_Header)
        print (xml_dist_Body)
        print('接收并读取成功')

        return xml_dist_Header,xml_dist_Body

    def close(self):
        self.sockClient.close()
 


def heart_packet(my_socket):
    my_socket.send('ctHeartBeatRequest')
    my_socket.accept('heart_packet_1')
    print ('收到包1')
    my_socket.accept('heart_packet_2')
    print ('收到包2')

    


if __name__ == "__main__":
    my_socket = socket_Communication('127.0.0.1',6789)
    scheduler = BlockingScheduler()
    scheduler.add_job(heart_packet, 'interval', seconds=10,args=[my_socket])
    scheduler.start()




