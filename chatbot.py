import nltk
from nltk.chat.util import Chat, reflections

pairs = [
  [
    r"what is data science",
    ["Data science is the study of data to extract meaningful insights for business. It combines principles from mathematics, statistics, and computer engineering to analyze large amounts of data."],
  ],
  [
    r"why is data science important",
    ["Data science is important because it helps organizations generate meaning from data."],
  ],
  [
    r"what are machine learning algorithms",
    ["Machine learning algorithms enable computers to learn from data by building models and making predictions."],
  ],
  [
    r"what is deep learning",
    ["Deep learning refers to artificial neural networks that simulate the function of the human brain to recognize patterns in data."],
  ],
  [
    r"what is KNN algorithm",
    ["KNN or K-Nearest Neighbours is a type of supervised machine learning algorithm used to classify new data points based on distance measure (Euclidean, Manhattan, etc.) between features in the training set."],
  ],
  [
    r"what is SVM algorithm",
    ["SVM or Support Vector Machines is a type of supervised machine learning algorithm that constructs a hyperplane in high-dimensional space to separate classification classes with maximum margin."],
  ],
  [
    r"what is decision tree algorithm",
    ["Decision tree algorithm is a type of supervised machine learning algorithm that builds a flowchart-like model of decisions and their possible consequences (outcomes) using a set of rules based on features in the training set."],
  ],
  [
    r"what is logistic regression algorithm",
    ["Logistic regression algorithm is a type of supervised machine learning algorithm used to predict the probability of categorical dependent variables based on independent variables."],
  ],
  [
    r"what is random forest algorithm",
    ["Random forest algorithm is a type of supervised machine learning algorithm that builds multiple decision trees and aggregates their predictions to improve the accuracy and avoid overfitting."],
  ],
  [
    r"what is K means clustering",
    ["K-means clustering is a type of unsupervised machine learning algorithm used to group data points into K clusters based on their similarity to centroid points."],
  ],
  [
    r"what is hierarchical clustering",
    ["Hierarchical clustering is a type of unsupervised machine learning algorithm used to group data points into nested clusters based on their similarity to each other."],
  ],
  
  # Add more pairs/questions/answers as per your needs
  
]

chatbot = Chat(pairs, reflections)
chatbot.converse()