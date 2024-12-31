# filename: refined_plot.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV 파일 다운로드
url = "https://github.com/mwaskom/seaborn-data/raw/master/titanic.csv"
data = pd.read_csv(url)

# 'age'의 결측치를 평균값으로 채우기 (경고 없이 안전하게 처리)
data['age'] = data['age'].fillna(data['age'].mean())

# 다른 결측치 처리 방법 예시:
# data['age'] = data['age'].fillna(data['age'].median())  # 중앙값으로 채우기
# data['age'] = data['age'].fillna(30)  # 특정 값으로 채우기

# 'pclass'를 범주형으로 변환
data['pclass'] = data['pclass'].astype('category')

# seaborn 스타일로 설정
sns.set(style="whitegrid")

# 'age'와 'pclass'의 관계를 박스플롯으로 시각화
plt.figure(figsize=(10, 6))
sns.boxplot(x='pclass', y='age', hue='survived', data=data, palette="Set2", dodge=True)
plt.title('Age Distribution by Pclass and Survival', fontsize=16)
plt.xlabel('Pclass', fontsize=14)
plt.ylabel('Age', fontsize=14)
plt.legend(title='Survived', loc='upper right', fontsize=12)
plt.grid(True)

# 차트를 파일로 저장
plt.savefig('refined_age_pclass_relationship.png')
plt.close()