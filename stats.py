from aocd.models import default_user
user = default_user()
print(user.get_stats(2022))