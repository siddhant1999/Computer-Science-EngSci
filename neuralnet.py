import numpy as np

class NeuralNet():
	inp = []
	outp = []
	def __init__(self, inp, outp):
		self.inp = inp
		self.outp = outp
		self.w= np.random.uniform(low=-1, high=1, size=(3,3,3))
		self.n= [[0 for j in range(3)] for i in range(4)]
		self.n[0][0]=1
		print self.w
		print "*"
		print self.n


	def forward(self):
		neurons=[2,3,3,1]
		print "*"
		for i in range(1,4):
			for j in range(neurons[i]):
				s= 0
				for k in range(neurons[i-1]):
					s+= self.n[i-1][k] * self.w[i-1][k][j]
				self.n[i][j] = np.tanh(s)
		print "n: ", self.n
		
	def backwards(self, ans):
		err = np.absolute(ans-self.n[3][0])




a = [[1,0],[0,1],[1,1],[1,0],[0,0],[1,1],[0,1],[0,0]]
b= [1,1,0,1,0,0,1,0]

x = NeuralNet(a, b)
x.forward()