class Pattern: 
    def pattern1(self,n):
        for _ in range(n):
            print("*" * n)
    def pattern2(self,n):
        for i in range(1,n+1):
            if (i == 1 or i == n):
                print("*"*n)
            else:
                print("*"+" "*(n-2)+"*")
    # def pattern3(self,n):
        

pt = Pattern()
num = int(input("num: "))
pt.pattern3(num)