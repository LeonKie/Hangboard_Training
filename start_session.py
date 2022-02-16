from playsound import playsound
import time
import winsound


from prompt_toolkit.shortcuts import ProgressBar , clear
from prompt_toolkit.formatted_text import HTML


current_time=0 #in secconds
time.sleep(5)
winsound.PlaySound(r'start.wav', winsound.SND_ASYNC)
time.sleep(3)
#winsound.PlaySound(None, winsound.SND_PURGE)

title = HTML('Downloading <style bg="yellow" fg="black">4 files...</style>')
label_Rest = HTML('<ansired>Rest:    [s]</ansired>: ')
label_workout = HTML('<b>Workout: [s]</b>: ')



def rest(seconds, end=False,title=None, label=label_Rest, next=''):
    with ProgressBar(title=title) as pb:
        for i in pb(range(seconds),label=label):
            global current_time
            time.sleep(1)
            current_time+=1
            #print("Time: ",int(current_time/60),"min",current_time%60,"sec")
            if i +1 == seconds -10 and end == False:
                winsound.PlaySound(r'notice.wav', winsound.SND_ASYNC)
            if i == seconds-4  and end == False:
                winsound.PlaySound(r'start.wav', winsound.SND_ASYNC)
            elif i+1 == seconds and end == True:
                winsound.PlaySound(r'end.wav', winsound.SND_ASYNC)
                
    
    
def workout(seconds,last=False,title=None):
    with ProgressBar(title=title) as pb:
        for i in pb(range(seconds),label=label_workout):
            global current_time
            time.sleep(1)
            current_time+=1
            #print("Time: ",int(current_time/60),"min",current_time%60,"sec")

            
            if i+1 == seconds and last == False:
                winsound.PlaySound(r'goal.wav', winsound.SND_ASYNC)
            elif i+1 == seconds and last == True:
                winsound.PlaySound(r'end.wav', winsound.SND_ASYNC)

def getTitle(workout_name,next=False):
    if next == False:
        return HTML('<ansigreen>Current Workout: ' + workout_name  + '</ansigreen>: ')
    else:
        return HTML('<ansiblue>Next Workout: '+ workout_name +' </ansiblue>: ')


while current_time < 60*10: #10 min
    
    
    workout_name= "3 Sets of 10 sec 20mm hands"
    workout_name_next = "3 Sets of 10 sec 3 finger rag"
   
     #print("Time: ",int(current_time/60),"min",current_time%60,"sec")
    for i in range(3):
        # 10s 20mm hangs
        workout(10,title=getTitle(workout_name)) if i<2 else workout(10,last=True,title=getTitle(workout_name))
        # 50s Resting
        rest(50) if i<2 else rest(50,title=getTitle(workout_name_next,next=True))
        clear()
    
    
    workout_name= workout_name_next
    workout_name_next = "1 Set of 2 finger pocket (middel, ring)"
    for i in range(3):
        # 10s hangs
        workout(10,title=getTitle(workout_name)) if i<2 else workout(10,last=True,title=getTitle(workout_name))
        # 50s Resting
        rest(50) if i<2 else rest(50,title=getTitle(workout_name_next,next=True))
        clear()
    
    
    workout_name= workout_name_next
    workout_name_next = "1 Set of 2 finger pocket (index, middel)"
    #print("1 Set of 2 finger pocket (middel, ring)")  
    # 10s workout
    workout(10,last=True,title=getTitle(workout_name))
    # 50s Resting
    rest(50,title=getTitle(workout_name_next,next=True))
    clear()
    
    workout_name= workout_name_next
    workout_name_next = "1 Set of 4 finger 20mm"
    
    #print("1 Set of 2 finger pocket (index, middel)")
    # 10s workout
    workout(10,last=True,title=getTitle(workout_name))
    # 50s Resting
    rest(50,title=getTitle(workout_name_next,next=True))
    clear()
    
    
    workout_name= workout_name_next
    workout_name_next = "1 Set of 4 finger 40mm"
    print("1 Set of 4 finger 20mm")
    # 10s workout
    workout(10,last=True,title=getTitle(workout_name))
    # 50s Resting
    rest(50,title=getTitle(workout_name_next,next=True))
    clear()
    
    
    workout_name= workout_name_next
    workout_name_next = "Done!!"
    print("1 Set of 4 finger 40mm")
    # 10s workout
    workout(10,last=True,title=getTitle(workout_name))
    # 50s Resting
    rest(50,title=getTitle(workout_name_next,next=True),end=True)
    clear()
          
    
    

    
    

