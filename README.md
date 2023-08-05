# Crack Detection Project


## Project Description
Developing an image analysis software to detect cracks from pictures involves 
several steps. Here is a basic image analysis project setup that can detect 
cracks from image. It is only trained with a less amount of data available in Kaggle.


## File Structure
```sh
crack-detection/
├── templates/
├── |── index.html
├── app.py
├── test_data/
├── |── img(1)
├── |── img(2)
├── uploads
├── |── up_img(1)
├── |── up_img(2)
├── crack_detector.py
├── crack_detection_model.ipynb
├── model.pkl
├── requirements.txt
├── .gitignore
```

## Up and Run

```sh
git clone https://github.com/bipsec/crack-detection.git
cd crack-detection
```


## Create a virtual env
```sh
 python -m venv env
 source env/bin/activate
 pip install -r requirements.txt
```

```sh
python app.py
```
You can see the project is running on [http://127.0.0.1:5000](http://127.0.0.1:5000)

# Conclusion
 