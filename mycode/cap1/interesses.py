#!/usr/bin/env python3
#coding: utf-8

from collections import Counter

# Tópicos de Interesse

interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data"),
(10, "Java")
]


# Uma simples forma (e também fascinante) de encontrar os interesses mais
# populares é fazer uma simples contagem de palavras:
# Coloque cada um em letras minúsculas (já que usuários diferentes podem
# ou não escrever seus interesses em letras maiúsculas).
# Divida em palavras.
# Conte os resultados.

words_and_counts = Counter(word
  for user, interest in interests
  for word in interest.lower().split()
)

# print(words_and_counts)
teste = list(word
  for user, interest in interests
  for word in interest.lower().split()
)
#print (teste)

# Bricando com retorn val
print([v 
  for key, val in interests
  for v in val.lower().split()
])
