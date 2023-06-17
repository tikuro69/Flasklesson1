from flask import Flask, request, render_template, redirect, url_for, jsonify
import json
import uuid

app = Flask(__name__)

results_dict = {}  # 結果を保存するための辞書


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
  data = request.get_json()

  # ここでOpenAIにデータを送信するロジックを追加します
  # この例では、結果として独自のIDを生成します。
  # result_id = "123"
  result_id = str(uuid.uuid4())
  # ここで設定ファイルを生成する処理を書く。
  # 以下は単純な例で、実際には適切な設定ファイルを生成するロジックに書き換える必要があります。
  config = f"""
        hostname {data["Hostname"]}
        ip address {data["ManagementIP"]} {data["Netmask"]}
        ip default-gateway {data["DefaultGateway"]}
        enable secret {data["EnablePassword"]}
        username admin secret {data["SecretPassword"]}
    """
  results_dict[result_id] = config  # 結果を保存する

  # return json.dumps({"result_id": result_id}), 200
  return jsonify({'result_id': result_id})  # 結果のIDをクライアントに返す


@app.route('/results/<result_id>')
def results(result_id):
  # 実際のアプリケーションでは、result_idに基づいてデータベースから結果を取得するでしょう。
  # この例では、結果をハードコーディングします。
  # result = {
  #   "input1": "Test Input 1",
  #   "input2": "Test Input 2",
  #   "input3": "Test Input 3"
  # }
  result = results_dict.get(result_id)
  if result is None:
    return redirect(url_for('index'))  # 結果が見つからない場合はトップページにリダイレクトする
  return render_template('results.html', result=result)

  return render_template('results.html', result=result)  # 結果をテンプレートに渡します


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
