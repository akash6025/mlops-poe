import pandas as pd
from evidently import Report
from evidently.presets import DataSummaryPreset

data = pd.DataFrame({
    "age": [22, 25, 30, 35, 40],
    "income": [20000, 30000, 40000, 50000, 60000]
})

report = Report([
    DataSummaryPreset()
])

result = report.run(data)

result.save_html("evidently_report.html")

print("Evidently report generated successfully!")