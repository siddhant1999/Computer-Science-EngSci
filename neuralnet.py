import numpy as np
import math

class NeuralNet():
	inp = []
	outp = []
	learning_rate=0.5

	def __init__(self, inp, outp):
		self.inp = inp
		self.outp = outp
		self.w= np.random.uniform(low=-1, high=1, size=(3,3,3))
		self.n= [[0 for j in range(3)] for i in range(4)]
		#self.n[0][0]=1
		print self.w
		print self.n

	def sigmoid(self, x):
		return 1 / (1 + math.exp(-x))

	def der(self, x):
		return self.sigmoid(x)*(1-self.sigmond(x))



	def forward(self, firstLayer):
		#set the neuron values
		for p in range(len(firstLayer)):
			self.n[0][p] = firstLayer[p]
		self.neurons=[2,3,3,1]
		bias = np.random.uniform(low=-1, high=1, size=(3))
		# the size of the bias array is one less than the number of layers
		print "*"

		for i in range(1,4):
			for j in range(self.neurons[i]):
				#s= bias[i-1]
				s=0
				for k in range(self.neurons[i-1]):
					s+= self.n[i-1][k] * self.w[i-1][k][j]
				self.n[i][j] = self.sigmoid(s)
		#print "n: ", self.n

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
			val = self.n[3][i]
			totError += (target-val)*(target-val)/2.0
			#now that we have a neuron we are working with we should itterate over all the neurons
			delta = (val-target)*target*(1-target)
			deltaList.append(delta)
			for j in range(self.neurons[-2]):
				neuron = self.n[-1][j] #weight from neuron j in layer -1 (last element) to the ith neuron of the next layer
				weight = self.w[-1][j][i]
				self.dup[-1][j][i] = weight-self.learning_rate * delta * neuron
				
		#this takes care of the first set
		#simply provide a list of the Eoi/doutoi which is just delta
		print "Error:", totError
		self.backprop(len(self.neurons)-2, deltaList)

	def backprop(self, layer, prev_deltas):

		if layer == 0:
			self.w = self.dup.copy()
		return

		newdeltaList = []
		for i in range(self.neurons[layer]):
			val = self.n[layer][i]
			deltasum = 0

			for j in range(self.neurons[layer+1]):
				weight = self.w[layer][i][j]
				eoi = deltaList[j]*weight
				deltasum+= eoi

			delta = deltasum*val*(1-val)
			newdeltaList.append(delta)
			#now itterate over every previous weight and modify it
			for k in range(self.neurons[layer-1]):
				neuron = self.n[layer-1][k]
				weight = self.w[layer-1][k][i]
				self.dup[layer-1][k][i] = weight - self.learning_rate * neuron * delta

		self.backprop(layer-1, newdeltaList)





a = [[1,0],[0,1],[1,1],[1,0],[0,0],[1,1],[0,1],[0,0]]
b= [[1],[1],[0],[1],[0],[0],[1],[0]]

x = NeuralNet(a, b)
x.forward(a[0])
print "Back:"
x.outputLayer(b[0])

x.forward(a[1])
print "Back:"
x.outputLayer(b[1])