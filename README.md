# Fate_backend
## 姓名搜索
网址：域名/name_search  
### 前端给后端json文件格式：  
{  
name:英灵姓名  
}  
### 后端给前端json文件格式：  
[  
id: xxx servent_name: '英灵姓名1', 'servent_profile_pic': 网址},  
  
id: xxx servent_name: '英灵姓名1', 'servent_profile_pic': 网址},   
  
...  
  
]  
  
## 特征搜索
网址：域名/characteristics_search  
### 前端给后端json文件格式：  
{  
“origin”:“明史”  
“region”:“罗马”  
“class”:“Ruler”  
“alignment”:“秩序.中”  
“weight_down”:“下限”  
“weight_up”:“上限”  
“height_down ”:“下限”  
“height_up”:“上限”  
}  
如果为空，就用”null”字符串代替。  
“下限”,“上限”如果为空，用”-1”代替。  
  
### 后端给前端json文件格式：  
[  
id: xxx servent_name: '英灵姓名1', 'servent_profile_pic': 网址},  
  
id: xxx servent_name: '英灵姓名1', 'servent_profile_pic': 网址},   
  
...  
  
]  

  
  
网址：域名/get_attribute  
### 前端给后端发送get请求  
  
### 后端给前端json文件格式：  
{  
region:[XXX,XXXX,XXX,...]  
origin:[XXX,XXXX,XXX,...]  
alignment:[XXX,XXXX,XXX,...]  
servent_class:[XXX,XXXX,XXX,...]  

}  

## 英灵界面
网址：域名/servent_infomation  
### 前端给后端json文件格式：  
{  
servent_id:XXXXXX  
}  
  
### 后端给前端json文件格式：  
{  
servent_id: XXXXXX  
servent_name: XXXXXX  
servent_name_japanese: XXXXXXX  
servent_name_english: XXXXXX  
height: XXX  
weight: XXX  
gender: XXX  
strength: XXX  
endurance: XXX  
agility: XXX  
mana: XXX  
luck: XXX  
noble_phantasm: XXX  
craft_name: XXX  
craft_description: XXX  
craft_src: XXX  
alignment: [XXX,XXX,XXX]（可能多阵营）  
class: [XXX,XXX,XXX]（可能多职阶）  
illustrator: [XXX,XXX,XXX]（可能多画师）  
voice_actor: [XXX,XXX,XXX](可能多声优）  
region: [XXX,XXX,XXX]（可能多地域）  
origin: [XXX,XXX,XXX]（可能多起源）  
prototype: [XXX,XXX,XXX]（可能多原型）  
full_picture: [XXX,XXX,XXX]（可能多英灵图片）  
bond_text: [XXX,XXX,XXX]（可能多出处）  
}  

## explorer界面
网址：域名/explorer_infomation  
### 前端给后端json文件格式：  
{  
servent_id:XXXXXX  
}  
  
### 后端给前端json文件格式：  
{  
prototype: XXXXXX  
region: XXXXXX  
origin: XXXXXXX  
pedias: [{pedia_id:XXXXX,pedia_name:XXXXX,pedia_url:XXXXXX},....]  

articles: [{article_id:XXXXX,article_title:XXXXX,article_content:XXXXXX,author:XXXXXX},....]  

books: [{book_title:XXXXX,isbn_code:XXXXX,book_writer:XXXXXX},....]  

}  

## other界面
网址：域名/prototype_search  
### 前端给后端json文件格式：  
{  
prototype: XXXXXX  
}  
  
### 后端给前端json文件格式：  
[  
id: xxx servent_name: '英灵姓名1', 'servent_profile_pic': 网址},  
  
id: xxx servent_name: '英灵姓名1', 'servent_profile_pic': 网址},   
  
...  
  
]  

网址：域名/region_search  
### 前端给后端json文件格式：  
{  
region: XXXXXX  
}  
  
### 后端给前端json文件格式：  
[  
id: xxx servent_name: '英灵姓名1', 'servent_profile_pic': 网址},  
  
id: xxx servent_name: '英灵姓名1', 'servent_profile_pic': 网址},   
  
...  
  
]  

网址：域名/origin_search  
### 前端给后端json文件格式：  
{  
origin: XXXXXX  
}  
  
### 后端给前端json文件格式：  
[  
id: xxx servent_name: '英灵姓名1', 'servent_profile_pic': 网址},  
  
id: xxx servent_name: '英灵姓名1', 'servent_profile_pic': 网址},   
  
...  
  
]  
