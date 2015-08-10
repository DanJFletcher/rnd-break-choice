# ****************************************************************************
# PROGRAM: RANDOM BREAK CHOOSER                                              *
# DESCRIPTION: A SCRIPT TO RNDMLY CHOOSE FROM A LIST OF BREAK OPTIONS        *
# AUTHOR: DAN FLETCHER                                                       *
# DATE STARTED: AUG 10/15                                                    *
# ****************************************************************************

''' I recently started adopting the Pomodoro technique for scheduling breaks
during the work day. This script is like rolling the dice to choose what I do
on my short but frequent breaks. '''

# TODO:
# HIGH PRIORITY:
# ---------------
# 1. add more breaks to the dictionary
# 2. add a "reroll" option

# EXTRAS (LOW PRIORITY):
# ---------------
# 1. add option to set the current length of break (5min or 30min?)
# 2. make choices based on the length of current break (ie if the break is 5min,
#    don't choose a walk as an option).
# 3. look into making a GUI. (I've Never worked with graphics in Python yet)



import random

# A dictionary containing each break option and a description of the break
# from this article:
# https://open.bufferapp.com/science-taking-breaks-at-work/?utm_content=buffer4aa0e&utm_medium=social&utm_source=twitter.com&utm_campai
breaks = {1: 'Take a walk! \n'
          'A 20-minute stroll can increase blood flow to the brain, '
          'which can boost creative thought. Regular walks can enhance '
          'the connectivity of important brain circuits, combat age-related '
          'declines in brain function and improve memory and cognitive '
          'performance. ',
          
          2: 'Day Dream! \n'
          'Daydreaming “leads to creativity, and creative activities teach '
          'us agency, the ability to change the world, to mold it to our '
          'liking, to have a positive effect on our environment.”',

          3: 'Eat! \n'
          'Replenish your brain with a snack–here’s a look at some '
          'brain- and productivity-nourishing foods to grab.',

          4: 'Read! \n'
          'Read a (non-work) book–especially fiction. Studies have shown '
          'that individuals who frequently read fiction are better able to '
          'understand other people, empathize with them and see the world '
          'from their perspective.',

          5: 'Get a Coffee! \n'
          'OK, you probably already thought of this break option. But are you '
          'timing your coffee breaks correctly? For people who wake up '
          'between 6 a.m. and 8 a.m., the optimal times for consuming caffeine '
          'fall somewhere around 9:30 a.m. to 11:30 a.m. and 1:30 p.m. to '
          '5:30 p.m.',

          6: 'Doodle! \n'
          'Let your mind wander as you put pen to paper for some creative '
          'free time. Research shows that doodling can stimulate new ideas '
          'and help us stay focused.',}


# choose random int between one and the length of the dictionary
choice = random.randint(1,len(breaks))

# print the value at choice to the screen
print(breaks.get(choice))
