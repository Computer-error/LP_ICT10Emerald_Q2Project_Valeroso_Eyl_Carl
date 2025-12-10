from pyscript import document

def reveal(event):
    grp = float(document.getElementById("clb").value)
     
    if grp == 1:
        club = "Math Club: " \
        "Learn more about numbers and shapes and join competitions! " \
        "Meetings in Classroom 2-3. " \
        ">Academic"
    elif grp == 2:
        club = "Science Club: " \
        "Master science therough experiments. " \
        "Meetings at Science Laboratory. " \
        ">Academic"
    elif grp == 3:
        club = "Band Club: " \
        "Make art through music and sounds and perform in events! " \
        "Meetings at Music Room. " \
        ">Special"
    elif grp == 4:
        club = "Robotics Club: " \
        "Master the programming and create functional robots. " \
        "Meetings at Computer Room. " \
        ">Special"
    elif grp == 5:
        club = "Some clubs are not available yet, you can email us about your suggestion."
    else:
        club = "Please select a club to view"
        
    document.getElementById("view").innerText = club
