# Clustering Analysis of Social Mobility Indicators in Los Angeles

## Background
With COVID-19 penetrating much of the US, organizations like hospitals and essential business across communities have been in a frenzy to accommodate local needs and preserve the supply chain. However, despite best efforts, the disease has continued to rise and significantly impacted the economy. In March alone, the economy [lost almost 700,000 jobs.](https://www.cnn.com/2020/04/03/economy/march-jobs-report-coronavirus/index.html) According to a report by CNN, this was the first time the economy lost jobs in a month since September 2010, and the worst month for American jobs since the depths of the Great Recession in March 2009. Given this, there is clearly going to be a high degree of unemployment, even after the immediate effors of the pandemic have been mitigated. In determining how to handle this situation, local communities will need to get a better understanding of how to efficiently help. Looking specifically at employment rate, many other metrics for social mobility are closely tied including individual income, fraction married, incarceration rate, and number of children in a tract. My project focuses on evaluating clustering between employment rate and these factors within Los Angeles to see how different geographic regions are affected. 

## Results
![alt text](https://github.com/PaarthSharma98/Clustering-Analysis-of-Social-Mobility-Indicators-in-Los-Angeles/blob/master/Manipulated%20Data%20and%20Figures/ExcelClusterAnalysis.png)
First looking at a cluster analysis in Excel, I first wanted to evaluate the clustering output with 3 different communities: Bel Air, Culver City, and Compton. These three regions are distinct in terms of culture and community makeup. When looking at the results of the 3 cluster analysis we saw a few insights: Bel Air had the highest normalized Individual Income, Compton had higher incarceration rate, lowest fraction married, and lowest number of children, and Culver City had lowest incarceration rate and highest number of children in a tract.  

A K-Means Cluster Analysis was subsequently performed for 3 clusters using Python. The results are presented below:

![alt text](https://github.com/PaarthSharma98/Clustering-Analysis-of-Social-Mobility-Indicators-in-Los-Angeles/blob/master/Manipulated%20Data%20and%20Figures/z%20Employment%20Ratez%20Fraction%20Married.png)
![alt text](https://github.com/PaarthSharma98/Clustering-Analysis-of-Social-Mobility-Indicators-in-Los-Angeles/blob/master/Manipulated%20Data%20and%20Figures/z%20Employment%20Ratez%20Incarceration%20Rate.png)
![alt text](https://github.com/PaarthSharma98/Clustering-Analysis-of-Social-Mobility-Indicators-in-Los-Angeles/blob/master/Manipulated%20Data%20and%20Figures/z%20Employment%20Ratez%20Individual%20Income%20Normalized.png)
![alt text](https://github.com/PaarthSharma98/Clustering-Analysis-of-Social-Mobility-Indicators-in-Los-Angeles/blob/master/Manipulated%20Data%20and%20Figures/z%20Employment%20Ratez%20Number%20of%20Children%20Normalized.png)

As can be seen above, there are always three disctinct groups within each of the graphs. Given that most the parameters evaluated are co-linear, there was a primarily linear trend in each graph. The clustering nonetheless clarified groups in the negative, 0, and positive range, as expected. The primary thing to note here was in the tail range. Many of these graphs had a region which was almost vertical. In other words, a small band of employment rate had a high variance in its evaluated metric. This is important to understand because especially in a city, it highlights the large degree of diversity across geographic areas. As such, this may make it difficult for local efforts to know where to truly help. A clustering approach such as this makes this approach slightly more efficient by highlighting the groups and regions which are definitely negatively affected in comparison to other regions. 

## Data Analysis Steps
1. Data was collected from [The Opportunity Atlas](https://www.opportunityatlas.org/) for Los Angeles. All datasheets had the following column values: [Tract Name Metric]
2. Data was extracted from each excel into a common spreadsheet for Los Angeles
3. In a new column, I used the IFERROR and INDEX commands to add the tract id of each metric into one column
4. The "Remove Dublicates" excel feature was used to ensure only unique values remained in the column
5. Next, I used VLOOKUP to find and add data pertaining to each tract into a new table. Thus, I had a new table witht he following column values: [Tract Name Metric1 Metric2 Metric3...]
6. I then added new columns next to each metric and normalized all the values by dividing by the max value (found with MAX function)
7. From here, z scores were evaluated and a clsutering analysis was conducted. This used VLOOKUP and STANRADIZE as the main functions for data outputs
8. Once the data was cleaned, a python script was written to analyze the dataset through K-Means Clustering
9. Various libraries were used and K-Means was imported using sklearn
