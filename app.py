from flask import Flask,render_template,request
import os
import pickle

app = Flask(__name__)


def detact(x):
    with open("model.pkl","rb") as model:
        model_data = pickle.load(model)
    
    with open("vectorizer.pkl","rb") as model:
        vector_data = pickle.load(model)
        
    v= vector_data.transform([x])
    pre = model_data.predict(v)
    
    if pre == 0:
        return f"This content appears to be fake. Please verify from reliable sources."
    else:
        return f"This content appears to be genuine.However, we recommend verifying it with trusted sources."        
    
        
# end def

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/Analyze_News",methods=['GET','POST'])
def analyze():
    user = request.form.get("user_input")
    dec = detact(user)  
    return render_template('index.html',result=dec)
    
    

port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)


