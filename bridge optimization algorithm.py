#bridge optimization algorithm

#declared variables

 #length of pi
#x= 10.0; #length of the attachment
#y= 20.0; #length between web legs
#t1= 1.3; #thickness of top member
#t2= 1.3; #thichness of web components
#t3= 1.3; #thickness of bottom flange used for strengthening
#h= 170.0; #height of entire section

def frange(start, stop, step):
	p = start
	while p < stop:
		yield p
		p += step

a= 100; #stiffiner spacing
l= 100.0;


def run():
	curbest = 0;
	for x in frange(5.0,20.0, 1.0):
		print "next:", x
		for y in frange(75.0,76.0, 1.0):
			if x*2 + y > l:
				continue
			for t1 in frange(1.3,6.5, 1.3):
				for t2 in frange(1.3,6.5, 1.3):
					for t3 in frange(1.3,6.5, 1.3):
						for h in frange(10,171, 1):
							'''x=10
							y=20;
							t1=1.3
							t2=1.3
							t3=1.3
							h=170'''
	
							MatboardE = 4000;
							P1M = 166.0377358;
							BM = -190;
							PI =3.14159;
							
							d= h-t1-t2;
							z=(l-2*x - y)/2;
							if z<0.1:
								continue;
							
							#Rectangle 1
							Area1 = t1*l;
							Yi1 = h-(t1/2.0);
							AYi1 = Area1 * Yi1;
							
							#Rectangle 2
							
							Area2 = d*t2;
							Yi2 = d/2.0;
							AYi2 = Area2 * Yi2;
							
							#Rectangle 4
							
							Area4 = x*t2;
							Yi4 = d + t2/2.0;
							AYi4 = Area4 * Yi4;
							
							V_max =1048772*0.8; #using 80% of 
							
							inter_V = (Area1 + Area2*2 + Area4*2)*1300;
							V = (Area1 + Area2*2 + Area4*2) * 1250 +t3*y*464.286;
							Volume_percentage = V/V_max * 100;
							#print Volume_percentage
							if Volume_percentage > 100:
								continue;
							
							y_bar = (AYi1+AYi2 +AYi4)/ (Area1 +Area2 + Area4);
							#print AYi1, AYi2, AYi4
							yi1 = Yi1 - y_bar;
							yi2 = Yi2 - y_bar;
							yi4 = Yi4 - y_bar;
							#print yi1, yi2, yi4
							A1yi_2 = Area1*(yi1)*(yi1);
							A2yi_2 = Area2*(yi2)*(yi2);
							A4yi_2 = Area4*(yi4)*(yi4);
							
							I=A1yi_2+ A2yi_2*2 + A4yi_2*2;
							
							#print (l*t1*t1*t1)/12.0, (t2*d*d*d)/12, (x*t2*t2*t2)/12
							I+= ((l*t1*t1*t1) + (t2*d*d*d)*2 + (x*t2*t2*t2)*2)/12.0;
							#print I
							
							#Flex Fail
							MTensile = 	30.0;
							MCompressive =	6.0;
							MShear=4.0;
							GShear=	2.0;
							
							Compressive_failure_P1 =MCompressive*I/(h-y_bar)/P1M;
							Tensile_failure_P1 =MTensile*I/y_bar/P1M;
							
							Compressive_failure_B =MCompressive*I/(y_bar)/BM;
							Tensile_failure_B =MTensile*I/(h-y_bar)/BM;
							
							#print Compressive_failure_P1, Tensile_failure_P1, Compressive_failure_B, Tensile_failure_B;
							
							#Q board
							QArea= t2*y_bar
							Qyi = y_bar/2
							Q1 =QArea * Qyi * 2;
							b1 = 2*t2
							
							#Matboard Shear Failure
							Shear_failure_centeroid=MShear*I*b1/Q1
							#print Shear_failure_centeroid
							
							#Glue Shear Failure
							
							Q2=l*t1*(h-t1/2-y_bar)
							b2= 2*x
							
							Shear_failure_glue = GShear*I*b2/Q2
							#print Shear_failure_glue
							
							#Top Flange Buckling
							
							k=4;
							stress=k*(PI*PI)*MatboardE/(12*0.99) * (t1/y)*(t1/y)
							Top_Buckling_failure_P1 =stress*I/(h-y_bar)/P1M;
							
							stress=4*(PI*PI)*MatboardE/(12*0.99) * (t3/y)*(t3/y)
							Top_Buckling_failure_B =abs(stress*I/(y_bar)/BM);
							
							#print Top_Buckling_failure_P1, Top_Buckling_failure_B
							
							#Buckling Ends
							k = 0.425
							
							stress=k*(PI*PI)*MatboardE/(12*0.99) * (t1/z)*(t1/z)
							
							Buckling_Ends_failure = stress*I/(h-y_bar)/P1M
							#print Buckling_Ends_failure
							
							#Buckling web
							k=6
							stress=k*(PI*PI)*MatboardE/(12*0.99) * (t2/(d-y_bar))* (t2/(d-y_bar))
							Bucking_web_failure_P1 = stress*I/(h-y_bar-t1)/P1M
							
							
							
							stress=k*(PI*PI)*MatboardE/(12*0.99) * (t2/(y_bar))* (t2/(y_bar))
							Bucking_web_failure_B = abs(stress*I/(y_bar)/BM)
							
							#print Bucking_web_failure_P1, Bucking_web_failure_B
							
							#Shear Buckling Web
							k=5
							stress=k*PI*PI*MatboardE/(12*0.99) *(((t2)/ (h-t1))*((t2)/ (h-t1)) + ((t2/a))*((t2/a)))
							Shear_bucking_web_failure = stress * I *b1/Q1;
							
							min_val = min(abs(Compressive_failure_P1), abs(Compressive_failure_B), abs(Tensile_failure_P1), abs(Tensile_failure_B), abs(Shear_failure_centeroid), abs(Shear_failure_glue), abs(Top_Buckling_failure_B), abs(Top_Buckling_failure_P1), abs(Buckling_Ends_failure), abs(Bucking_web_failure_P1), abs(Bucking_web_failure_B*3), abs(Shear_bucking_web_failure));
							
							if min_val > curbest:
								curbest= min_val;
								print "Fails at:", min_val
								print Compressive_failure_P1, Compressive_failure_B, Tensile_failure_P1, Tensile_failure_B, Shear_failure_centeroid, Shear_failure_glue, Top_Buckling_failure_B, Top_Buckling_failure_P1, Buckling_Ends_failure, Bucking_web_failure_P1, Bucking_web_failure_B, Shear_bucking_web_failure
								print "With: ", "x=", x, "y=", y, "t1=", t1, "t2=", t2, "t3=", t3, "h=", h ,"and a volume percentage", V/1048772
							#return curbest
							#print Shear_bucking_web_failure
	return curbest
	
curbest = run()
print "done"
print "The maximum point load that can be supported is:", curbest







