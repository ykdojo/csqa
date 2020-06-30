## These are just some notes I took to write a script.

count = {}
for answer in f.answer_set.all():
    for user in answer.upvoted_users.all():
        u = user.username
        if not u in count:
          count[u] = 1
        else:
          count[u] += 1

count2 = {}
for answer in r.upvoted_answers.all():
    u = answer.user.username
    if not u in count2:
      count2[u] = 1
    else:
      count2[u] += 1
