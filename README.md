# RICE Chart Interactive Visualization

This is a simple, local web application to visualize data from a CSV file using the RICE scoring model.

## How to Use

### 1. Prerequisites
- You need to have Python 3 installed on your system.

### 2. Prepare Your Data
- Make sure your data file is named `ideas_rice.csv` and is located in the same directory as this README file.
- The CSV file must contain at least the following columns: `Key`, `Summary`, `Effort_2`, `Reach_2`, `Impact_2`, `Confidence_2`, `Availability`, `Impact Scope`, `Value Direction`, `OKRs impact`.

### 3. Run the Application
- Open your terminal or command prompt.
- Navigate to this directory (`rice-chart-app`).
- Run the following command:
  ```bash
  python3 start_server.py
  ```
- This will start a local web server. The script should automatically open the application in your default web browser.
- If it doesn't open automatically, please open this URL manually: [http://localhost:8000/rice_chart.html](http://localhost:8000/rice_chart.html)

### 4. Stop the Application
- To stop the server, go back to your terminal window and press `Ctrl+C`.

---
*This application was created with assistance from Gemini.*
