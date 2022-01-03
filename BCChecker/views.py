from BCChecker import * 


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        birads = request.form['birads']
        age = request.form['age']
        shape = request.form['shape']
        margin = request.form['margin']
        density = request.form['density']
        
        data = [[int(birads), int(age), int(shape), int(margin), int(density)]]
        data = np.array(data)
        
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "static/model", "model.json")
        json_file = open(json_url, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)

        weights_path = os.path.join(SITE_ROOT, "static/model", "model.h5")
        loaded_model.load_weights(weights_path)
        
        loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        prog = loaded_model.predict_classes(data)
        
        if prog == 0:
            prog = "Benign"
        else:
            prog = "Malignant"
        
        return render_template('results.html', result=prog)

app.route('/results/')
def results():
    return render_template('results.html')




