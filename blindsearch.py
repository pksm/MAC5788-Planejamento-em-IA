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

class blindSearch(object):
	"""docstring for blindSearch"""
	def __init__(self, domain, problem, search):
		#super(blindSearch, self).__init__()
		self._domain = domain
		self._problem = problem
		self._search = search

	@property
	def domain(self):
		return self._domain

	@property
	def problem(self):
		return self._problem

	@property
	def search(self):
		return self._search

	def getInit(self):
		return self.problem._init #return a set with the initial propositions

	def isGoal(self, state):
		return ((self.problem.goal & state) == self.problem.goal) #goal test
		#before last update: return ((self.problem._goal & state) == self.problem._goal)

	def applicableActions(self,state):
		validActions = []
		all_actions = self.domain.operators
		literals = self.problem.objects
		#for s in state:


		for a in all_actions:
			if ((set(a.precond) & state) == set(a.precond)):
				validActions.append(a.name)

		return validActions
