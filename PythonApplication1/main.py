@app.route('/username')
def home():
    return '<hi>Hello World</hi>' % username
if __name__== '__name__':
    app.run()