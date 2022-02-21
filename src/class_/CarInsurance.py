import pickle
import numpy as np
import pandas as pd
import json
import xgboost as xgb
import sklearn


class CarInsurance:
    def __init__(self):

        self.annual_premium = pickle.load(
            open('preparation/annual_premium.pkl', 'rb'))
        self.monthly_premium = pickle.load(
            open('preparation/monthly_premium.pkl', 'rb'))
        self.policy_sales_channel = pickle.load(
            open('preparation/policy_sales_channel.pkl', 'rb'))
        self.age = pickle.load(open('preparation/age.pkl', 'rb'))
        self.region_code = pickle.load(
            open('preparation/region_code.pkl', 'rb'))
        self.vintage = pickle.load(
            open('preparation/vintage.pkl', 'rb'))

    def cleaning(self, df1):

        def lower(x): return x.lower()
        df1.columns = list(map(lower, df1.columns))

        # vehicle demage - str to int
        df1['vehicle_damage'] = df1['vehicle_damage'].apply(
            lambda x: 1 if x == 'Yes' else 0).astype('int64')

        return df1

    def feature_engineering(self, df2):

        # monthly_premium: Monthly amount paid
        df2['monthly_premium'] = df2['annual_premium'].apply(
            lambda x: x / 12).round()

        # age_category: over 30 years old or under and equal 30 years old.
        df2['age_category'] = df2['age'].apply(
            lambda x: 'over_30_years' if x > 30 else 'between_30_years')

        # vintage_category: between 60 day or more than 60 days.
        df2['vintage_category'] = df2['vintage'].apply(
            lambda x: 'between_60_days' if x < 60 else 'more_60_days')

        return df2

    def preparation(self, df5):

        # -- Rescaling
        # annual_premium - Standardization
        df5['annual_premium'] = self.annual_premium.transform(
            df5[['annual_premium']].values)

        # monthly_premium - Standardization
        df5['monthly_premium'] = self.monthly_premium.transform(
            df5[['monthly_premium']].values)

        # -- MinMaxScaler
        # age - MinMaxScaler
        df5['age'] = self.age.transform(df5[['age']].values)

        # vintage - MinMaxScaler
        df5['vintage'] = self.vintage.transform(df5[['vintage']].values)

        # -- Encoding
        # gender - One Hot Encoding
        df5 = pd.get_dummies(df5, prefix='gender', columns=['gender'])

        #  vehicle_age - Label Encoding
        df5['vehicle_age'] = df5['vehicle_age'].map(
            {'< 1 Year': 1, '1-2 Year': 2, '> 2 Years': 3})

        # age_category - Label Encoding
        df5['age_category'] = df5['age_category'].map(
            {'between_30_years': 0, 'over_30_years': 1})

        # vintage_category - Label Encoding
        df5['vintage_category'] = df5['vintage_category'].map(
            {'between_60_days': 0, 'more_60_days': 1})

        # region_code - Target Encoding
        df5.loc[:, 'region_code'] = df5['region_code'].map(self.region_code)

        # policy_sales_channel: Frequency Encoding
        df5.loc[:, 'policy_sales_channel'] = df5['policy_sales_channel'].map(
            self.policy_sales_channel)

        # -- Feature Selection
        cols_selected = ['vintage', 'annual_premium', 'monthly_premium', 'age', 'region_code',
                         'policy_sales_channel', 'vehicle_damage', 'previously_insured', 'vehicle_age']

        return df5[cols_selected]

    def get_prediction(self, model, original_data, test_data):

        # model prediction
        pred = model.predict_proba(test_data)

        # Join prediction into original data
        original_data['score'] = pred[:, 1]

        return original_data.to_json(orient='records', date_format='iso')
