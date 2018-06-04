import re
import json
import codecs
DBData = [] #данные из файла
tagname = [] #Имя в PLC
shortname = [] #Имя в JS
DBName = [] #Имя DB
SplitedDB = [] #Разбитая DB
typename = []
pref = '' # Префикс для структур
DBdictArr = []
Comment = []
with open ('D:\Rep\GDB#WarehouseConstant_DB.db', 'r', encoding = 'UTF-8') as fp:
    for line in fp:
        DBData.append(line)
fp.close #закрываем файл
DBName =  DBData[0].split() #название DB
p = re.compile('\d')
y = len (DBData)
for i in range(y):
    if i > 5:
        SplitedDB = DBData[i].split() #разрезаем строку
     
        if len(SplitedDB)>1:
           if SplitedDB[2] == 'Struct': #если тип Struct
            pref = SplitedDB[0] + '.'
        if SplitedDB[0] == 'END_STRUCT;':
            pref = ''     
        if SplitedDB[0] != 'END_DATA_BLOCK' and SplitedDB[0] != 'END_STRUCT;' and len(SplitedDB)>1 and SplitedDB[2] != 'Struct' and p.match(SplitedDB[2]) == None :
            fullTagName = DBName[1] + '.' + pref + SplitedDB[0]
            CommentText= ' '.join (SplitedDB[3:])
            typename.append(SplitedDB[2])
            tagname.append(fullTagName)
            Comment.append(CommentText)
            shortname.append(pref+SplitedDB[0])

for i in range(len(tagname)):
    DBdict = {'name': tagname[i], 'type': typename[i], 'comment' : Comment[i] }
    DBdictArr.append(DBdict)
with open ('D:\Rep\GDB#WarehouseConstant_DB_read.JSON', 'w', encoding = 'UTF-8')  as JSONforRead: #пишем в файл для чтения 
    
    JSONforRead.write(json.dumps (DBdictArr, ensure_ascii=False))
with open ('D:\Rep\GDB#WarehouseConstant_DB_read.JSON', 'r', encoding = 'UTF-8' )  as JSONforRead: #пишем в файл для чтения 
    for line in JSONforRead:
        print (line)