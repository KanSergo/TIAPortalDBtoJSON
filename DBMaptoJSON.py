import re
import json
import codecs
DBData = [] #данные из файла
UDTData = [] #тип данных
tagname = [] #Имя в PLC
shortname = [] #Имя в JS
DBName = [] #Имя DB
SplitedDB = [] #Разбитая DB
typename = []
pref = '' # Префикс для структур
DBdictArr = []
UDTTypes1 = []
UDTType = []
#открываем файл DB
with open ('D:\Rep\GDB#TRACK_MAP.db', 'r', encoding = 'UTF-8') as fp:
    for line in fp:
        DBData.append(line)
fp.close #закрываем файл
DBName =  DBData[0].split() #название DB
p = re.compile('\d+')
y = len (DBData)
for i in range(y):
    if re.search("Array", DBData[i]) != None:   #Если нашли TrackData в строке
        ArrayStr = DBData[i].split() #разбиваем строку с массивом
        First = str(ArrayStr[0])  #Определяем имя массива
        print (First)
        QtyInStr = str(ArrayStr[2])
        Qty = list(map(int, re.findall(r'\d+', QtyInStr))) #определяем длину массива
        print(Qty)
        UDT = str(ArrayStr[4])
        ArrDict = {'name': First, 'Qty': Qty, 'UDTName': UDT, 'Types': UDTTypes1}
        print(ArrDict)
 
#открываем файл с типом данных
with open ('D:\Rep\TrackData.udt', 'r', encoding = 'UTF-8') as fp:
    for line in fp:
        UDTData.append(line)
fp.close #закрываем файл
#TypeFromUDT = [UDTData[0].split()][0][1]
#TypeFromDB =  (UDTType[0].split(';'))

print (UDTData)




for i in range(len(tagname)):
    DBdict = {'name': tagname[i], 'type': typename[i], 'comment' : UDtType[i] }
    DBdictArr.append(DBdict)
with open ('D:\Rep\GDB#TRACK_MAP_read.JSON', 'w', encoding = 'UTF-8')  as JSONforRead: #пишем в файл для чтения 
   
    JSONforRead.write(json.dumps (DBdictArr, ensure_ascii=False))
with open ('D:\Rep\GDB#TRACK_MAP_read.JSON', 'r', encoding = 'UTF-8' )  as JSONforRead: #пишем в файл для чтения 
    for line in JSONforRead:
        print (line)