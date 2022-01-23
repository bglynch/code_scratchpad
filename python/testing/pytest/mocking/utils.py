from database import read_db

def foo():
  print("foo, enter")
  x = read_db()
  y = write_db()
  return x + y

def write_db():
  print("Writing value to DB")
  return 1