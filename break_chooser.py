import random


breaks = {'1': 'Take a walk! \n'
          'A 20-minute stroll can increase blood flow to the brain, '
          'which can boost creative thought. Regular walks can enhance '
          'the connectivity of important brain circuits, combat age-related '
          'declines in brain function and improve memory and cognitive '
          'performance. ',
          
          '2': 'Day Dream! \n'
          'Daydreaming “leads to creativity, and creative activities teach '
          'us agency, the ability to change the world, to mold it to our '
          'liking, to have a positive effect on our environment.”',

          '3': 'Eat! \n'
          'Replenish your brain with a snack–here’s a look at some '
          'brain- and productivity-nourishing foods to grab.'}


choice = random.randint(1,3)

select_break = breaks.get(str(choice))

print(select_break)
