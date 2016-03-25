# -*- coding: utf-8 -*-

class Vacuum_cleaner_world(Environment):
	world = [0,0]
	location = 0
	sensors = {
		"location": lambda: location,
		"dirt": lambda: world[location]==1
		#"geography": return world
		}

	actions = ["clean", "pass", "left", "right"]
	
	def prior(this):
		return {"map":this.world, "actions":this.actions}

	def running():
		for t in range(turns):
			yield True
		yield False
	
	def update(this, action):
		action()

	def partial_evaluation(this,score,turn):
		score += sum(world) #We award one point per clean square and turn
	
	def final_evaluation(this,score, turn):
		return score


class vacuum_cleaner_agent():
    pass
	#def this()

#Modified vacuum_cleaner_world where agents are penalized for movement
class Vacuum_not_free_moves(vacuum_cleaner_world):
	def partial_evaluation(this,score,turn):
		score = super.partial_evaluation()
		if action in ["left", "right"]: score -= 1

#Location sensor is replaced by a bump sensor
class Bump_vacuum(Vacuum_cleaner_world):
	sensors = {
		#bump detects if last turn a boundary was tried to be transpassed
		"bump": lambda: this.action in ["left","right","up","down"]
		"dirt": lambda: (this.world[this.location]==1)
		#"geography": return world
		}
	def prior():
		return {"actions":actions}

#Suck action may fail and deposit dirt in location
class Murphys_law(Vacuum_cleaner_world):
	pass

#Clean squares have a chance of becoming dirty
class Small_children(Vacuum_cleaner_world):
	def update(this, action):
		action()
		for (i,j) in [(i,j) for i in range(world.len) for j in range(world[0].len)]:
			if(world[i][j]==1 and random(10)==0) world[i][j] = 0