"""
November 2016
@author Charlotte Alexandra Wilson

"""

import arff
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

labels = ["ID","AFP","Input","Output","Enquiry","File", "Interface", "Added", "Changed", "Deleted", "PDR_AFP", "PDR_UFP","NPDR_AFP","NPDU_UFP", "Resource","Dev Type", "Duration", "N_effort"];

