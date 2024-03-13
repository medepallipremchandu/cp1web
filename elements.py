import flet as flt
class Elements():
    def __init__(self):
            self.gender =  flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='Gender',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in ['Male','Female']])
                         
            self.senior_citizen = flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='SeniorCitizen',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in ['Yes','No']])

            self.partner = flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='Partner',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in ['Yes','No']])

            self.dependents = flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='Dependents',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in ['Yes','No']])

            self.tenure = flt.TextField(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,text_size=10,label_style=flt.TextStyle(color="white"),label="Tenure",)

            self.phone_service = flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='PhoneService',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in ['Yes','No']])
                         
            self.multiple_lines = flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='MultipleLines',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in ['Yes','No','No phone service']])

            self.internet_service = flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='InternetService',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in ['DSL', 'Fiber optic','No']])

            self.online_security =  flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='OnlineSecurity',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in ['Yes','No','No internet service']])

            self.online_backup =  flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='OnlineBackup',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in ['Yes','No','No internet service']])
            
            self.device_protection = flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='DeviceProtection',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in ['Yes','No','No internet service']])

            self.tech_support = flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='TechSupport',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in ['Yes','No','No internet service']])

            self.streaming_tv = flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='StreamingTV',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in ['Yes','No','No internet service']])

            self.streaming_movies =flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='StreamingMovies',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in ['Yes','No','No internet service']])

            self.contract = flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='Contract',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in ['Month-to-month','One year','Two year']])

            self.paperless_billing =  flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='PaperlessBilling',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in ['Yes','No']])

            self.payment_method = flt.Dropdown(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,label='PaymentMethod',text_size=10,label_style=flt.TextStyle(color="white"),options=[flt.dropdown.Option(i) for i in  ['Electronic check','Mailed check', 'Bank transfer (automatic)',
                         'Credit card (automatic)']])

            self.monthly_charges = flt.TextField(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,text_size=10,label_style=flt.TextStyle(color="white"),label="MonthlyCharges",)

            self.total_charges = flt.TextField(bgcolor="#041944",filled=True,color="#6BA5FF",width=250,height=50,text_size=10,label_style=flt.TextStyle(color="white"),label="TotalCharges",)


        