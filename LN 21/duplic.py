student_data={
    "id1" :{
        "name":"sara",
        "class":"V",
        "subject":["engish,math,science"]
    },
    "id2":{
        "name":"david",
        "class":"V",
        "subject":["engish,math,science"]
    },
    "id3":{
        "name":"Hamza",
        "class": "V",
        "subject" :["engish,math,science"]
    },
    "id4":{"name":"Hamza",
        "class": "V",
        "subject" :["engish,math,science"]}

}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result
      
      )