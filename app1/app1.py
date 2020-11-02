from flask import request, Flask
import pymongo
from bson.json_util import dumps
from datetime import datetime as dtm

app1 = Flask(__name__)

connection_url = 'mongodb://cobadatabase:<DatabasePassword>@cluster0-shard-00-00.sxr4g.gcp.mongodb.net:27017,cluster0-shard-00-01.sxr4g.gcp.mongodb.net:27017,cluster0-shard-00-02.sxr4g.gcp.mongodb.net:27017/Example?ssl=true&replicaSet=atlas-u07olz-shard-0&authSource=admin&retryWrites=true&w=majority'
client = pymongo.MongoClient(connection_url)

database = client.get_database('Example')
Suhu = database.suhu

@app1.route("/info", methods = ['GET'])
def get_all_contact():
    data = Suhu.find({})
    return 'INI WEB SERVER APP 1 \n ' + dumps(data)

@app1.route('/input/suhu', methods = ["POST"])
def post():
    sekarang = dtm.now()
    tgl = dtm.strftime(sekarang, '%d-%b-%Y/%H:%M:%S')
    _json = request.json
    #_suhu = _json['suhu_tubuh']
    data={ 'suhu_tubuh': _json , 'waktu': tgl}
    Suhu.insert(data)
    print(request.data,tgl + "\tditambahkan ke database")
    print(request.headers)
    return str(data) + "\n berhasil input data ke Database ... BTW, INI WEB SERVER APP 1"
    
@app1.route('/')
def hello_world():
    return 'Assalamualaikum, ini web server App1 :)'


if __name__ == '__main__':
   app1.run(debug=True, host='0.0.0.0')


