import json
import os

path=''


def create_directory(self,dir_path=None):
    '''set directory path is not provided by user'''
    if dir_path==None:
        dir_path="C:\\"
    
    '''folder name'''
    directory='freshworks_data'

    '''final path of path'''
    global path
    path=dir_path+directory

    '''create directory and check if there is a duplicate file or not'''
    try:
        os.mkdir(path)
        print("Directory '% s' created" % path) 
        
        '''create datastore'''
        temp={}
        path=path+'\\master.json'
        with open(path,'w') as fp:
            json.dump(temp,fp)

    except OSError as error:  
        print(error)     
    

def add_data(self,key1,value1):
    '''check current key is presnt in datastore or not'''
    with open(path,'r') as fp:
        data=json.load(fp)
    if key1 in data:
        print("key already exist, try with another key")
    else:
        '''check size of json file'''
        size=os.path.getsize(path)
        if size<=1073741824:  
            '''save data in datastore'''  
            with open(path,'r') as fp:
                data=json.load(fp)
            data[key1]=value1
            '''check if we add new data, it will not cross the data limit'''
            data2={}
            data[key1]=value1
            with open('datatest.json','w') as fp:
                json.dump(data2,fp)
            size2=os.path.getsize('datatest.json')
            '''check size of data never exceed after adding new data'''
            if size+size2<1073741824:
                os.remove("datatest.json")
                with open(path,'w') as fp:
                    json.dump(data,fp)
            else:
                print("data entry unsuccessful!\n New entry is exceeding data restriction.")   
        else:
            print("size of file is exceeding 1 GB")


def read_data(self,key1):
    '''load json file'''
    with open(path,'r') as fp:
        data=json.load(fp)
    if key1 in data:
        print(data[key1])
    else:
        print("key doesn't exist")
    

def delete_data(self,key1):
    with open(path,'r') as fp:
        data=json.load(fp)
    if key1 in data:
        data.pop('hours', None)
        with open(path, 'w') as data_file:
            json.dump(data, data_file)  
    else:
        print("key doesn't exist")

