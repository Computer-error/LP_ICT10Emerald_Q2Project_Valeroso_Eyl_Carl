from pyscript import document

def calculate_average(event):
    set = (document.getElementById("set").value)
    lev = (document.getElementById("lv").value)
    Fname = (document.getElementById("Fir").value)
    Lname = (document.getElementById("Las").value)
    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)
    score3 = float(document.getElementById("score3").value)
    score4 = float(document.getElementById("score4").value)
    score5 = float(document.getElementById("score5").value)
    score6 = float(document.getElementById("score6").value)
    score7 = float(document.getElementById("score7").value)

    average = (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7

    if average == 100:
        rank = "S"
    elif average == 99:
        rank = "A+"
    elif average >= 96:
        rank = "A"
    elif average >= 93:
        rank = "A-"
    elif average >= 90:
        rank = "B+"
    elif average >= 87:
        rank = "B"
    elif average >= 84:
        rank = "B-"
    elif average >= 81:
        rank = "C+"
    elif average >= 78:
        rank = "C"
    elif average >= 75:
        rank = "C-"
    elif average >= 72:
        rank = "D+"
    elif average >= 69:
        rank = "D"
    elif average >= 66:
        rank = "D-"
    elif average >= 63:
        rank = "F+"
    elif average >= 60:
        rank = "F"
    else:
        rank = "F-"

    if average >= 75:
        result = "passed"
    elif average == 100:
        result = "aced"
    else:
        result = "failed"

    document.getElementById("averageA").innerText = str(round(average,2))

    document.getElementById("result").innerText = ( Lname+", "+Fname+", a student from grade "+lev+set+", has "+result+" this quarter with a grade of "+str(round(average,2))+"("+rank+")""." )



