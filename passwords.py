def  strengthen_passwords(passwords):
	x=['' for o in range(len(passwords))]
	for q in range(len(passwords)):
		s=list(passwords[q])
		for i in range(len(s)):
			if s[i] == 's' or s[i]=='S':
				s[i] = '5'
		val = 0
		if len(s)%2 == 1:
			if len(s) > 1 and s[len(s)/2].isdigit():
				val = int(s[len(s)/2])*2
				u= str(int(s[len(s)/2])*2)
				if len(u) > 1:
					s[len(s)/2] = u[0]
					s.insert(len(s)/2+1, u[1])
				else:
					s[len(s)/2] = u

		if len(s)%2 == 0:
			a = s[0]
			if s[len(s)-1].isupper():
				s[0] = s[len(s)-1].lower()
			else:
				s[0] = s[len(s)-1].upper()

			if a.isupper():
				s[len(s)-1] = a.lower()
			else:
				s[len(s)-1] = a.upper()
		p=[]	
		for i in range(len(s)):
			p.append(s[i].lower())
		p=''.join(p)
		t= p.find("nextcapital")
		if (t >= 0):
			a=s[t]
			b=s[t+1]
			c=s[t+2]
			d=s[t+3]

			s[t] = d
			s[t+1] = c
			s[t+2] = b
			s[t+3] = a
				

		x[q] = ''.join(s)

	return x



y =['GoCardinals', 'Doge', '123nEXtcapital99nextcapital123', 'ThreeSThree']
print strengthen_passwords(y)