class User:
    def __init__(self, username, email, eco_pal):
        self.username = username
        self.email = email
        self.eco_points = 0
        self.eco_actions = []
        self.learned_issues = []
        self.friends = []
        self.eco_pal = eco_pal

    def log_eco_action(self, action, points):
        self.eco_actions.append((action, points))
        self.eco_points += points

    def learn_issue(self, issue):
        self.learned_issues.append(issue)

    def add_friend(self, friend_email):
        if friend_email in self.eco_pal.users:
            self.friends.append(self.eco_pal.users[friend_email])
        else:
            print("User not found. Please ask them to register first.")

class EcoPal:
    def __init__(self):
        self.users = {}

    def register_user(self, username, email):
        if email not in self.users:
            self.users[email] = User(username, email, self)
            print(f"User {username} registered successfully!")
        else:
            print("Email already in use. Please try logging in.")

    def login(self, email):
        if email in self.users:
            print(f"Welcome back, {self.users[email].username}!")
        else:
            print("User not found. Please register.")

    def show_leaderboard(self):
        sorted_users = sorted(self.users.values(), key=lambda x: x.eco_points, reverse=True)
        print("Leaderboard:")
        for i, user in enumerate(sorted_users, start=1):
            print(f"{i}. {user.username} - Eco Points: {user.eco_points}")

    def show_learned_issues(self, email):
        if email in self.users:
            print(f"{self.users[email].username}'s learned environmental issues:")
            for issue in self.users[email].learned_issues:
                print(f"- {issue}")
        else:
            print("User not found.")

    def show_friends_leaderboard(self, email):
        if email in self.users:
            user = self.users[email]
            sorted_friends = sorted(user.friends, key=lambda x: x.eco_points, reverse=True)
            print(f"{user.username}'s friends' leaderboard:")
            for i, friend in enumerate(sorted_friends, start=1):
                print(f"{i}. {friend.username} - Eco Points: {friend.eco_points}")
        else:
            print("User not found.")

# Sample Usage
ecopal = EcoPal()
ecopal.register_user("Shriyash", "Shriyash@example.com")
ecopal.register_user("AJ", "AJ@example.com")
ecopal.login("Shriyash@example.com")
ecopal.login("charlie@example.com")  # User not found
Shriyash = ecopal.users["Shriyash@example.com"]
Shriyash.log_eco_action("Using reusable bag", 10)
Shriyash.log_eco_action("Cycling instead of driving", 20)
ecopal.show_leaderboard()
ecopal.show_learned_issues("Shriyash@example.com")
Shriyash.add_friend("AJ@example.com")
ecopal.show_friends_leaderboard("Shriyash@example.com")