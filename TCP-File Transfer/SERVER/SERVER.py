import socket
import os

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9999

s.bind((host,port))
print("server Started")

s.listen(5)

os.chdir(r"D:\HARI HARAN\Education\Sem 4\CN\SERVER")
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
type1 = ".txt"
clist=[]
conn= [[0 for x in range(2)] for y in range(4)]

def check_modify(filename):
    f1=open(filename+".txt","r")
    f2=open(filename+"1.txt","r")
    count=0
    f=0
    for line1 in f1:
        f+=1
        for line2 in f2:
            if line1==line2:
                count+=1
            break
    if count == f:
        print("Received file is Same as sent!!!")
    else:
        print("Received file is Modified!!!")
    f1.close()
    f2.close()

while True:
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    cn=c.recv(1024).decode('ascii')
    dummy=any(cn in sublist for sublist in clist)
    print(dummy)
    if dummy is False:
        clist.append([cn])
    count=0
    while True:
        op = c.recv(1024).decode('ascii')
        print(op)
        if op == str(1):
            print("Start of 1")
            res = [i for i in files if type1 in i]
            res=str(res)
            c.send(res.encode('ascii'))
            filename = ''
            data = c.recv(1024).decode('ascii')
            filename += data
            print("from connected user: " + filename)
            myfile = open(filename+".txt", "rb")
            c.send(myfile.read())
            print("End of 1\n")
            count=count+1
            print("Count in 1",count)
        elif op == str(2):
            print("Start of 2")
            d = c.recv(1024).decode('ascii')
            d1 = d.replace("\n", "")
            file1 = open(filename+'1.txt', 'w')
            file1.write(d1)
            file1.close()
            print(d)
            print("End of 2")
            count=count+1
            print("Count in 2",count)
            check_modify(filename)
        elif op == str(3):
            break
    c.close()
    row=len(clist)
    while True:
        pos=0
        for i in range(row):
            c=clist[i][0]
            if c==cn:
                pos=i
                break
        break
    print("No. of interactions made:")
    clist[pos].extend([count])
    print(*clist,sep="\n")
    print("\n")
    conn[pos][0]=cn
    val=conn[pos][1]
    val=val+1
    conn[pos][1]=val
    print("No. of Times clients Connected:")
    for i in range(len(conn)):
        for j in range(2):
            if conn[i][j] != 0:
                print(conn[i][j])
    print("\n")
