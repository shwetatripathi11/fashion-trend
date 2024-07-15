import pandas as pd

def save_feedback(feedback_data):
    feedback_df = pd.DataFrame([feedback_data])
    feedback_df.to_csv('data/feedback.csv', mode='a', header=False, index=False)
