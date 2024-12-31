# filename: plot_age_pclass_relationship.py
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 다운로드
url = "https://github.com/mwaskom/seaborn-data/raw/master/titanic.csv"
data = pd.read_csv(url)

# 'age'와 'pclass'의 관계를 시각화
plt.figure(figsize=(10, 6))
plt.scatter(data['pclass'], data['age'], alpha=0.5)
plt.title('Relationship between Age and Pclass')
plt.xlabel('Pclass')
plt.ylabel('Age')
plt.grid(True)

# 차트를 파일로 저장
plt.savefig('age_pclass_relationship.png')
plt.close()