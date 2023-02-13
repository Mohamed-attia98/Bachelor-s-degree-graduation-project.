
# Customer analysis and customer seqmentation app
## Overview
Bachelor's degree graduation project. The main goal is to analyze customer transaction data to gain useful insights and then implement a machine learning model to group similar customers together, so the marketing or sales team can reach out to them more effectively.
## Project goals
- Analyze the data and extract valuable insights to enhance business value.
- implementing customer segmentation model based on needs and behaviors, enabling us to target specific groups and thereby boost product sales.
## Steps
1. Data exploration: Trying to understand what the data contains, its size, and its column types.
2. Data processing: Transforming raw data into a well-formed dataset so that data analytics can be applied.
3. Exploratory Data Analysis (EDA) and visualization: Applying data analytics to extract useful insights, then visualizing the insights using visualization tools to help stakeholders make the right decisions.
4. Feature engineering and Feature extraction: Selecting and transforming the most relevant variables from raw data when creating machine learning models, which can improve the performance of ML algorithms.
5. Machine learning model: ML algorithms like K-means and hierarchical clustering are used to cluster customers and dimension reduction algorithms, such as T-SNE, are used to reduce dimensions.
6. Deployment: The last stage is to help stakeholders easily use the ML model via a small website 
## Technical details
- the cleaning and data visualization process was carried out using both python libraries(Pandas ,Numpy, Matplotlib , Seaborn) and Power bi
- deployed machine learning models( KMeans - AgglomerativeClustering - TSNE ) using scikit learn
- Implemented a small website to deploy the ml model using Streamlit
## Demo
- One dashboard of two dashboards we created in Power BI, showing the sales over the months and the top ten products, and the total sales and total sales for each country
 ![Sales Dashboard](https://user-images.githubusercontent.com/82019926/218533618-7e89d85b-2620-45da-bdab-eb1a6c86893a.png)
 - This chart shows the customer segmentation using the agglomerative clustering algorithm after reducing the data dimensions to only two using the tsne algorithm.
 ![image](https://user-images.githubusercontent.com/82019926/218545732-9218de34-c7f7-49d1-bcf0-f4a88472c1f3.png)
 - This is the final product and it is a website built on the kmeans algorithm, it works by outputting the cluster number for the customers after inputting their data.
 ![image](https://user-images.githubusercontent.com/82019926/218544009-bbf412aa-816f-452d-baf2-6bb336b54773.png)
 
 










 







