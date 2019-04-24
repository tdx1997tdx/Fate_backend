# Fate_backend
##姓名搜索：  
前端给后端json文件格式：  
{  
“name”:英灵姓名  
}  
后端给前端json文件格式：  
{  
英灵1id: {'servent_name': '英灵姓名', 'servent_profile_pic': ['网址']},  
  
英灵2id: {'servent_name': 'hahaha', 'servent_profile_pic': [网址']},  
  
...  
  
}  
  
##特征搜索：  
前端给后端json文件格式：  
{  
“origin”:“明史”  
“region”:“罗马”  
“class”:“Ruler”  
“alignment”:“秩序.中”  
“weight”:[“下限”,“上限”]  
“height ”:[“下限”,“上限”]  
}
如果为空，就用”null”字符串代替。  
“下限”,“上限”如果为空，用”-1”代替。  
  
后端给前端json文件格式：  
{  
227: {'servent_name': '兰陵王',   
'servent_profile_pic': ['https://fgo.wiki/images/thumb/9/97/Servant227%E6%AD%A3%E9%9D%A21.png/150px-Servant227%E6%AD%A3%E9%9D%A21.png']},  

226: {'servent_name': 'hahaha',   
'servent_profile_pic': ['https://fgo.wiki/images/thumb/9/97/Servant227%E6%AD%A3%E9%9D%A21.png/150px-Servant227%E6%AD%A3%E9%9D%A21.png']}   
}  

##英灵界面：  
  
前端给后端json文件格式：  
{  
servent_id:XXXXXX  
}  
  
后端给前端json文件格式：  
