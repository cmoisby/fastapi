import pandas as pd
 
data = pd.read_csv ('https://dst-de.s3.eu-west-3.amazonaws.com/fastapi_fr/questions.csv' ,sep=','  )

dict = []

question = [{
            "question" : "question",
            "subject" :  "question",
            "use" :  "question",
            "correct" :  "question",
            "responseA" :  "question",
            "responseB" : "question",
            "responseC" : "question",
            "responseD" : "question",
            "remark" :  "question",
            }]

dict.append(question)
print(dict)



