txt = "파이썬 파일 중에 a.txt 가 파이썬 폴더에 존재합니다.hwp"

print(txt.find('자바')) # -1 출력 ==> '없다'는 뜻
print(txt.find('.')) # 11 출력 ==> 11번재 위치에 있다는 뜻
print(txt.count('파이썬')) # 2 출력 == > 전체 있는 개수 출력
print(txt.count('.py')) # 0 출력 ==> 없으면 0
print(txt.endswith('.hwp')) # True 출력 ==> 제일 뒤에 해당문자열로 끝나면 True
print(txt.endswith('.')) # False ==> 제일 뒤에 해당문자열로 끝나지 않으면  False
