import pickle
import networkx as nx
import matplotlib.pyplot as plt
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

random.seed(123)

class CreateNetworkGraph:
	def __init__(self, inputFile):
		self.inputFile = inputFile
		self.V = list() #[]
		#~ self.c_d = dict()
		#~ self.c_s = dict()
		self.c = dict()
		self.E = list() #[]
		self.d = dict()
		self.l = dict()
		
		self.g = pickle.load(open(self.inputFile))

	def getNodes(self):
		totalDegree = 0
		for i in self.g.degree(self.g.nodes()):
			totalDegree += self.g.degree(i)
		meanDegree = totalDegree / self.g.__len__()
		
		for n in self.g.nodes(data = True):
			print n
		
		# randomCdlist = [500, 1000, 1500, 2000]
		randomCdlist = [5000]
		#~ randomCslist = [5, 10, 15, 20]
		#~ randomCslist = [20]
		for n in self.g.nodes():
			self.V.append(n)
			# If the degree of a node is larger than the mean degree,
			# make it a switch node
			if self.g.degree(n) <= meanDegree:
				#~ self.c_d[n] = 100
				#~ self.c_d[n] = random.choice(randomCdlist)
				#~ self.c_s[n] = 0
				# self.c[n] = 2000
				self.c[n] = random.choice(randomCdlist)
			else:
				#~ self.c_d[n] = 0
				#~ self.c_s[n] = 5
				#~ self.c_s[n] = random.choice(randomCslist)
#				print "switch", n
				self.c[n] = 800
		
#		print "V", self.V
#		print "c_d", self.c_d
#		print "c_s", self.c_s		
		#~ return self.V, self.c_d, self.c_s
		return self.V, self.c

	def getEdges(self):
		# randomDlist = [1000, 1500, 2000]
		randomDlist = [1500]

		for u,v,edata in self.g.edges(data = True):
			self.E.append((u,v))
			#self.d[(u,v)] = edata['dr']
			# self.d[(u,v)] = 2000 # Gbps
			self.d[(u,v)] = random.choice(randomDlist)
			#~ self.d[(u,v)] = 200 # Gbps
			self.l[(u,v)] = edata['lat'] / 1000 # Seconds
		# Make the graph bidirectional
		for (u,v) in self.g.edges():
			if (v,u) not in self.g.edges():
				self.E.append((v,u))
				self.d[(v,u)] = self.d[(u,v)]
				self.l[(v,u)] = self.l[(u,v)]
		# Make self loops on every node
		for v in self.g.nodes():
			if (v,v) not in self.E:
				self.E.append((v,v))
				self.d[(v,v)] = 500000
				self.l[(v,v)] = 0
#		print "E", self.E
#		print "d", self.d
#		print "l", self.l
		return self.E, self.d, self.l
		
	#~ def debugPNG(self):
		#~ G = nx.DiGraph()
		#~ for node in self.nodes:
			#~ (xpos,ypos) = self.coordinates[node]
			#~ p = "{0},{1}!".format(xpos,ypos)
			#~ G.add_node(node, x=xpos, y=ypos, pos=p, pin='true',shape='circle', width=1, height=1, color='blue', fillcolor='blue', style='filled')
		#~ for edge in self.edges:
			#~ G.add_edge(edge[0],edge[1])
#~ 
		#~ #nx.draw_graphviz(G,prog='neato')
		#~ #plt.savefig("nobel-eu.png")
		#~ A = nx.to_agraph(G)
		#~ A.layout()
		#~ A.draw('nobel-eu.png')

