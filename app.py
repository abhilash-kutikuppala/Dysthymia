from flask import Flask, render_template, jsonify
import time
import subprocess
import sys
import csv
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/2)
print(maxInt)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/_get_data/', methods=['POST'])
def _get_data():
    #subprocess.run((["python3", "dep1.py"]))
    #while(1):
    #sys.stdout=open('result%s.txt' % scriptInstance,'w')
      #sleep(1)
      subprocess.run((["python", "gethistory.py"]))
      subprocess.run((["python", "dep2.py"]))
      f= open("extension/p","r")

    #myList = [true, false]
      true=f.readline()
      false=f.readline()
      f.close()
  
      myList=["Number of depressive queries :" + " "+ str(true)+ " ","Out of recent 500 searches!!!"]
      return jsonify({'data': render_template('response.html', myList=myList)})


if __name__ == "__main__":
    app.run(debug=True)

