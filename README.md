# 🎓 AI-Powered Student Performance Predictor

An interactive Machine Learning application that predicts a student's academic performance category based on academic, family and lifestyle-related information.

## 🚀 Project Overview

This project uses Machine Learning to classify student performance into three categories:

- **Low**
- **Average**
- **High**

The application allows users to enter student details through a Streamlit dashboard and receive an instant prediction.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest Classifier
- Streamlit
- Joblib
- Google Colab
- VS Code

## 📊 Dataset

- Dataset: Student Performance Dataset (UCI Machine Learning Repository)
- Records: 395 students
- Original features: 33
- Selected input features: 19
- Target variable: Performance

### Performance Categories

| Grade (G3) | Category |
|---|---|
| Below 10 | Low |
| 10–14 | Average |
| 15 and above | High |

## ⚙️ Machine Learning Workflow

1. Dataset loading and exploration.
2. Data preprocessing.
3. Creating performance categories.
4. Selecting relevant input features.
5. Encoding categorical variables.
6. Splitting data into training and testing sets.
7. Training a Random Forest Classifier.
8. Evaluating model performance.
9. Saving the trained model using Joblib.
10. Integrating the model into a Streamlit application.

## 📈 Model Performance

- Algorithm: Random Forest Classifier
- Accuracy: 50.63%
- Training/testing split: 80:20
- Number of input features: 19

*Note: This is a beginner educational project. The model has limited predictive performance and should not be used for real-world academic decisions.*

## 💻 Run Locally

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project folder:

```bash
cd Student-Performance-Predictor
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install streamlit pandas numpy scikit-learn joblib
```

Run the application:

```bash
python -m streamlit run app.py
```

## 📁 Project Structure

```text
Student-Performance-Predictor/
│
├── app.py
├── student_performance_model.pkl
├── student_features.pkl
├── README.md
└── requirements.txt
```

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Data preprocessing and feature selection.
- Classification algorithms.
- Model training and evaluation.
- Model serialization using Joblib.
- Building interactive ML applications using Streamlit.
- Integrating a trained ML model into a web application.

## 🔮 Future Improvements

- Experiment with additional classification algorithms.
- Improve model performance through feature engineering.
- Add interactive data visualizations.
- Explore deployment options.

## 👩‍💻 Author

**Bhavya Sri Sai**

B.Tech – Computer Science and Engineering (AI & ML)

Interested in Artificial Intelligence, Machine Learning and building practical technology solutions.

---

⭐ This project represents my journey of learning Machine Learning concepts and implementing them through hands-on development.