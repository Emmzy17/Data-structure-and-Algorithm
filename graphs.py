from collections import deque
search_queue = deque()


graph = {}
graph["you"]=["mom", "chibby", "Esther", "Dad", "Abbi", "mom"]

graph["orka"] = []
graph["chibby"] = ["you","emjay", "bright", "shakura"]

graph["Esther"] = []
graph["Dad"] = []
graph["Abbi"] = []
graph["mom"] = []
graph["bright"] = []
graph["emjay"] = []
graph["shakura"] = []

def person_is_seller(name):
	return name[-1] == 'm'
def search(name):
	search_queue = deque()
	search_queue +=graph[name]
	searched = []
	person = search_queue.popleft()
	while search_queue:
		if not person in  searched:
			if person_is_seller(person):
				print(person + "is a mango seller")
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False

print(search("you"))
