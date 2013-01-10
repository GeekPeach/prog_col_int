critics={'Lisa': {'Lady': 2.5, 'Snake': 3.5, 'Just': 3.0, 'Superman': 3.5,
  'You': 2.5, 'Night': 3.0},
  'Gene': {'Lady': 3.0, 'Snake': 3.5, 'Just': 1.5, 'Superman':5.0, 
  'You': 4.0, 'Night': 0.5},
  'Michael': {'Lady': 2.5, 'Snake': 4.0, 'Just': 4.0, 'Superman': 3.5,
  'you': 3.5, 'Night': 3.5},
  'Claudia': {'Lady': 2.0, 'Snake':4.0, 'Just': 2.5, 'Superman': 4.0,
  'You': 3.0, 'Night': 1.5},
  'Mick': {'Lady': 3.0, 'Snake': 3.0, 'Just': 2.5, 'Superman': 3.0, 
  'You': 4.0, 'Night':3.0},
  'Jack': {'Lady': 4.0, 'Snake': 2.0, 'Just': 3.5, 'Superman': 4.0,
  'You': 3.0, 'Night': 3.5},
  'Toby': {'Snake': 4.0, 'You': 3.5, 'Superman': 4.0}} 

def sim_dist(prefs, person1, person2):
  si={}
  for item in prefs[person1]:
    if item in prefs[person2]:
      si[item]=1

  if len(si) == 0: return 0

  sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item], 2)
                      for item in prefs[person1] if item in prefs[person2]])

  return 1/(1 + sum_of_squares)


from math import sqrt

def sim_pearson(prefs, p1, p2):
  si={}
  for item in prefs[p1]:
    if item in prefs[p2]: si[item]=1

  n=len(si)

  if n==0: return 0

  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])

  sum1sq=sum([pow(prefs[p1][it], 2) for it in si])
  sum2sq=sum([pow(prefs[p2][it], 2) for it in si])

  pSum=sum([prefs[p1][it] * prefs[p2][it] for it in si])

  num=pSum - (sum1*sum2/n)
  den=sqrt((sum1sq - pow(sum1,2)/n) * (sum1sq - pow(sum2,2)/n))
  if den == 0: return 0

  r=num/den

  return r
