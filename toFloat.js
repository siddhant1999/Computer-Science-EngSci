
//some sample numbers
str = '-1.230'
s="-00000.1"
d = "-00035.00100"

function toFloat(x){

	l = x.split('.') //splits into before and after decimal

	var mult=1;
	if(l[0].charAt(0)=='-'){
		mult = -1;
		l[0]=l[0].substr(1);
	}
	
	
	var s = l[0];
	while(s.charAt(0) === '0') {
		s = s.substr(1);
	}
	
	for(var i = l[1].length-1; i>=0;i--){
	  if(l[1][i] == '0'){
	    l[1]=l[1].slice(0,-1);
	  }
	  else break;
	}
	l[0] =s

	r =0
	
	m = 1
	for(var j = l[0].length-1; j>=0;j--){
		o = l[0][j]
		if (o.charCodeAt() >= 48 && o.charCodeAt()<=57) {
			val = o.charCodeAt() -48 //48 is the ASCII value of '0'
			r+= val*m;
			m*=10;
		}
		
	}

	u= 0;
	m=10;
	for(var j = 0; j < l[1].length; j++){
		o = l[1][j]
		if (o.charCodeAt() >= 48 && o.charCodeAt()<=57) {
			val = o.charCodeAt() -48
			u+= val/m;
			m*=10;
		}
		
	}
	r+=u;
	return (r*mult)
}


toFloat(str)