
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

# Reference data
reference_data = pd.DataFrame({
    "num1": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    "num2": [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
})

# Current data
current_data = pd.DataFrame({
    "num1": [110, 120, 130, 140, 150, 160, 170, 180, 190, 200],
    "num2": [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
})

# Generate drift report
report = Report([DataDriftPreset()])

result = report.run(
    reference_data=reference_data,
    current_data=current_data
)

result.save_html("drift_report.html")

print("Drift report generated successfully!")