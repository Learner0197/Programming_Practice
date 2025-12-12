import joblib
from flask import Flask, render_template, request
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
app = Flask(__name__)

ps=PorterStemmer()
swords=stopwords.words('english')
def clean_text(sent):
    tokens1=word_tokenize(sent)
    tokens2=[token for token in tokens1 if token.isalpha()]
    tokens3=[ps.stem(token.lower()) for token in tokens2 if token.lower() not in swords]
    return tokens3

classifier = joblib.load('classifier.model')
tfidf = joblib.load('preprocessor.model')
@app.route('/')
def student():
    return render_template('spamdetector.html')

@app.route('/spamfinder', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        data = dict(request.form)
        message = tfidf.transform([data['message']])
        data['result'] = classifier.predict(message)[0]
        return render_template('spamoutput.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)