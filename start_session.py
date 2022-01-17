from playsound import playsound
import time
import winsound

import multiprocessing


current_time=0 #in secconds
time.sleep(5)
winsound.PlaySound(r'start.wav', winsound.SND_ASYNC)
time.sleep(3)
#winsound.PlaySound(None, winsound.SND_PURGE)



def rest(seconds, end=False):
    for i in range(seconds):
        global current_time
        time.sleep(1)
        current_time+=1
        print("Time: ",int(current_time/60),"min",current_time%60,"sec")
        if i == seconds-4  and end == False:
            winsound.PlaySound(r'start.wav', winsound.SND_ASYNC)
        elif i+1 == seconds and end == True:
            winsound.PlaySound(r'end.wav', winsound.SND_ASYNC)
    
    
def workout(seconds,last=False):
    for i in range(seconds):
        global current_time
        time.sleep(1)
        current_time+=1
        print("Time: ",int(current_time/60),"min",current_time%60,"sec")

           
        if i+1 == seconds and last == False:
            winsound.PlaySound(r'goal.wav', winsound.SND_ASYNC)
        elif i+1 == seconds and last == True:
            winsound.PlaySound(r'end.wav', winsound.SND_ASYNC)



while current_time < 60*10: #10 min
    
    
    
    print("3 Sets of 10 sec 20mm hands")
    print("Time: ",int(current_time/60),"min",current_time%60,"sec")
    for i in range(3):
        # 10s 20mm hangs
        workout(10) if i<2 else workout(10,True)
        # 50s Resting
        rest(50)
    
    print("3 Sets of 10 sec 3 finger rag") 
    for i in range(3):
        # 10s workout
        workout(10) if i<2 else workout(10,True)
        # 50s Resting
        rest(50)
    
    
    print("1 Set of 2 finger pocket (middel, ring)")  
    # 10s workout
    workout(10,True)
    # 50s Resting
    rest(50)
        
    print("1 Set of 2 finger pocket (index, middel)")
    # 10s workout
    workout(10,True)
    # 50s Resting
    rest(50)
    
    print("1 Set of 4 finger 20mm")
    # 10s workout
    workout(10,True)
    # 50s Resting
    rest(50)
    
    print("1 Set of 4 finger 40mm")
    # 10s workout
    workout(10,True)
    # 50s Resting
    rest(50,end=True)
          
    
    

    
    

