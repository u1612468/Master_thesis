# Data Analysis

# Basic Analysis
We analyze features crawled from the Internet and compare them in different sectors. Note here we mainly use structured data.

# Association Rules (Apriori Algorithm)
This file "association_rules.ipynb" analyzes the association rules among variables including 'salary_label', 'exp_en', 'eduBack_en', 'scale_en','Comp_en', 'city_en', 'industry_category' and 'Comp_en'. It examines the relationships among job postings' characteristics in two sectors. It highlights significant associations related to salary range, education requirement, industry category, work experience requirement, and company location. By categorizing positions and applying the Apriori algorithm, association rules are generated to quantify the connections between attributes.

# Word Could
The file "word_cloud.ipynb" outputs two word cloud graphs for each industry. The data is imported from "fin_skills_counts_top.csv" and "it_skills_counts_top.csv" and those two files are generated in "skills.ipynb". The generated word cloud displays the most frequent skills (top 50) required in two sectors.

# Co-occurrence Table
The file "skills.ipynb" outputs two co-occurrence tables. The data is imported from Finance_cleaned_file.csv and Internet_cleaned_file.csv, which is compressed in Cleaned_file.zip. We visualized the connections between these skills in two sectors by constructing a co-occurrence matrix. The weight assigned to each edge in the co-occurrence table represents the frequency of two skills appearing together in job postings, indicating a strong association.

# Questionnaire 
The file "Questionnaire_analyze.ipynb" analyzes the questionnaire data. The data is imported from Questionnarie_Clean_Manually.csv. To complement the perspective of job seekers, we employed an online questionnaire to investigate recruitment discrimination in the actual hiring process.
