# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 10:25:32 2019

@author: Columbia Girls
"""
chocolate1 = {"milk":5}
chocolate2 = {"dark":6}
chocolate3 = {"white":8}

chocolatebox = {"milk":5,"dark":6,"white":8}
chocolatebox

student1 = ["Steve",32,"M"]
student2 = ["Lia",28,"F"]
student3 = ["Vin",45,"M"]
student4 = ["Katie",38,"F"]

student1[0]
student1[1]
student1[2]

print(student1,student2,student3,student4)

students = [student1,student2,student3,student4]
students
studentinfo= [["Steve",32,"M"],["Lia",28,"F"],["Vin",48,"M"],["Katie",38,"F"]]

milk1 = {5:"chocolate"}
milk2 = [5,"chocolate"]

import pandas
dir(pandas)

studentdf = pandas.DataFrame(studentinfo,columns=("name","age","gender"))
studentdf

import pandas
dir(pandas)

chocolatebox= [["Milk",5],["Dark",6],["White",8]]
chocolatedf = pandas.DataFrame(chocolatebox,columns=("type","quantity"))
print(chocolatedf)

#go=graphobject

import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go

studentbar = go.Bar(x=studentdf["name"], y = studentdf["age"])
plot([studentbar])



