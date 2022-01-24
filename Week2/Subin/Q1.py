class Score():
    def __init__(self, mid, final):
        self.__mid = mid #private 선언
        self.__final = final
@property #데코레이터
def mid(self):
    return self.__mid
@property
def final(self):
    return self.__final
score = Score(50, 75)
print((score.mid + score.final)/2)
