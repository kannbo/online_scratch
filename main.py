from bottle import get, post, request,run,route
import scratchattach as scratch3,uuid

account={"nantokamaru":{"name":"aaa","password":"aaa"}}
@get('/')
def login():
        return '''
<title>scachクラウド変数改造</title>
<h2>キー生成</h2>
        <form action="/" method="post">
            名前を入力: <input name="username" type="text" />
            パスワード: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
<a href="/cloud">変更する</a>
        '''
@post('/')
def do_login():
    global account
    uuid4=str(uuid.uuid4())
    account[str(uuid4)]={"name":request.forms.get('username'),"password":request.forms.get('password')}
    print(account)
    try:
        session = scratch3.login(account[uuid4]["name"],account[uuid4]["password"])
        return f"<h2>キーを生成しました</h2>{uuid4}"#""""<meta http-equiv="refresh" content="0;URL=/cloud">"""
    except:
        return """<h1>パスワードが違います<meta http-equiv="refresh" content="3;URL=/">"""
@get('/cloud')
def cloud_get():
    return """        <form action="/cloud" method="post">
            変数名: <input name="name" type="text" /><br>
            作品のID: <input name="id" type="number" /><br>
            変更する数字: <input name="num" type="number" /><br>
            キー: <input name="key" type="text" /><
            <input value="変更" type="submit" />
        </form>"""
@post("/cloud")
def cloud_post():
    global account
    try:
        session = scratch3.login(account[request.forms.get('key')]["name"],account[request.forms.get('key')]["password"])
        conn = session.connect_cloud(str(request.forms.get('id')))
        conn.set_var(request.forms.get('name'),str(request.forms.get('num')))
        return "変更しました<title>変更完了</title>"
    except Exception as e:
        print(e,"\n",account)
        return "変更失敗しました<title>変更失敗</title>"
@route("/request")
def requ_1():
    return """
<title>リクエストガイド</title>
<h1>リクエストプロパティ</h1>
<h2>作成中</h2>"""
@route("/request/key/<key>")
def requ_2(key):
    global account
    try:
            return str(account[key])
    except:
            aaa={"name":"no user","password":"no password"}
            return str(aaa)
@route("/request/delete/<key>")
def requ_3(key):
        global account
        try:
                del account[key]
                return "delete"
        except:
                return "not delete"
run(host='localhost', port=8080, debug=True)
