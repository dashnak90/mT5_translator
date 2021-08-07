from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html', title='Welcome  to  mT5-Translator')

@app.route('/translate',methods=["POST"])
def translate():
    input = dict(request.form)

    TEXT=list(input.values())[1]
    FROM=list(input.keys())[0]
    TO=list(input.keys())[2]


    input_text = str(TEXT)
    language = '<'+str(FROM)+'>'

    print(language,input_text)

#    input_ids = encode_input_str(
#        text = language+input_text,
#        tokenizer = tokenizer,
#        seq_len = max_seq_len
#        )
#    input_ids = input_ids.unsqueeze(0).cuda()
#    print(input_ids)
#    output_tokens = model.generate(input_ids,num_beams=10, num_return_sequences=1, length_penalty = 1, no_repeat_ngram_size=2)
#    
#    TRANS=tokenizer.decode(output_tokens[0], skip_special_tokens=True)
    
    TRANS='your translation'


    return render_template('translate.html', text=input_text, trans=TRANS )





if __name__ == "__main__":
    app.run(debug=True, port=5000)