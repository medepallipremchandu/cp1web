import flet as flt
import elements as elmts
import model  as mdl
display = ''

def main(page:flt.Page):

    page.title = "It is Home Page"
    
    inp_ele = elmts.Elements()
    model = mdl.ChurnModel()
   

    def submit(_):
        global display
        gend_y_n = {'Female':0,'Male':1,'No':0,'Yes':1}
        multiple = {'No':0,'No phone service':1,'No internet service':1,'Yes':2}
        others = {'DSL':0,'Fiber optic':1,'No':2,'Month-to-month':0,'One year':1,'Two year':2,'Electronic check':2,'Mailed check':3, 'Bank transfer (automatic)':0,'Credit card (automatic)':1}
        testvalues = [
                     gend_y_n[inp_ele.gender.value],
                     gend_y_n[inp_ele.senior_citizen.value],
                     gend_y_n[inp_ele.partner.value],
                     gend_y_n[inp_ele.dependents.value],
                     int(inp_ele.tenure.value),
                     gend_y_n[inp_ele.phone_service.value],
                     multiple[inp_ele.multiple_lines.value],
                     others[inp_ele.internet_service.value],
                     multiple[inp_ele.online_security.value],
                     multiple[inp_ele.online_backup.value],
                     multiple[inp_ele.device_protection.value],
                     multiple[inp_ele.tech_support.value],
                     multiple[inp_ele.streaming_tv.value],
                     multiple[inp_ele.streaming_movies.value],
                     others[inp_ele.contract.value],
                     gend_y_n[inp_ele.paperless_billing.value],
                     others[inp_ele.payment_method.value],
                     float(inp_ele.monthly_charges.value),
                     float(inp_ele.total_charges.value)
                    ]
        print(testvalues)
        model.Training()
        if(model.istrain==True):
            model.Predicting([testvalues])
            print(model.y_predict)
            if(model.y_predict[0]==0):
                display = 'The Customer is not willing to churn'
            elif(model.y_predict[0]==1):
                 display = 'The Customer is willing to churn'
            page.go('/predicted')
    page.update()
        
    def rout_change(route):
        page.views.clear()
        page.views.append(
            flt.View(
            "/",
            [
                 flt.Text(value="Predicting Customer Churn ",size=50,text_align='center',color="#041944",),
                 flt.Container(height=50),

                 flt.ListView(
                     controls =[
                 flt.Row(
                     controls = [
                          flt.Column
                          (
                              controls = [
                                  inp_ele.gender,
                                  inp_ele.senior_citizen,
                                  inp_ele.partner,
                                  inp_ele.dependents,
                                  inp_ele.tenure,
                                  inp_ele.phone_service,
                                  inp_ele.multiple_lines,
                                  inp_ele.internet_service,
                                  inp_ele.online_security,
                                  inp_ele.online_backup,

                              ],
                              alignment=flt.MainAxisAlignment.CENTER,
                              horizontal_alignment= flt.CrossAxisAlignment.CENTER
                          ),


                 flt.Column(
                     controls = [
                         inp_ele.device_protection,
                         inp_ele.tech_support,
                         inp_ele.streaming_tv,
                         inp_ele.streaming_movies,
                         inp_ele.contract,
                         inp_ele.paperless_billing,
                         inp_ele.payment_method,
                         inp_ele.monthly_charges,
                         inp_ele.total_charges,
                        flt.ElevatedButton(text="Predict",width=250,height=50,bgcolor="#041944",on_click=submit),
                     ],
                 ),

                             
                     ],
                     alignment=flt.MainAxisAlignment.CENTER,
                     vertical_alignment= flt.CrossAxisAlignment.CENTER
                 )
                     ],
                     auto_scroll=True,
                     expand=1, 
                     spacing=10, 
                     padding=20,
                 ),
                
            ],
            vertical_alignment='top',
            horizontal_alignment='center',
            padding=50,
            bgcolor="#6BA5FF",
            )
        )    
            
        if page.route == '/predicted':
             page.views.append(
                  flt.View(
                       '/predicted',
                       [       
                        flt.Text(value= display,size=50,text_align='center',color="#041944",),
                        ],

                        vertical_alignment='center',
                        horizontal_alignment='center',
                        padding=50,
                        bgcolor="#6BA5FF",
                    )
                )
        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    
    page.on_route_change=rout_change    
    page.on_view_pop=view_pop
    page.go(page.route)
    
    
flt.app(target=main,view=flt.WEB_BROWSER)
