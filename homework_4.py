from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('homework4.html')


## API 역할을 하는 부분

@app.route('/orders', methods=['POST'])
def write_orders():
    name_receive = request.form['name_give']
    option_receive = request.form['option_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']
    print(name_receive, option_receive, address_receive, number_receive)

    # DB에 삽입할 order 만들기
    order = {
        'name': name_receive,
        'option': option_receive,
        'address': address_receive,
        'number': number_receive
    }

    # orders에 order 저장하기
    db.orders.insert_one(order)

    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 완료되었습니다.'})


@app.route('/orders', methods=['GET'])
def read_orders():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)