import webbrowser

new=3
tebUrl="http://google.com/?#q";
term = "hello";
#term= raw_input("Enter search query: ");
for x in xrange(1,30):
	webbrowser.open(tebUrl+term,new=new);
#webbrowser.open(tebUrl+term,new=new);