#test score, mid : 50, final : 75

class Score():
    def __init__(self, mid, final):
        self.__mid = mid
        self.__final = final
    
    @property
    def mid(self):
        return self.__mid
    @property
    def final(self):
        return self.__final

# 출력함수
score = Score(50, 75)
print((score.mid+score.final)/2)