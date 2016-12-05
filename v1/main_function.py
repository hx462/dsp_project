from myfunctions import clip16,matchwords
import pyttsx
#import pypiwin32 
import operator
import savevoice
import savecombination
import datetime

avg_fft = [0 for a in range(3)]

i = 0
n = 0

while n < 3:
    avg_fft[n] = savevoice.savevoice(n)
    #print"The average is ", avg_fft[n]
    n = n + 1
    

max_sound = max(avg_fft)
max_index = avg_fft.index(max_sound)

min_sound = min(avg_fft)
min_index = avg_fft.index(min_sound)

mid_sound = (max_sound + min_sound)/2


print "The maximum bound is ", max_sound, max_index
print "The medium bound is ", mid_sound
print "The minimum bound is ", min_sound, min_index


print "\nReady to start? make some sound"

avg_comb = [0 for c in range(2)]

while i < 2:
    avg_comb[i] = savecombination.savecombination(i)
    i = i + 1



#matchwords(avg_comb[0],avg_comb[1],max_sound,min_sound)

