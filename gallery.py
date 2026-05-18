from pyscript import document
from pyodide.ffi import create_proxy

# here are all the memories i could get !
PHOTOS = [
	# there was supposed to be a 1st one... but nvm! :3 ignore the id starting later
	{
		"id": 2, 
		"caption": "Teacher's Day",          
		"date": "Oct 2025",  
		"tag": "1", 
		"img_url": "teachersday.png"
	},
	{
		"id": 3, 
		"caption": "Food Fair and Minimart", 
		"date": "Dec 2025",  
		"tag": "2", 
		"img_url": "foodfair.png"
	},
	{
		"id": 4, 
		"caption": "Christmas Party",        
		"date": "Dec 2025",  
		"tag": "2", 
		"img_url": "christmas.png"
	},
	{
		"id": 5, 
		"caption": "Joint Campout",          
		"date": "Jan 2026",  
		"tag": "3", 
		"img_url": "help.png"
	},
	{
		"id": 6, 
		"caption": "Sabayang Pagbigkas",     
		"date": "Mar 2026",  
		"tag": "3", 
		"img_url": "sbp.png"
	},
	{
		"id": 7, 
		"caption": "Peace Congress",         
		"date": "Apr 2026",  
		"tag": "4", 
		"img_url": "pc.png"
	},
	{
		"id": 8, 
		"caption": "CAT Graduation",         
		"date": "Apr 2026",  
		"tag": "4", 
		"img_url": "cat.png"
	},
	{
		"id": 9, 
		"caption": "Intramurals",            
		"date": "Apr 2026",  
		"tag": "4", 
		"img_url": "intrams.png"
	}
]

# ui filtering blabla
TAG_LABELS = {
	"1": "1st Quarter", 
	"2": "2nd Quarter", 
	"3": "3rd Quarter", 
	"4": "4th Quarter"
}

# default
state = {"filter": "all"}

def render_gallery():
	grid = document.querySelector("#galleryGrid")
	grid.innerHTML = ""
	
	filtered = [p for p in PHOTOS if state["filter"] == "all" or p["tag"] == state["filter"]]

	# creates cards for each memory :)
	for photo in filtered:
		card = document.createElement("div")
		card.className = "memory-card animate__animated animate__fadeIn"
		
		meta_text = f"{TAG_LABELS.get(photo['tag'], photo['tag'].title())} · {photo['date']}"
		
		card.innerHTML = f"""
			<div class="card-img-wrapper">
				<img src="{photo['img_url']}" alt="{photo['caption']}">
			</div>
			<div class="card-body p-3">
				<h5 class="memory-title mb-1">{photo['caption']}</h5>
				<p class="memory-meta mb-0">{meta_text}</p>
			</div>
		"""
		
		grid.appendChild(card)

# sum filter typa stuff.
def handle_filter(event):
	target = event.target
	btn_id = target.id if target.id else target.closest("button").id
	
	state["filter"] = btn_id.replace("filter-", "")
	
	for btn in document.querySelectorAll("[id^='filter-']"):
		btn.classList.remove("active")
	document.querySelector(f"#{btn_id}").classList.add("active")

	# refresh when filter applied
	render_gallery()

# attaching the listeners so we know what shows up when u switch yadda yadda!
filter_proxy = create_proxy(handle_filter)
for tag in ["all"] + list(TAG_LABELS.keys()):
	btn = document.querySelector(f"#filter-{tag}")
	if btn:
		btn.addEventListener("click", filter_proxy)

# startup
render_gallery()