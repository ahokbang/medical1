class Tv: # calss 선언 - 설계도
    channel = 0
    color = "black"
    size = 65
    volume = 0
    
    def Tv() :
        pass
    
    def __init__(self, channel, color, size, volume) : # *** 위치 ***
        self.channel = channel
        self.color = color 
        self.size = size 
        self.volume = volume
        
    def up_volume(self, volume) :
        self.volume += volume
        
    def down_volume(self, volume) :
        self.volume -= volume
    
    def up_channel(self, channel) :
        self.channel += channel
        
    def down_channel(self, channel) :
        self.channel -= channel
        
 
# 철수-화이트,채널 10 변경, 채널 2 증가
# 영희-핑크, 채널 7 변경, 채널 5 증가
# 반장-실버, 채널 1 변경, 채널 3 증가

cs = Tv(10, "white", 65, 0) # 객체선언 - 제품생산
cs.up_channel(2)

print("철수 tv : ", cs.channel, cs.color, cs.size, cs.volume)

yh = Tv(7, "pink", 65, 0)
yh.up_channel(5)
print("영희 tv : ", yh.channel, yh.color, yh.size, yh.volume)

bj = Tv(1, "silver", 65, 0)
bj.up_channel(3)
print("반장 tv : ", bj.channel, bj.color, bj.size, bj.volume)


''' 선생님 풀이
- 철수-화이트,채널 10 변경, 채널 2 증가
t1 = Tv()
t1.color = "화이트"
t1.size = 65  # 없어도 돼
t1.volume = 0 # 없어도 돼
t1.channel = 19
t1.up_channel(2)
print(f"철수 TV : {t1.color}, {t1.size}, {t1.volume}, {t1.channel}")


- 영희-핑크, 채널 7 변경, 채널 5 증가
class Tv: # calss 선언 - 설계도
    channel = 0
    color = "black"
    size = 65
    volume = 0
    
    def Tv() :
        pass
    
    def __init__(self, channel=0, color="", size=0, volume=0) : # *** 위치 ***
        self.channel = channel
        self.color = color 
        self.size = size 
        self.volume = volume
        
    def up_volume(self, volume) :
        self.volume += volume
        
    def down_volume(self, volume) :
        self.volume -= volume
    
    def up_channel(self, channel) :
        self.channel += channel
        
    def down_channel(self, channel) :
        self.channel -= channel
        
t2 = Tv("핑크", 65, 0, 7)
print(f"영희 TV : {t2.color}, {t2.size}, {t2.volume}, {t2.channel}")
t2.up_chanee.(5)
print(f"영희 TV : {t2.color}, {t2.size}, {t2.volume}, {t2.channel}")

- 반장-실버, 채널 1 변경, 채널 3 증가
t3 = Tv("실버", 65, 0, 1)
print(f"반장 TV : {t3.color}, {t3.size}, {t3.volume}, {t3.channel}")
t2.up_chanee.(3)
print(f"영희 TV : {t3.color}, {t3.size}, {t3.volume}, {t3.channel}")
'''