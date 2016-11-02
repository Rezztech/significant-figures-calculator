# Python3
# 
# 
# 
#           Wildfoot 2016 10 31

class Significant_figures:
    def __init__(self, keyinstr):           #keyinstr   "1234.67800"
        if keyinstr[0] == '-':
            self.sign = True
            keyinstr = keyinstr[1:]
        else:
            self.sign = False
        in_float = float(keyinstr)          #float_in   1234.678
        in_int_str = repr(int(in_float))    #int_in     "1234"
        if len(in_int_str) == len(keyinstr):
            self.point_len = 0
        else:
            self.point_len = len(keyinstr) - len(repr(in_int_str)) + 1
        self.estimated = 1
        self.number = int(in_float * ( 10 ** self.point_len ))
        self.nlen = len(repr(self.number))

    def _real_add(self, other):
        ret = Significant_figures("0")
        if self.point_len < other.point_len:
            increase = other.point_len - self.point_len
            self.estimated = self.estimated + increase
            self.point_len = self.point_len + increase
            self.nlen = self.nlen + increase
            self.number = self.number * ( 10 ** increase )
        elif self.point_len > other.point_len:
            increase = self.point_len - other.point_len
            other.estimated = other.estimated + increase
            other.point_len = other.point_len + increase
            other.nlen = other.nlen + increase
            other.number = other.number * ( 10 ** increase )
        ret.number = self.number + other.number
        ret.nlen = len(repr(ret.number))
        ret.point_len = self.point_len
        ret.estimated = max(self.estimated, other.estimated)
        return ret

    def _real_sub(self, other):
        ret = Significant_figures("0")
        if self.point_len < other.point_len:
            increase = other.point_len - self.point_len
            self.estimated = self.estimated + increase
            self.point_len = self.point_len + increase
            self.nlen = self.nlen + increase
            self.number = self.number * ( 10 ** increase )
        elif self.point_len > other.point_len:
            increase = self.point_len - other.point_len
            other.estimated = other.estimated + increase
            other.point_len = other.point_len + increase
            other.nlen = other.nlen + increase
            other.number = other.number * ( 10 ** increase )
        ret.number = self.number - other.number
        if ret.number < 0:
            ret.sign = True
            ret.number = ret.number * -1
        ret.nlen = len(repr(ret.number))
        ret.point_len = self.point_len
        ret.estimated = max(self.estimated, other.estimated)
        return ret

    def __add__(self, other):
        ret = Significant_figures("0")
        if self.sign and other.sign:            # - + -
            ret = _real_add(self, other)
            ret.sign = True
        elif self.sign and not other.sign:      # - + +
            ret = _real_sub(other, self)
        elif not self.sign and other.sign:      # + + -
            ret = _real_sub(self, other)
        elif not self.sign and not other.sign:  # + + +
            ret = _real_add(self, other)
            ret.sign = False
        return ret
        
    def __sub__(self, other):
        ret = Significant_figures("0")
        if self.sign and not other.sign:        # - - +
            ret = _real_add(self, other)
            ret.sign = True
        elif not self.sign and not other.sign:  # + - +
            ret = _real_sub(self, other)
        elif self.sign and other.sign:          # - - -
            ret = _real_sub(other, self)
        elif not self.sign and other.sign:      # + - -
            ret = _real_add(self, other)
            ret.sign = False
        return ret
    
    def __mul__(self, other):
        ret = Significant_figures("0")
        if (self.sign and other.sign) or (not self.sign and not other.sign):
            ret.sign = False
        else:
            ret.sign = True
        ret.number = self.number * other.number
        ret.nlen = len(repr(ret.number))
        ret.point_len = self.point_len + other.point_len
        ret.estimated = max(self.estimated * other.nlen, other.estimated * self.nlen)
        return ret
        
    #對使用者
    def __str__(self):
        if self.sign:
            return "-" + repr(self.number /(10 ** self.point_len))
        else:
            return repr(self.number /(10 ** self.point_len))

    #對開發人員
    def __repr__(self):
        if self.sign:
            return "-" + repr(self.number) + "," + repr(self.point_len) + "," + repr(self.estimated)
        else:
            return repr(self.number) + "," + repr(self.point_len) + "," + repr(self.estimated)

# estimated 估計值位數
# number 去掉小數點
# nlen 數字長度 (-小數點)
# point_len 小數點位數
# sign : 0:+ 1:-



