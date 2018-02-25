import numpy as np
import math

class NeuralNet():
	inp = []
	outp = []
	learning_rate=2

	def __init__(self, inp, outp):
		self.inp = inp
		self.outp = outp
		self.w= np.random.uniform(low=-1, high=1, size=(3,3,3))
		self.n= [[0 for j in range(3)] for i in range(4)]
		self.w[0][0][0] = 0
		self.w[0][1][0] = 0
		#self.n[0][0]=1
		print self.w
		#rint self.n

	def sigmoid(self, x):
		return 1 / (1 + math.exp(-x))


	def forward(self, firstLayer):
		#set the neuron values
		for p in range(len(firstLayer)):
			self.n[0][p] = firstLayer[p]
		self.neurons=[2,1]

		for i in range(1,2):
			#i is layer number
			for j in range(self.neurons[i]):
				#j is the neuron in this layer
				#s= bias[i-1]
				s=0
				for k in range(self.neurons[i-1]):
					#k is the neuron in the previous layer
					#print "neuron value:", self.n[i-1][k], "weight:", self.w[i-1][k][j]
					s+= self.n[i-1][k] * self.w[i-1][k][j]
				self.n[i][j] = self.sigmoid(s)
				#print "n:", self.n[i][j]
		#print "n: ", self.n
		'''print "-------------------------------------------"
		print self.w
		print "*******************************************"
		print self.n'''

	def outputLayer(self, ans):
		#in this case ans in the vector of outputs and must be of equal size to the last element of the neurons array
		totError = 0
		self.dup = self.w.copy() #this is a copy of the weights matrix so that we can update weights
		if self.neurons[-1] != len(ans):
			print "*error*"
			return
		deltaList=[]
		for i in range(self.neurons[-1]):
			target = ans[i]
			#print "target: ", target, self.n[1][i]
			val = self.n[1][i]
			totError += (target-val)*(target-val)/2.0
			#now that we have a neuron we are working with we should itterate over all the neurons
			delta = (val-target)*val*(1-val)
			#print "delta:", delta
			deltaList.append(delta)
			for j in range(self.neurons[-2]):
				neuron = self.n[0][j] #weight from neuron j in layer -1 (last element) to the ith neuron of the next layer
				weight = self.w[0][j][i]
				#print "neuron:", neuron, "weight:", weight
				#print "self.learning_rate * delta * neuron: ", self.learning_rate * delta * neuron
				self.dup[0][j][i] = weight-self.learning_rate * delta * neuron
				
		self.w=self.dup.copy()
		#this takes care of the first set
		#simply provide a list of the Eoi/doutoi which is just delta
		#print "Error:", totError
		
		print totError


#a = [[1,0],[0,1],[1,1],[1,0],[0,0],[1,1],[0,1],[0,0]]
#b= [[1],[1],[0],[1],[0],[0],[1],[0]]

a = np.random.randint(low=1, high=2, size=(100,2), dtype='l')
b=[]
for i in range(len(a)):
	if a[i][0] == a[i][1]:
		b.append([0.7])
	else:
		b.append([0.7])
# print a[1:100]
# print b[1:100]


x = NeuralNet(a, b)

for i in range(len(a)):
	x.forward(a[i])
	x.outputLayer(b[i])
