from pyscript import document, display
import numpy as np

import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

# maps weekdays to enforce chronological sorting
weekOrder = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4}

days = []
absences = []

def displaying(e):

	day = document.getElementById('dayOfTheWeek').value
	absence = int(document.getElementById('absences').value)

	days.append(day)
	absences.append(absence)
	
	# zip() pairs matching indices together, sorted() looks up the day's numerical order in weekOrder
	sorted_pairs = sorted(zip(days, absences), key=lambda x: weekOrder.get(x[0], 99))

	# separate pairs back into individual, sorted lists
	sorted_days = [pair[0] for pair in sorted_pairs]
	sorted_absences = [pair[1] for pair in sorted_pairs]

	converted_absences = np.array(sorted_absences)

	plt.clf()

	plt.plot(sorted_days, converted_absences, marker='o', color='#b55d75', linewidth=2)

	plt.title("Weekly Attendance (Absences)")
	plt.xlabel("Day")
	plt.ylabel("Number of Absences")
	plt.grid()

	# prints the matplotlib inside a div instead of outside it
	output_div = document.getElementById('output')
	output_div.innerHTML = ""

	display(plt.gcf(), target="output") 