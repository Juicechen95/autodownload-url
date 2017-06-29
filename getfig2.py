#-*- coding: utf-8 -*-  
""" 
Created on Tue Apr 07 20:19:38 2015 
 
@author: Chenriwei 
"""  
  
import threading  
import time  
import urllib
import os
  
  
def download_and_save(url,savename,name,image_id):  
        try:  
         #urlopen=urllib.URLopener()  
        # fp = urlopen.open(url)  
        # data = fp.read()  
        # fp.close()  
         proxies={'http':'http://127.0.0.1:8787'}
         filehandle = urllib.urlopen(url,proxies=proxies)
         data=filehandle.read()
         fid=open(savename,'w+b')  
         fid.write(data)  
         print "SUCCESS:  "+ name+'\t'+image_id 
         fid.close()  
        except IOError:  
         print "FAIL:    "+ name+'\t'+image_id  
  
  
def get_all_iamge(filename):  
    fid=open(filename)  
    lines=fid.readlines()  
    for line in lines:  
        line_split=line.split('\t')  
        name=line_split[0]  
        image_id=line_split[1]  
        #face_id=line_split[2]  
        box=line_split[3]  
        image_url=line_split[2]  
        if False == os.path.exists(name):  
            os.mkdir(name)  
        savefile=name+'/'+image_id+'.jpg'    
        #最多1000个线程，  
        while True:  
                if(len(threading.enumerate()) < 100):  
                    break  
                  
        t = threading.Thread(target=download_and_save,args=(image_url,savefile,name,image_id))  
        t.start()  
  
if __name__ == "__main__":  
    get_all_iamge('dev_urls.txt')
    #get_all_iamge('1.txt')
