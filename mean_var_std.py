import numpy as np

def calculate(list):

  # input: list of 9 digits
  # [1,2,3,4,5,6,7,8,9]
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")

  # convert list(9) -> array(3,3)
  '''[[1,2,3],
      [4,5,6],
      [7,8,9]]'''
  ## convert array(6,3) -> dict(6,3)
  inArray = np.array(list).reshape(3,3)

  # calculate mean
  meanCol = inArray.mean(axis=0).tolist()
  meanRow = inArray.mean(axis=1).tolist()
  meanMat = inArray.mean().tolist()
  meanList = [meanCol, meanRow, meanMat]
  np.array(meanList).tolist()

  print(meanList)

  # calculate variance
  varCol = inArray.var(axis=0).tolist()
  varRow = inArray.var(axis=1).tolist()
  varMat = inArray.var().tolist()
  varList = [varCol, varRow, varMat]

  # calculate standard deviation
  stdCol = inArray.std(axis=0).tolist()
  stdRow = inArray.std(axis=1).tolist()
  stdMat = inArray.std().tolist()
  stdList = [stdCol, stdRow, stdMat]

  # calculate max
  maxCol = inArray.max(axis=0).tolist()
  maxRow = inArray.max(axis=1).tolist()
  maxMat = inArray.max().tolist()
  maxList = [maxCol, maxRow, maxMat]

  # calculate min
  minCol = inArray.min(axis=0).tolist()
  minRow = inArray.min(axis=1).tolist()
  minMat = inArray.min().tolist()
  minList = [minCol, minRow, minMat]

  # calculate sum
  sumCol = inArray.sum(axis=0).tolist()
  sumRow = inArray.sum(axis=1).tolist()
  sumMat = inArray.sum().tolist()
  sumList = [sumCol, sumRow, sumMat]

  # calculations: array(6,3)
  '''{
    'mean': [axis1, axis2, flattened],
    'variance': [axis1, axis2, flattened],
    'standard deviation': [axis1, axis2, flattened],
    'max': [axis1, axis2, flattened],
    'min': [axis1, axis2, flattened],
    'sum': [axis1, axis2, flattened]
  }'''
  # create dictionary
  outDict = {
    'mean': meanList,
    'variance': varList,
    'standard deviation': stdList,
    'max': maxList,
    'min': minList,
    'sum': sumList
  }

  return outDict
