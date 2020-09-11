import socket
import struct

Host = '127.0.0.1'
Port = 6789#端口号
BufSize = 8196#最大字符值
FmtHead = '256sHL'	#L決定單個文件必須小於4G
relPath="NTCTTP/1.0 NOTIFY(CRLF)Content-Type:text/xml(CRLF)Content-Length:456(CRLF)(CRLF)"
pathfile='my-xml.xml'#发送文件名



sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockClient.connect((Host, Port))


pkgHead = relPath.encode('utf8')

sockClient.sendall(pkgHead)

with open(pathfile, mode='rb') as f:
    buf = f.read(1024)
    sockClient.sendall(buf)

sockClient.close()

    

