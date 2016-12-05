import pyttsx

def clip16( x ):    
    # Clipping for 16 bits
    if x > 32767:
        x = 32767
    elif x < -32768:
        x = -32768
    else:
        x = x        
    return int(x)


# matchwords(avg_comb[0],avg_comb[1],max_sound,min_sound)
def matchwords(x,y,max_sound,min_sound):
    engine = pyttsx.init()
    if (x > max_sound and y > max_sound):
        engine.say('Words1')
        engine.runAndWait()
    elif (x > max_sound and y > min_sound):
        engine.say('Words2')
        engine.runAndWait()
    elif (x > max_sound and y < min_sound):
        engine.say('Words3 ')
        engine.runAndWait()
    elif (x > min_sound and y > max_sound):
        engine.say('Words4 ')
        engine.runAndWait()
    elif (x > min_sound and y > min_sound):
        engine.say('Words5')
        engine.runAndWait()
    elif (x > min_sound and y < min_sound):
        engine.say('Words6 ')
        engine.runAndWait()
    elif (x < min_sound and y > mad_sound):
        engine.say('Words7 ')
        engine.runAndWait()
    elif (x < min_sound and y > min_sound):
        engine.say('Words8')
        engine.runAndWait()
    elif (x < min_sound and y < min_sound):
        engine.say('Words9 ')
        engine.runAndWait()
    print('Great!')



# elif(avg_comb(0) == 0 && avg_comb(1) ==1):
# engine.say('Good morning.')

# elif(avg_comb(0) == 0 && avg_comb(1) ==1):
# engine.say('Good morning.')

# elif(avg_comb(0) == 0 && avg_comb(1) ==1):
# engine.say('Good morning.')

# elif(avg_comb(0) == 0 && avg_comb(1) ==1):
# engine.say('Good morning.')

# elif(avg_comb(0) == 0 && avg_comb(1) ==1):
# engine.say('Good morning.')

# elif(avg_comb(0) == 0 && avg_comb(1) ==1):
# engine.say('Good morning.')

# elif(avg_comb(0) == 0 && avg_comb(1) ==1):
# engine.say('Good morning.')

# elif(avg_comb(0) == 0 && avg_comb(1) ==1):
# engine.say('Good morning.')

