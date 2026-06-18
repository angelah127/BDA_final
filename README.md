## Live Demo
- **Deployed App:** [AutoData-Refiner](https://bdafinal-lhg5bxssv48aas8lkhtduw.streamlit.app/)

## Evidence of Demand
To validate our business model, we conducted targeted mini-surveys with active CV/AV researchers. Read the full questions and qualitative insights here: [Survey Summary](survey_summary.md).

## How to Run Locally

1. Clone this repository and navigate to the directory:
   ```bash
   git clone https://github.com/angelah127/BDA_final.git
   cd BDA_final
   
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

4. Launch the Streamlit application:
   ```bash
   streamlit run app.py

## Architecture Overview
The system architecture traces a direct linear path from ingestion to revenue. It decouples raw mass storage from interactive query delivery, maximizing stateless computational throughput:

[Raw Cloud Storage Logs (GBs)] -> [Vectorized Data Filtering Pipeline] -> [Streamlit UI Dashboard] -> [Value Extraction Metrics] -> [Payment Verification & CSV Export]

## Data Reproducibility (Data Generation)
This application simulates a massive data ingestion process. Upon running app.py for the first time, the script will automatically utilize numpy and pandas to generate a 1,000,000-row raw multi-modal driving dataset (raw_vehicle_logs.csv). This simulates the unstructured infrastructure overhead that the Refiner system targets.
