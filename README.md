# ApexPlanet - Data Storytelling & Statistical Validation

![GitHub repo size](https://img.shields.io/github/repo-size/SricharanAsr/ApexPlanet-Task4?style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/SricharanAsr/ApexPlanet-Task4?style=for-the-badge)
![GitHub license](https://img.shields.io/github/license/SricharanAsr/ApexPlanet-Task4?style=for-the-badge)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge&logo=python)

![About Us](about_us.png)

## 📊 Overview
This repository contains the complete deliverables for **Task 4** of the ApexPlanet Data Analytics project. Our mission was to synthesize multi-phase analysis into a cohesive business narrative and validate key findings using rigorous statistical methods.

## 🛠 Built With
*   **Python 3.10+**: Core analysis engine.
*   **Pandas**: Data manipulation and wrangling.
*   **SciPy**: Statistical hypothesis testing (Welch's T-Test).
*   **HTML5/CSS3**: Interactive stakeholder presentation deck.
*   **GitHub Actions**: Automated CI pipeline for linting and testing.

## 📂 Project Structure

### 1. Statistical Validation
- **[statistical_test.py](statistical_test.py)**: Refactored Python script performing Welch's T-test on Average Order Value (AOV).
- **[test_statistical_test.py](test_statistical_test.py)**: Robust unit tests ensuring calculation accuracy.
- **[hypothesis_testing_report.md](hypothesis_testing_report.md)**: Full report on the statistical significance of age-group spending.

### 2. Business Narrative
- **[data_story.md](data_story.md)**: A structured storytelling document covering the analytical journey.
- **[presentation_script.md](presentation_script.md)**: A professionally drafted script for executive briefings.

### 3. Stakeholder Deliverables
- **[final_presentation.html](final_presentation.html)**: A premium, interactive presentation deck with dynamic visualizations.

## 🚀 Key Insights
*   **Electronics Dominance**: Revenue is primarily driven by high-ticket Electronics items ($104K+).
*   **Segment Muscle**: The 35-44 age segment provides the highest immediate value.
*   **Validated Growth**: Confirmed a statistically significant 30% gap in spending between key demographics.

## ⚙️ Getting Started

### Installation
```bash
git clone https://github.com/SricharanAsr/ApexPlanet-Task4.git
cd ApexPlanet-Task4
pip install -r requirements.txt
```

### Running Analysis
```bash
python statistical_test.py
```

### Running Tests
```bash
pytest
```

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

---
*Developed as part of the ApexPlanet Internship Program.*
