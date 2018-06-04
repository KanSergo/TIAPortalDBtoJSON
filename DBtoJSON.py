import re
DBData = [] #данные из файла
tagname = [] #Имя в PLC
shortname = [] #Имя в JS
DBName = [] #Имя DB
SplitedDB = [] #Разбитая DB
pref = '' # Префикс для структур
with open ('D:\Rep\GDB#WarehouseConstant_DB.db', 'r', encoding="utf-8") as fp:
    for line in fp:
        DBData.append(line)
fp.close #закрываем файл
DBName =  DBData[0].split() #название DB

y = len (DBData)
for i in range(y):
    if i > 5:
        SplitedDB = DBData[i].split() #разрезаем строку
     
        if len(SplitedDB)>1:
           if SplitedDB[2] == 'Struct': #если тип Struct
            pref = SplitedDB[0] + '.'
        if SplitedDB[0] == 'END_STRUCT;':
            pref = ''     
        if SplitedDB[0] != 'END_DATA_BLOCK' and SplitedDB[0] != 'END_STRUCT;' and len(SplitedDB)>1 and SplitedDB[2] != 'Struct':
            fullTagName = DBName[1] + '.' + pref + SplitedDB[0]
            tagname.append(fullTagName)
            shortname.append(pref+SplitedDB[0])
with open ('D:\Rep\GDB#WarehouseConstant_DB_write.JSON', 'w', encoding="utf-8") as JSONforWrite: #пишем в файл для записи
    for line in tagname:
        JSONforWrite.write ('!-- AWP_In_Variable Name=\'' + line + '\' -->' + '\n' )
zip(shortname,tagname)
with open ('D:\Rep\GDB#WarehouseConstant_DB_read.JSON', 'w', encoding="utf-8") as JSONforRead: #пишем в файл для чтения    
    for i in range (len(tagname)):
        JSONforRead.write('\"'+ str(shortname[i]) + '\": \":=' + str(tagname[i]) + ':\"\n')
