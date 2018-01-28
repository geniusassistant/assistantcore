# flips a coin
def flip():
    tof = bool(random.getrandbits(1))
    if tof == True:
        return 'heads'
    else:
        return 'tails'

#main func for api
#TODO: work on transitioning main functions over here
def outsource():
    if 'heads or tails' in text:
        return flip()