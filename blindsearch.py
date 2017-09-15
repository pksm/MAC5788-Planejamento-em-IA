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
from copy import deepcopy
from itertools import product


def generate(typ,lit): #lit eh um dict (literals) --- retorna todas as subst possiveis para uma acao
	combList = []
	if (len(typ)==1):
		return lit[typ[0]]  
	for t in typ:
		combList.append(lit[t])
	allComb = list(product(*combList))
	return allComb

def subst(comb,act): #comb is a list 
	for i in range(len(act.params)):
		act.params[i]._value = comb[i]
	return act
		



class blindSearch(object):
	"""docstring for blindSearch"""
	def __init__(self, domain, problem, search):
		#super(blindSearch, self).__init__()
		self._domain = domain
		self._problem = problem
		self._search = search
		self.operatorsPrecond = {}
		self.genDict()
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

	def genDict(self):
		all_actions = self._domain.operators
		for a in all_actions:
			for p in a.precond:
				if p.predicate.name != '=':
					self.operatorsPrecond[a] = self.operatorsPrecond.get(a, set()) #na hora de fazer union, intersect, difference mudar para set
					self.operatorsPrecond[a].add(re.sub(r'\([^)]*\)', '', str(p)))
					# self.operatorsPrecond[a.name] = self.operatorsPrecond.get(a.name, set()) #na hora de fazer union, intersect, difference mudar para set
					# self.operatorsPrecond[a.name].add(re.sub(r'\([^)]*\)', '', str(p)))

	# @property
	# def domainOperators(self):
	# 	return self._domainOperators.copy()

	def getInit(self):
		return self.problem._init #return a set with the initial propositions

	def isGoal(self, state):
		return ((self.problem.goal & state) == self.problem.goal) #goal test
		#before last update: return ((self.problem._goal & state) == self.problem._goal)

	def grounding(self, actions, state): #returns list of instatiated applicable actions
		literals = self.problem.objects #dict key -> type   values -> literals
		actToGround = set()
		for a in actions:
			tempAction = deepcopy(a)
			params = deepcopy(a.params)
			var = [i.name for i in params]
			typ = [i.type for i in params]
			#print ("HEYY", a.name, type(params),params[len(params)-1].name, params[len(params)-1].type, len(params), var, typ)
			#print(self.gen_all_combinations(['block', 'girafa'],{'block' : ['d', 'b', 'a', 'c'], 'girafa' : ['mimosa', 'gigi']}))
			combAll = generate(typ,literals)
			#print("possible combinations for ", a.name, combAll)
			#subst(list(combAll), deepcopy(a),var)
			for i in combAll:
			 	tempAction = subst(list(i), deepcopy(a))
			 	actToGround.add(tempAction)
			 	
			for ac in actToGround:
				print(ac)
				for par in ac.params:
					print(par.value ,end='')
				print(" ")

		print ("Literals Problem > ", literals) 



	def applicableActions(self,state): #esperando um state do tipo set
		validActions = set()
		all_actions = self.domain.operators
		atomState = {re.sub(r'\([^)]*\)', '', str(i)) for i in self.problem.init} #sera state depois
		for i in self.operatorsPrecond.keys():
			if ((self.operatorsPrecond[i] & atomState) == self.operatorsPrecond[i]):
				validActions.add(i)
		print ("VALID FOR > ", self.problem.init, "ACTIONS > ", validActions )
		self.grounding(all_actions, self.problem.init)
		#actInst = self.grounding(all_actions, self.problem.init) # self.grounding(validActions, state) in the future
		#generate successor state for each actInst



		# atomState = re.sub(r'\([^)]*\)', '', str(self.problem.init))
		#print(atomState, type(self.problem.init), self.problem.init)
		#types = list(literals.keys()) #pode ser alterado para set 
		#types2 = list(literals.items())
		#precondAct = []
		'''
		Ideia:
			criar dois dicts: (1) dict predicate (2) dict equality (pode ser um set com o nome das actions que contenham tipo equality na precond)
			(1) [action.name] = action.precond.predicate.name

			se tem equality nas preconds, entao deve ter uma flag para detectar isso e testar os literais

			OLD:
			- pegar toda letra que sucede ? em Action.params e adicionar a um set para nao ter duplicadas
			- para cada letra gerar um novo set com o mesmo index e atribuir 
			------------------------------------
			NOW: a ideia eh q dado um set de atomos, eh possivel verificar a aplicabilidade dos operadores disponiveis sem instanciar, olhar num 
			dicionario talvez...chamar funcao q cria esse dicionario assim que entra no __init___
				[action.name] = [action.precond (sem os predicados de igualdade)]	DICT referente a DOMAIN

		'''
		# for a in all_actions:
		# 	if ((set(a.precond) & state) == set(a.precond)):
		# 		validActions.append(a.name)

		return 

