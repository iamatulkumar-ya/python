
"""
Problem Statement: 
For the given input array determine the minimum number of jumps would required to reach the end of the array.

So if at the position of 0th means 2 in this case, then we can have max 2 jumps from there, 
likewise if we are at position 1st means 3 in this case then we can have max 3 jumps to reach at the end
"""


li =  [2,3,1,1,4]
# li =  [2,1]
import time
def get_minimum_jumps():
    st = time.time()
    jumpCounter = 0
    i = 0 
    reached_at_end = False  
    while not reached_at_end:  
        # need to assign currentPosition
        currentPosition = li[i]
        futureJump = 0
        futurePosition = 0
        print("currentPosition and jumpCounter ", currentPosition, jumpCounter)

        if len(li) == 1:
            jumpCounter +=1
            return jumpCounter
        

        if i + currentPosition >= len(li):
            jumpCounter += 1
            return jumpCounter
    

        for j in range(1, currentPosition + 1): 
            if i+j <= len(li)-1 and li[i+j] >= futureJump :
                futureJump = li[i+j] 
                futurePosition = i+j

        print("futurePosition and futureJump :", futurePosition, futureJump )
        # need to check the jumps
        if futurePosition + futureJump >= len(li)-1:
            # means we reached to the end
            jumpCounter += 2 # need to do 2, because current to future and futrue to end of the list
            return jumpCounter

        else:
            jumpCounter += 1
            i = futurePosition + futureJump
                
        
        print("next processing position:", i)

        if time.time() - st > 10:
            reached_at_end = True
         

print("Minimum jumps required to reach at end would be: ", get_minimum_jumps())


