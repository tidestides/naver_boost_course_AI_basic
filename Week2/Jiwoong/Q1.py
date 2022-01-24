class Score(object):
    def __init__(self,mid : int,final : int ):
        self.__mid = mid
        self.__final = final
    @property
    def mid(self):
        return self.__mid
    @property
    def final(self):
        return self.__final

score = Score(50,75)
print((score.mid + score.final)/2.0)