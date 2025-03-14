import json

data = {'name' : '홍길동', 'age' : 22}
d = {"name":"홍길동", "birth":"0525", "age": 30}
with open('myinfo.json','w') as f :
    json.dump(data,d,f,indent=2)  # s가 붙은 명령어는 파일을 직접 수정하지 않음
    json.dump(d, f,indent=2, ensure_ascii=False)

# with open('myinfo.json', 'w') as f :
#     data = json.load(f.read())
