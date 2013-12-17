__author__ = 'martin'


class LongCommonSubSequence:
    def __init__(self, X, Y):
        self.d = None
        self.p = None
        self.X = " " + X
        self.Y = " " + Y

    def BottomUpComputation(self):

        m = len(self.X)
        n = len(self.Y)

        # initialization
        self.d = d = [[0 for i in range(n)] for j in range(m)]
        self.p = p = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            d[i][0] = 0
        for j in range(n):
            d[0][j] = 0

        # dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                if self.X[i] == self.Y[j]:
                    d[i][j] = d[i - 1][j - 1] + 1
                    p[i][j] = "LU"
                else:
                    if d[i - 1][j] >= d[i][j - 1]:
                        d[i][j] = d[i - 1][j]
                        p[i][j] = "U"
                    else:
                        d[i][j] = d[i][j - 1]
                        p[i][j] = "L"

    def ShowBUC(self):
        d = self.d
        p = self.p
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

    def __PrintLCS(self, i, j):
        if i == 0 or j == 0:
            return None
        if self.p[i][j] == "LU":
            self.__PrintLCS(i - 1, j - 1)
            print(self.X[i], end=" ")
        else:
            if self.p[i][j] == "U":
                self.__PrintLCS(i - 1, j)
            else:
                self.__PrintLCS(i, j - 1)

    def PrintLCS(self):

        self.__PrintLCS(len(self.p)-1, len(self.p[0])-1)

# main
str1 = "ABCBDAB"
str2 = "BDCABA"

print("str1= %s" % str1)
print("str2= %s" % str2)

instance = LongCommonSubSequence(str1, str2)

instance.BottomUpComputation()

print("=> Show Bottom Up Computation:")
instance.ShowBUC()

print("=> Print Result:")
instance.PrintLCS()