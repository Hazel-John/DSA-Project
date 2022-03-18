import re
count=0
class University_Details:
    def __init__(self):
        global count

    def initializeHash(self):
        ApplicationRecords=[[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]
        self.count=0

    def hashID(self,name):
        name=name.lower()
        value=0
        for c in name:
            value+=ord(c)
        value%=26
        return value


    def inputAppDetails(self,ApplicationRecords,name,phone,country,program,status):
        global count
        count+=1
        hashValue= self.hashID(name)
        key=name+phone+country
        entries=[name,phone,country,program,status]
        if ApplicationRecords[hashValue]==[]:
            ApplicationRecords[hashValue]=[list((key,entries))]
        else:
            ApplicationRecords[hashValue].append(list((key,entries)))
            
        


    def destroyHash(ApplicationRecords):
        ApplicationRecords=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    def updateAppDetails(self,ApplicationRecords,name, phone, country, program, status):
        update_hash=self.hashID(name)
        key=name+str(phone)+country
        flag=0
        entries=[name,phone,country,program,status]
        if len(ApplicationRecords[update_hash])==0:
                print('No Records Found')
        elif len(ApplicationRecords[update_hash])==1:
            print(ApplicationRecords[update_hash][0][1][4])
            if ApplicationRecords[update_hash][0][1][4] != status:
                ApplicationRecords[update_hash]=[list((key,entries))]
                flag=1
        else:
            index=0
            for hash_value_entries in ApplicationRecords[update_hash]:
                if hash_value_entries[0]==key and hash_value_entries[1][4] !=status:
                    ApplicationRecords[update_hash][index]=list((key,entries))
                    flag=1
                index+=1
        if flag==1:
            print('Updated details of '+name+'. Application Status has been changed.')
    


    def appStatus(self,ApplicationRecords):
        applied_count,rejected_count,approved_count=0,0,0
        for record in ApplicationRecords:
            if record != []:
                for record_entries in record:
                    if record_entries[1][4]=='Applied':applied_count+=1
                    elif record_entries[1][4]=='Rejected':rejected_count+=1
                    elif record_entries[1][4]=='Approved':approved_count+=1
                    else :print("This situatiion should not come up, considering input text is error-free")
        print("---------- Application Status ----------")
        print("Applied: "+str(applied_count))
        print("Rejected: "+str(rejected_count))
        print("Approved: "+str(approved_count))
        print("----------------------------------------")

    def memRef(self,ApplicationRecords,Program):
        for record in ApplicationRecords:
            if record != []:
                for record_entries in record:
                    if record_entries[1][3]==Program:
                        print(record_entries[1][0]+" / "+record_entries[1][1]+" / "+record_entries[1][2]+" / "+record_entries[1][3]+" / "+record_entries[1][4])


input_content_list=[]
ApplicationRecords=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

with open('inputPS2.txt') as input_file:
    for line in input_file:
        line=line.replace('\n','')
        input_content_list.append(line)

University_pointer=University_Details()
for record in input_content_list:
    records = re.split(r'[/]\s*',record)
    University_pointer.inputAppDetails(ApplicationRecords,records[0][:-1],records[1][:-1],records[2][:-1],records[3][:-1],records[4])

print(ApplicationRecords)
print("Successfully inserted "+str(count)+" applications into the system.")

University_pointer.updateAppDetails(ApplicationRecords,'bbb',9953152234,'Nepal','Electronics','Rejected')
print(ApplicationRecords)
University_pointer.appStatus(ApplicationRecords)
University_pointer.memRef(ApplicationRecords,'Computer Science')