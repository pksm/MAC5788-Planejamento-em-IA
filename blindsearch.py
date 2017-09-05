'''
First attempt to create a class for Automated Planning

Options:
- a class that grounds all predicates at once and returns a set of instantiated actions
- a class called by blindSearch that given a domain and a set of atoms returns a list of valid grounded actions
*- only one class that ground actions and implements the search 

Criar arquivo de teste, exemplos de teste:
- teste da função getInit com uma comparação com o que foi imputado no pddl
- teste da função isGoal com a meta do problema e uma entrada manual da entrada da meta
'''
import re

class blindSearch(object):
	"""docstring for blindSearch"""
	def __init__(self, domain, problem, search):
		#super(blindSearch, self).__init__()
		self._domain = domain
		self._problem = problem
		self._search = search
		#self._objects[obj.type] = self._objects.get(obj.type, [])
		# self.domainOperators = {}
		# for i in self.domain.operators:
		# 	self.domainOperators[i.name] = []
		# 	for j in i.precond:
		# 		self.domainOperators[i.name].append(str(j))

	@property
	def domain(self):
		return self._domain

	@property
	def problem(self):
		return self._problem

	@property
	def search(self):
		return self._search

	# @property
	# def domainOperators(self):
	# 	return self._domainOperators.copy()

	def getInit(self):
		return self.problem._init #return a set with the initial propositions

	def isGoal(self, state):
		return ((self.problem.goal & state) == self.problem.goal) #goal test
		#before last update: return ((self.problem._goal & state) == self.problem._goal)

	def applicableActions(self,state):
		validActions = []
		all_actions = self.domain.operators
		literals = self.problem.objects
		types = list(literals.keys()) #pode ser alterado para set
		precondAct = []

		for i in range(len(all_actions)):
			#precondAct.append()
			# print (all_actions[i].name)
			# print (all_actions[i].params[0].type)
'''
Ideia:
	criar dois dicts: (1) dict predicate (2) dict equality (pode ser um set com o nome das actions que contenham tipo equality na precond)
		(1) [action.name] = action.precond.predicate.name
'''
			for j in range(len(all_actions[i].precond)):
				print (all_actions[i].precond[j].predicate.name)


		for a in all_actions:
			if ((set(a.precond) & state) == set(a.precond)):
				validActions.append(a.name)

		return 


