def FirstFactorial(num):
  if num == 1 or num == 0:
    return 1
  else:
    # code goes here 
    return num * FirstFactorial(num-1)

print FirstFactorial(int(raw_input()))