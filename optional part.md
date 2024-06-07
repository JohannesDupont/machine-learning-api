### Optional part

**Discuss pros and cons of your chosen algorithms as well as evaluation metrics:**

**Decision Trees and Random Forests:**
Easier to interpret (especially decision trees).
Can handle both numerical and categorical data.
Random Forests reduce the risk of overfitting.
Cons:
Decision Trees can overfit on noisy data.
Random Forests are less interpretable compared to individual decision trees.

**Support Vector Machines (SVM)**
Effective in high-dimensional spaces.
Still effective when the number of dimensions is greater than the number of samples.
Memory efficient.
Cons:
Not suitable for very large datasets.
Not very efficient if the number of features is much greater than the number of samples.

**k-Nearest Neighbors (k-NN)**
Pros:
Simple and easy to implement.
No training phase.
Cons:
Computationally expensive during prediction.
Performance degrades with high-dimensional data.

**evaluation metrics:** \
**1. Accuracy**
Pros: Easy to understand.
Cons: Not suitable for imbalanced datasets.

**2. Precision, Recall, and F1-Score**

Pros: Provide a better understanding of model performance, especially with imbalanced classes.
Cons: More complex to interpret than accuracy.

**3. ROC-AUC**

Pros: Measures the ability of the classifier to distinguish between classes.
Cons: May be less intuitive to understand.


**List libraries in various programming languages that you know or have used that implement those algorithms:**

pycaret\
pytorch/keras\
pyspark/databricks

**Would your setup change if these were Databricks notebooks with Spark compute clusters behind them, written in PySpark?**
 
**Adapting to Databricks and PySpark** \
in PySpark, the following changes would be necessary:

**Data Handling:** \
- Use Spark DataFrames instead of pandas DataFrames for handling data.
- Leverage Spark MLlib for scalable machine learning.
  
**Model Training and Evaluation:**

- Utilize PySpark's MLlib for algorithms such as Random Forest, Gradient-Boosted Trees, and SVM.

**Inference:**

- Using Spark's distributed processing capabilities to handle large-scale inference tasks.


### Big O Notation and Complexity

#### Gaussian Process Classifier (GPC)
- **Time Complexity**: \(O(n^3)\), where \(n\) is the number of training points.
- **Space Complexity**: \(O(n^2)\).

#### Decision Trees
- **Time Complexity**: \(O(n \log n)\), where \(n\) is the number of samples.
- **Space Complexity**: \(O(n \log n)\).

#### Random Forests
- **Time Complexity**: \(O(nt \log n)\), where \(t\) is the number of trees.
- **Space Complexity**: \(O(tn \log n)\).

#### Support Vector Machines (SVM)
- **Time Complexity**: \(O(n^2 \cdot d)\), where \(d\) is the number of features.
- **Space Complexity**: \(O(n^2)\).