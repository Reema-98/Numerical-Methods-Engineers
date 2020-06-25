u2=float(input("u2:"))
u4=float(input("u4:"))
u5=float(input("u5:"))
for i in range(7):
	print("iteration : ",i+1)
	u1str='(1000+u2+500+u4)/4'
	u1=eval(u1str)
	u2str='(1000+u1+u1+u5)/4'
	u2=eval(u2str)
	u4str='(2000+u5+u1+u1)/4'
	u4=eval(u4str)
	u5str='(u4+u4+u2+u2)/4'
	u5=eval(u5str)
	print(u1,u2,u4,u5)
	print("=========")
