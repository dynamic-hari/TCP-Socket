import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


host = '127.0.0.1'
port = 9999

s.connect((host, port))
op=0

def modify_file(filename):
    file = open(filename+".txt", "r")
    output=[]
    for line in file:
        if not "1" in line:
            output.append(line)
    file.close()
    file = open(filename+".txt", 'w')
    file.writelines(output)
    file.close
while True:
	c1="Client 2"
    s.send(c1.encode('ascii'))
    op=input("Select the option\n1.Receive\n2.Send\n3.Exit\n")
    s.send(op.encode('ascii'))
    if op==str(1):
        count=1
        list1 = s.recv(1024).decode('ascii')
        list1 = eval(list1)
        print(*list1,sep="\n")
        filename = input("Enter the File name you want :\n")
        s.send(filename.encode('ascii'))
        data = s.recv(1024).decode('ascii')
        data1 = data.replace("\n", "")
        file1 = open(filename+".txt", 'w')
        file1.write(data1)
        file1.close()
        print(data)
    elif op==str(2):
        fname=input("Enter the file name you want to send:")
        op1=input("Want to modify  the file\n1.Yes\n2.No\n")
        if op1==str(1):
            modify_file(fname)
            myfile = open(fname+".txt", "rb")
            s.send(myfile.read())
            print("Sent modified")
        elif op1==str(2):
            myfile1 = open(fname+".txt", "rb")
            s.send(myfile1.read())
            print("Sent not modified")
    elif op == str(3):
        break
        s.close()
