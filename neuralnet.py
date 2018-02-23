import numpy as np
import math

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
		print self.n

	def sigmoid(self, x):
		return 1 / (1 + math.exp(-x))

	def der(self, x):
		return self.sigmoid(x)*(1-self.sigmond(x))



	def forward(self):
		neurons=[2,3,3,1]
		bias = np.random.uniform(low=-1, high=1, size=(3))
		# the size of the bias array is one less than the number of layers
		print "*"

		for i in range(1,4):
			for j in range(neurons[i]):
				s= bias[i-1]
				for k in range(neurons[i-1]):
					s+= self.n[i-1][k] * self.w[i-1][k][j]
				self.n[i][j] = self.sigmoid(s)
		print "n: ", self.n
		
	def backwards(self, ans):
		err = ans-self.n[3][0]
		errsquared = err*err/2.0 #this is simply the error and isn't used for calculations
		de = -1*(ans - )
		#let's write a method for finding the amount by which each weight should be changed for a single layer






a = [[1,0],[0,1],[1,1],[1,0],[0,0],[1,1],[0,1],[0,0]]
b= [1,1,0,1,0,0,1,0]

x = NeuralNet(a, b)
x.forward()