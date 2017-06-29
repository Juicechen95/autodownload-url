# -*- coding: utf-8 -*-  
""" 
Created on Tue Apr 07 15:28:53 2015 
 
@author: Chenriwei 
"""  
  
import os  
import re  
import time  
import urllib  
  
def get_all_iamge(filename):  
    fid=open(filename)  
    lines=fid.readlines()
    #print(lines)
    for line in lines:
       # print(line+'\n')
        line_split=line.split('\t')
        
        
        name=line_split[0]  
        image_id=line_split[1]  
        #face_id=line_split[2]  
        box=line_split[3]  
        image_url=line_split[2]  
       # print image_url+'\n'  
        #print box+'\n'  
        if False == os.path.exists(name):  
            os.mkdir(name)  
          
        try:  
        # urlopen=urllib.URLopener()
         proxies={'http':'http://127.0.0.1:8787'}
         filehandle = urllib.urlopen(image_url,proxies=proxies)
         data=filehandle.read()
        
         #urlopen=urllib.URLopener()  
         #fp = urlopen.open(image_url)  
         #data = fp.read()  
         #fp.close()  
         file=open(name+'/'+image_id+'.jpg','w+b')  
         file.write(data)  
         print "SUCCESS:  "+ name+'\t'+image_id 
         file.close()  
        except IOError:  
         print "FAIL:    "+ name+'\t'+image_id 
  
if __name__ == "__main__":  
    #get_all_iamge('dev_urls.txt')
    get_all_iamge('1.txt')
    
