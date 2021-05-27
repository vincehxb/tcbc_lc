import os
import random
import time
from flask import Flask
app = Flask(__name__)
def get_today_top_question():
  all_res=[]
  with open("./easy_top_qustion.txt",'r') as fp:
    for line in fp:
      q=line.strip()
      all_res.append(q)
  random.shuffle(all_res)
  return all_res

@app.route('/')
def hello_world():
  return "Hola"
#   t = time.localtime()
#   current_time = time.strftime("%Y/%M/%D %H:%M:%S", t)
#   all_questions_rand=get_today_top_question()
#   return f"{}\nTodays LeetCode Question:\n{}".format(current_time,all_questions_rand[0])
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=8080)
