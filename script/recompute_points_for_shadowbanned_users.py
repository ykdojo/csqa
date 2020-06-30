## Run this with:
# ./manage.py shell < file_name.py

def recompute_points_for_user(user):
  for answer in user.upvoted_answers.all():
    answer.update_points()
    answer.user.update_points()
  for answer in user.downvoted_answers.all():
    answer.update_points()
    answer.user.update_points()

from users.models import User
users = User.objects.filter(is_shadow_banned=True)

for user in users:
  recompute_points_for_user(user)