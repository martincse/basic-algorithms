__author__ = 'martin'

class LongCommonSubString:
    def __init__(self, X, Y):
        self.d = None
        self.pMax = None
        self.lMax = None
        self.X = " " + X
        self.Y = " " + Y

    def BottomUpComputation(self):

        m = len(self.X)
        n = len(self.Y)
        self.lMax = 0
        self.pMax = 0

        # initialization
        self.d = d = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            d[i][0] = 0
        for j in range(n):
            d[0][j] = 0

        # dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                if self.X[i] != self.Y[j]:
                    d[i][j] = 0
                else:
                    d[i][j] = d[i - 1][j - 1] + 1
                    if d[i][j] > self.lMax:
                        self.lMax = d[i][j]
                        self.pMax = i

    def ShowBUC(self):
        d = self.d
        X = self.X
        Y = self.Y

        print(" ", end=" ")
        for i in range(len(Y)):
            print(Y[i], end=" ")
        print("")

        for i in range(len(d)):
            print(X[i], end=" ")
            for j in range(len(d[i])):
                print(d[i][j], end=" ")
            print("")

    def PrintLCString(self):
        if self.lMax == 0:
            return None

        for i in range(self.pMax - self.lMax, self.pMax):
            print(self.X[i+1], end=" ")

        print("")

# main
str1 = "lollipop"
str2 = "philologist"

print("str1= %s" % str1)
print("str2= %s" % str2)

instance = LongCommonSubString(str1, str2)

instance.BottomUpComputation()

print("=> Show Bottom Up Computation:")
instance.ShowBUC()

print("=> Print Result:")
instance.PrintLCString()
print("longest length = %d" % instance.lMax)