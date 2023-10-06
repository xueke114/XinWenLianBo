import pandas as pd


durations = pd.read_csv("duration.csv")
anchors = pd.read_csv("anchors.csv")

# 检查主播的拼写是否正确
condition_female_anchors = durations["anchorA"].isin(anchors["name"])
condition_male_anchors = durations["anchorB"].isin(anchors["name"])

if condition_female_anchors.all() and condition_male_anchors.all():
    print("success")

