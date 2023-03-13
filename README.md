# Master_thesis 

# The Analysis of Internet and Finance Industries Recruitment Criteria Based on Data Mining: A Study of Job Postings on Zhilian Recruitment Platform and a Survey on Hiring Discrimination in China.

Crawl data from the Boss Direct recruitment website https://www.zhipin.com/

Targeted crawl objects are restricted to 5 cities with the most job opportunities in China
Beijing, Shanghai, Guangzhou, Shenzhen, Hangzhou

# Abstract

In the new era, there are many recruitment websites, among which Zhilian has a large market share and popularity. In this paper, we choose this website as the source of data and collect all search keywords based on the Internet and financial industry, provided by the website, in five top cities (with the most number of job opportunities) in China, Beijing, Shanghai, Guangzhou, Shenzhen, and Hangzhou. We extract 9 features, such as job information, including name and salary, company information including its name, city, type, and size as well as job requirements, including work experience, and educational background. The data were de-weighted and processed with missing values, and finally, 10w+ data were expected to be obtained. For the structured data to be normalized, to facilitate the subsequent statistics, to draw the market portrait of each feature, to derive the overall characteristics of the post; for the unstructured data, mainly including the processing of Chinese text, first of all, using the features to extract the job name, based on Python software, jieba word separation, remove the stop words and other pre-processing. This paper uses the LDA topic model for topic clustering based on the skills required for the job and draws the number of topics - Perplexity curve to determine the number of topics, and finally divides the topics into () categories to get the proportion of different categories of job requirements, as well as different job experience, education, and salary levels; at the same time, word frequency statistics are conducted for job requirements. In order to observe the connection between different skills more intuitively, we construct a keyword co-occurrence matrix and draw its network diagram; we select keywords with certain skill characteristics in the job requirements, conduct skill correlation analysis, and analyze and compare them horizontally and vertically respectively; we construct association rules based on Apriori algorithm, and mine various types of positions and different attributes (experience, education, company type, region, etc.), and compare the similarities and differences between the two industries horizontally; in order to further explore the hidden laws of recruitment information. (The results of the study show that ) In addition, this paper will conduct a survey study for the Chinese recruitment market through questionnaires to explore whether recruitment discrimination exists, including but not limited to gender, age, education, health, etc. Ultimately, this paper aims to reveal industry characteristics and trends through the analysis of recruitment information in the Internet and finance sectors and provide useful references and suggestions for job seekers and recruiters.

# Overleaf Link (keep updated): 
https://www.overleaf.com/read/vykdwytvhpct
# Thesis Progress Link (keep updated): 
https://docs.google.com/document/d/1nYcfhWtffh1yMhV30Wpk9Xdv-qsBjNWb0bGTDD6g_i0/edit?usp=sharing

