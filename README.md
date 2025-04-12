# SSI_riskfactors_prediction
Surgical Site Infection (SSI) Risk Prediction in Elective C-Section Patients 


##  Surgical Site Infection (SSI) Risk Prediction in Elective C-Section Patients
This project predicts the risk of surgical site infection (SSI) in those undergoing elective C-sections by analyzing antenatal and intrapartum risk factors. 
The goal is to identify patients at higher risk for postnatal complications, allowing for targeted wound care interventions.

### Project Overview
The project uses:

Python, Pandas, and NumPy to process patient data

RAG (Red, Amber, Green) scoring to categorize risk levels

Streamlit dashboard to visualize and interact with the data

Key Features
RAG Scoring System:

Antenatal and intrapartum factors are scored separately

Combined score identifies overall risk level

### Interactive Visualizations:

View risk distribution with clear, colorful charts

Filter patient data by risk level (Low, Moderate, High)


### 🛠 Dashboard:

Built with Streamlit for easy interaction

Displays patient data, scores, and visualizations

## Tech Stack
-Component	Technology Used
-Programming Language	Python
-Libraries	Pandas, NumPy, Matplotlib, Seaborn, Plotly, Streamlit
-Dataset	Simulated patient data (CSV file)
-Dashboard	Streamlit for interactivity

##  Dataset Overview
The dataset (data/dummy_data.csv)   will contain the following columns:

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

Initial commit has reduced tabel to testcsv file

Here are step-by-step instructions that you can add to your GitHub README file, so others can easily access and view your Streamlit app:

---

## How to View the Streamlit App Locally

Follow these steps to run and view the Streamlit app on your local machine.

### Prerequisites
Before you start, make sure you have the following installed:

- **Python** (preferably version 3.6 or later)
- **Streamlit**: A Python library for creating interactive apps

### Step 1: Clone the Repository
First, you need to clone this repository to your local machine. Open your terminal (Command Prompt or PowerShell for Windows, Terminal for macOS/Linux) and run the following command:

```bash
git clone https://github.com/your-username/SSI_riskfactors_prediction.git
```

Replace `your-username` with your GitHub username.

### Step 2: Navigate to the Project Directory
Once the repository is cloned, navigate to the project directory by running:

```bash
cd SSI_riskfactors_prediction
```

### Step 3: Set Up a Virtual Environment (Optional but Recommended)
It's good practice to set up a virtual environment to manage dependencies. To create and activate a virtual environment, run:

For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies
Install the required dependencies for the project by running:

```bash
pip install -r requirements.txt
```

If there is no `requirements.txt` file, you can manually install Streamlit and any other dependencies by running:

```bash
pip install streamlit
```

### Step 5: Run the Streamlit App
To launch the Streamlit app, run the following command:

```bash
streamlit run app.py
```

After running this command, Streamlit will start the app locally.

### Step 6: Access the App in Your Browser
Once the app is running, you will see output similar to:

```
You can now view your Streamlit app in your browser.

Local URL:  http://localhost:8501
Network URL: http://192.168.0.202:8501
```

- Open your browser and navigate to [http://localhost:8501](http://localhost:8501).
- You should now be able to view and interact with the app.

### Optional: Access the App on a Local Network
If you'd like to access the app from another device on the same network, use the **Network URL** provided by Streamlit (e.g., `http://192.168.0.202:8501`). Ensure that both devices are connected to the same Wi-Fi network.

---

## How to Stop the Streamlit App
To stop the app, press `Ctrl + C` in the terminal where the app is running. This will terminate the Streamlit server.

---

### Troubleshooting
If you encounter issues, here are some tips to resolve common problems:

1. **Streamlit is not installed**: Make sure you installed Streamlit by running `pip install streamlit`.
2. **Permission issues**: If you encounter permission issues, try running the terminal as an administrator (Windows) or using `sudo` (macOS/Linux).
3. **App is not showing up**: Make sure your firewall allows traffic on port 8501 or try accessing using the network URL.

---


## Visualization Samples
Risk Distribution
<img src="visuals/Screenshot 2025-04-12 172826.png">
RAG Scoring by Category
<img src="visuals/rag_scores.png" alt="RAG Scores" width="80%">

##  How It Works
Data Processing
Patient data is loaded and cleaned using Pandas

Antenatal and intrapartum risk factors are scored

# RAG Risk Scoring Logic
-Green (Low Risk) → Minimal or no risk factors

-Amber (Moderate Risk) → Moderate BMI, smoker, or prolonged surgery

-Red (High Risk) → Severe risk factors (e.g., diabetes, high blood loss, no antibiotics)

## Visualization
Data is visualized using Matplotlib, Seaborn, and Plotly

The Streamlit dashboard displays the scores and patient data interactively

## Future Enhancements
🚀 Planned Improvements:

-Expand the dataset with larger clinical data samples (anonymized)

-ML Model Integration: Add a machine learning model to predict infection likelihood

-Enhanced filtering options by patient demographics and surgery details

-Postnatal care recommendations based on risk scores

## Key Takeaways
This project demonstrates data analysis, risk scoring, and visualization skills applied to a real-world healthcare problem.
It showcases Python proficiency, clinical knowledge integration, and dashboard development using Streamlit.

### Contributing
Want to contribute? Follow these steps:

Fork the repository

Create a new branch (feature/new-feature)
Commit your changes
Push to the branch
Open a pull request

## 📧 Contact
For questions, feedback, or collaboration:
Contact me
