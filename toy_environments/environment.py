# -*- coding: utf-8 -*-

#Static toy environment for agents
class Environment():
	def __init__():
		raise Error_abstract_class
	
	#Runs the environment and assigns a score
	def evaluate(agent):
		score = 0 #To do: measure time
		agent.prior_knowledge = prior()
		while(running()):
			turn+=1
			this.percept = generate_percept()
			this.action = agent(percept)
			if not action in actions: raise Error
			update(action)
			this.score = partial_evaluation(score,turn)
		this.score = final_evaluation(score, turn)
		return this.score
	
	#Returns a dict of sensors:readings
	def generate_percept():
		percept = {}
		for sensor in sensors:
			percept.add(sensor.name, sensor.reading(state))
		return percept
