class Time:
    def __init__(self,hour,minute,second):
        self.__second=second
        self.__minute=minute
        self.__hour=hour
    def __add__(self,other):
        second=self.__second+other.__second
        minute=self.minute+other.__minute
        hour=self.__hour+minute.__hour
    if second > 60:
        minute=minute+int(minute/60)
        second=second%60
    if minute > 60:
        hour=hour+int(minute/60)
        minute=minute/60
    time="{0}hour:{1}minute:{2}second:",format(hour,minute,second)
        return time
h1=int(input("enter the hour of 1st time"))
m1=int(input("enter the minute of 1st time"))
s1=int(input("enter the second of 1st time"))
h2=int(input("enter the hour of 2nd time"))
m2=int(input("enter the minute of 2nd time"))
s2=int(input("enter the second of 2nd time"))
time1=Time(h1,m1,s1)
time2=Time(h2,m2,s2)
print("sum of time:",time1+time2)