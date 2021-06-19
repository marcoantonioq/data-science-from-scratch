# Cientistas de Dados Que Você Talvez Conheça

#!/usr/bin/env python3
#coding: utf-8

from collections import Counter

# Users
users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]

# Amigos
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


for user in users:
  user["friends"] = []

for i, j in friendships:
  # isso funciona porque users[i] é o usuário cuja id é i
  users[i]["friends"].append(users[j]) # adiciona i como um amigo de j
  users[j]["friends"].append(users[i]) # adiciona j como um amigo de i

# print(users)

# número médio de conexões
def number_of_friends(user):
  """quantos amigos o usuário tem?"""
  return len(user["friends"]) # tamanho da lista friend_ids
  
## número total de conexões
total_connections = sum(number_of_friends(user) for user in users) 
print(total_connections)
num_users = len(users) 
print(num_users)

avg_connections = total_connections / num_users

#  pessoas mais conectadas
# cria uma lista (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
# lista (user_id, number_of_friends)
# ordená-los do maior para o menor

print(num_friends_by_id)
print(sorted(num_friends_by_id, key = lambda user: user[1], reverse=True))


