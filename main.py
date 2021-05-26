import os
from flask import Flask
app = Flask(__name__)
def get_today_top_question():
  all_res=[]
  with open("easy_top_qustion.txt",'r') as fp:
    for line in fp:
      q=line.strip()
      all_res.append(q)
  random.shuffle(all_res)
  return all_res

@app.route('/')
def hello_world():
  all_questions_rand=get_today_top_question()
  return "Todays LeetCode Question: {}".format(all_questions_rand[0])
  #return 'Yo quiero mi camiseta!! por favor'
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=8080)
