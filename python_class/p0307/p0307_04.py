stuInfo = {
    "stuNo" : 1,
    "id" : "aaa",
    "pass" : "1111",
    "name" : "홍길동",
    "nicName" : "길동스"    
}
# 데이터베이스에 저장할 때 작은 확률이긴 하지만 한글로 된 키 값을 읽지 못하는 경우가 있어 주로 영어로 키 값 설정

print(stuInfo.get("tel")) # none
