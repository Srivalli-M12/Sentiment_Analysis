# Sentiment_Analysis
## Description
This project is a **web-based sentiment analysis tool** designed for business insights. It takes **user-inputted text (single sentence or multiple)** and performs **real-time sentiment analysis** using **VADER (Valence Aware Dictionary and Sentiment Reasoner)**. The results are visually represented using **interactive graphs powered by Plotly**, making sentiment trends easy to interpret.

## Features
- **Real-time sentiment analysis** based on business-related text.
- **Dynamic visualization** of sentiment scores using **Plotly**.
- **Interactive front-end** built with **HTML, CSS, and JavaScript**.
- **Backend powered by Flask**, handling API requests efficiently.
  
## Tech Stack
- **Backend:** Python, Flask, VADER Sentiment Analysis
- **Frontend:** HTML, CSS, JavaScript
- **Visualization:** Plotly for dynamic graph representation

## Project Structure
|-static 
  ->style.css
  ->script.js
|-templates
  ->index.html
|-app.py

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/SrivalliMannem/Sentiment_Analysis.git
   ```
2. **Navigate to the project folder**:
   ```bash
   cd Sentiment_Analysis
   ```
3. **Install dependencies**:
   ```bash
   pip install flask vaderSentiment plotly
   ```
4. **Run the Flask server**:
   ```bash
   python app.py
   ```
## How to Use
- Open the application in your browser .
- Enter a business-related sentence or multiple sentences in the text box.
- Click the "Analyze" button to perform sentiment analysis.
- The app will display:
   - Sentiment scores (Positive, Neutral, Negative percentages).
   - An interactive bar chart visually representing sentiment distribution.
- Explore different texts to understand variations in sentiment


## License
This project is licensed under the MIT License. Feel free to modify and improve!
### Contact

For any queries, suggestions, or collaborations, feel free to reach out:[GitHub](https://github.com/SrivalliMannem)

