# Python3
# 
# 
# 
#           Wildfoot 2016 10 31

class Significant_figures:
    def __init__(self, keyinstr):           #keyinstr   "1234.67800"
        in_float = float(keyinstr)          #float_in   1234.678
        in_int_str = repr(int(in_float))    #int_in     "1234"
        if len(in_int_str) == len(keyinstr):
            self.point_len = 0
        else:
            self.point_len = len(keyinstr) - len(repr(in_int_str)) + 1
        self.estimated = 1
        self.number = int(in_float * ( 10 ** self.point_len ))
        self.nlen = len(repr(self.number))

    def __add__(self, other):
        ret = Significant_figures("0")
        
        

    def __mul__(self, other):
        ret = Significant_figures("0")
        ret.number = self.number * other.number
        ret.nlen = len(repr(ret.number))
        ret.point_len = self.point_len + other.point_len
        ret.estimated = max(self.estimated * other.nlen, other.estimated * self.nlen)
        return ret
        
    #對使用者
    def __str__(self):
        return repr(self.number /(10 ** self.point_len))

    #對開發人員
    def __repr__(self):
        return repr(self.number) + "," + repr(self.point_len) + "," + repr(self.estimated)

# estimated 估計值位數
# number 去掉小數點
# nlen 數字長度 (-小數點)
# point_len 小數點位數



