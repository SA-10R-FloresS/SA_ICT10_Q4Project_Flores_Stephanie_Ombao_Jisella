from js import document as d

# global list to store all Classmate objects
allClassmates = []

# blueprint class
class Classmate:
	def __init__ (self, name, section, favorite_subject):
		self.name = name
		self.section = section
		self.favorite_subject = favorite_subject

	def introduce(self):
		# two lines of introduction to make it look cutesy <3
		line1 = f"Hi! I'm <strong>{self.name}</strong> from <strong>10-{self.section}</strong>."
		line2 = f"My favorite subject is <strong>{self.favorite_subject}</strong>."
		
		# return as a tuple... to be unpacked!
		return (line1, line2)

def displayClassmates(event):
	outputDiv = d.getElementById("cardContainer")
	outputDiv.innerHTML = ""

	# loopy loop loop...
	for student in allClassmates:
		
		# unpack tuple, use method
		line1, line2 = student.introduce()

		# each classmate has their own little box/card! :D
		card = d.createElement("div")
		card.className = "classmate-card"

		name_el = d.createElement("p")
		name_el.className = "name"
		name_el.innerHTML = line1

		meta_el = d.createElement("p")
		meta_el.className = "meta"
		meta_el.innerHTML = line2

		# nest the two lines inside the card, then add card to the container!
		card.appendChild(name_el)
		card.appendChild(meta_el)
		outputDiv.appendChild(card)

def addClassmates(event):
	# HTML input fields
	cmName = d.getElementById("nameInput")
	cmSection = d.getElementById("sectionInput")
	cmSubject = d.getElementById("subjectInput")

	# checks if any field is empty/blank
	if not cmName.value.strip() or not cmSection.value.strip() or not cmSubject.value.strip():
		return
	
	# instantiation 🤓 and add it to the list for display
	newClassmate = Classmate(cmName.value, cmSection.value, cmSubject.value)
	allClassmates.append(newClassmate)

	# updates the View All button to show the # of classmates added
	viewBtn = d.querySelector("button[py-click='displayClassmates']")

	if viewBtn:
		viewBtn.innerText = f"View All ({len(allClassmates)}) →"

	# clear input fields after adding
	cmName.value = ""
	cmSection.value = ""
	cmSubject.value = ""