word = rdd.filter(lambda s: "error" in s)

def containsError(s):
  return "error" in s 
word = rdd.filter(containsError)
