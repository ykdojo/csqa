## These are just some notes I took to write a script.
from users.models import User

f = User.objects.filter(username='')[0]
count = {}
# who upvoted this user's answers?
for answer in f.answer_set.all():
    for user in answer.upvoted_users.all():
        u = user.username
        if not u in count:
          count[u] = 1
        else:
          count[u] += 1

print(count)

count3 = {}
for answer in f.answer_set.all():
    for user in answer.downvoted_users.all():
        u = user.username
        if not u in count3:
          count3[u] = 1
        else:
          count3[u] += 1

print(count3)

r = User.objects.filter(username='')[0]
# whose answers did this user upvote?
count2 = {}
for answer in r.upvoted_answers.all():
    u = answer.user.username
    if not u in count2:
      count2[u] = 1
    else:
      count2[u] += 1

print(count2)

count4 = {}
for answer in r.downvoted_answers.all():
    u = answer.user.username
    if not u in count4:
      count4[u] = 1
    else:
      count4[u] += 1

print(count4)