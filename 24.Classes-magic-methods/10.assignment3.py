# Use the namedtuple function to create a GymExercise class whose
# instances will have three attribute: name, weight, and reps

import collections


GymExercise = collections.namedtuple('GymExercise', ['name', 'weight', 'reps'])

# Assign a squat variable to a GymExercise tuple object with
# a name of "squat", a weight of 265, and a rep count of 3
squat = GymExercise('squat', 265, 3)
print(squat.name)

# Assign a branch variable to a GymExercise tuple object with
# a name of "benchpress", a weight of 185, and a rep count of 5
branch = GymExercise(name='benchpress', weight=185, reps=5)
print(branch.weight)

# Assign a deadlift variable to a GymExercise tuple object with
# a name of "deadlift", a weight of 225, and a rep count of 6
deadlift = GymExercise('deadlift', 225, 6)
print(deadlift.reps)

# Assign a press variable to a GymExercise tuple object with
# a name of "press", a weight of 120, and a rep count of 8
press = GymExercise(name='press', weight=120, reps=8)
