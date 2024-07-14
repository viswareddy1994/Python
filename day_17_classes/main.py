class User:
    def __init__(self,user_id,user_name):
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0
        
    def follow(self,user):
        user.followers +=1
        self.following +=1
        
    
user_1 = User("001","Viswa")
user_2 = User("002","Gnan")

user_2.follow(user_1)

print(user_1.followers,user_1.following)
print(user_2.followers,user_2.following)