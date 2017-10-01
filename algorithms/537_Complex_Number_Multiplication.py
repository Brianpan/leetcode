class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        validset = sets.Set(["-","0","1","2","3","4","5","6","7","8","9"])
        a_arr = []
        b_arr = []
        stack = ""
        for s in a:
            if s in validset:
                stack += s
            if s == "+":
                a_arr.append(stack)
                stack = ""
            if s == "i":
                if stack == "":
                    stack += "1"
                a_arr.append(stack)
                stack = ""
        
        for s in b:
            if s in validset:
                stack += s
            if s == "+":
                b_arr.append(stack)
                stack = ""
            if s == "i":
                if stack == "":
                    stack += "1"
                b_arr.append(stack)
                stack = ""
        
        real_num = int(a_arr[0])*int(b_arr[0]) - int(a_arr[1])*int(b_arr[1])
        complex_num = int(a_arr[0])*int(b_arr[1]) + int(a_arr[1])*int(b_arr[0])
        
        return str(real_num) + "+" + str(complex_num)+"i"