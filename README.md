# SSI_riskfactors_prediction
📊 Surgical Site Infection (SSI) Risk Prediction in Elective C-Section Patients 


## 🩺 Surgical Site Infection (SSI) Risk Prediction in Elective C-Section Patients
This project predicts the risk of surgical site infection (SSI) in those undergoing elective C-sections by analyzing antenatal and intrapartum risk factors. 
The goal is to identify patients at higher risk for postnatal complications, allowing for targeted wound care interventions.

### 🚀 Project Overview
The project uses:

Python, Pandas, and NumPy to process patient data

RAG (Red, Amber, Green) scoring to categorize risk levels

Streamlit dashboard to visualize and interact with the data

🔥 Key Features
✅ RAG Scoring System:

Antenatal and intrapartum factors are scored separately

Combined score identifies overall risk level

### 📊 Interactive Visualizations:

View risk distribution with clear, colorful charts

Filter patient data by risk level (Low, Moderate, High)


### 🛠️ Dashboard:

Built with Streamlit for easy interaction

Displays patient data, scores, and visualizations

## 🛠️ Tech Stack
-Component	Technology Used
-Programming Language	Python
-Libraries	Pandas, NumPy, Matplotlib, Seaborn, Plotly, Streamlit
-Dataset	Simulated patient data (CSV file)
-Dashboard	Streamlit for interactivity

## 📄 Dataset Overview
The dataset (data/dummy_data.csv) contains the following columns:

* Column	Description	Example Values
* Patient_ID	Unique ID for each patient	1, 2, 3
* Age	Patient's age	32, 41, 29
* BMI	Body Mass Index	27, 35, 31
* Smoker	Smoking status (Yes/No)	Yes, No
* Diabetes	Diabetes status (Yes/No)	Yes, No
* Surgery_Duration	Duration of surgery (minutes)	45, 70, 90
* Blood_Loss	Blood loss during surgery (ml)	300, 1200, 900
* Antibiotics_Given	Whether antibiotics were given (Yes/No)	Yes, No
* RAG_Antenatal	Antenatal RAG score	Green, Amber, Red
* RAG_Intrapartum	Intrapartum RAG score	Green, Amber, Red
* Combined_Risk_Score	Overall SSI risk score	Low, Moderate, High Risk

## ⚙️ Installation & Usage
🛠️ 1️⃣ Clone the repository

git clone <your-repo-link>
cd SSI-Risk-Prediction

## 🔥 2️⃣ Install dependencies

pip install -r requirements.txt

## 📊 3️⃣ Run the Streamlit dashboard

streamlit run app.py

## 🌐 4️⃣ View the dashboard

Open your browser and navigate to:
http://localhost:8501

## 📊 Visualization Samples
✅ Risk Distribution
<img src="visuals/risk_distribution.png" alt="Risk Distribution" width="80%">
✅ RAG Scoring by Category
<img src="visuals/rag_scores.png" alt="RAG Scores" width="80%">

## 🔥 How It Works
🔎 1️⃣ Data Processing
Patient data is loaded and cleaned using Pandas

Antenatal and intrapartum risk factors are scored

# ⚠️ 2️⃣ RAG Risk Scoring Logic
-Green (Low Risk) → Minimal or no risk factors

-Amber (Moderate Risk) → Moderate BMI, smoker, or prolonged surgery

-Red (High Risk) → Severe risk factors (e.g., diabetes, high blood loss, no antibiotics)

## 📊 3️⃣ Visualization
Data is visualized using Matplotlib, Seaborn, and Plotly

The Streamlit dashboard displays the scores and patient data interactively

## ✅ Future Enhancements
🚀 Planned Improvements:

-Expand the dataset with larger clinical data samples (anonymized)

-ML Model Integration: Add a machine learning model to predict infection likelihood

-Enhanced filtering options by patient demographics and surgery details

-Postnatal care recommendations based on risk scores

## 🎯 Key Takeaways
This project demonstrates data analysis, risk scoring, and visualization skills applied to a real-world healthcare problem.
It showcases Python proficiency, clinical knowledge integration, and dashboard development using Streamlit.

### 🤝 Contributing
Want to contribute? Follow these steps:

Fork the repository

Create a new branch (feature/new-feature)
Commit your changes
Push to the branch
Open a pull request

## 📄 License
This project is licensed under the MIT License.

## 📧 Contact
For questions, feedback, or collaboration:
👩‍⚕️ Author: Dawn Hughes
📧 Email: dawnhughesnow@gmail.com
🔗 GitHub: 
