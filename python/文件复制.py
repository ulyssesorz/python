from os.path import exists

fromfile='sysu.txt'
tofile='scut.txt'

line=input('input something')
infile=open(fromfile,'w')
infile.write(line)           #写入内容至fromfile,

infile=open(fromfile)         #读取fromfile的内容，注意不能用w
data=infile.read()

print('',{exists(tofile)})   #判断文件是否存在

infile=open(tofile,'w')
infile.write(data)       #把之前读取的内容写入tofile中

infile.close()             #infile作为中间交换者

