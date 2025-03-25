# class User:
#     def __init__(self, system, user_id, attributes):
#         self.sk = system.keygen(user_id, attributes)
#         self.id = user_id

# class Authority:
#     def __init__(self, system):
#         self.system = system
    
#     def revoke_user(self, user_id):
#         self.system.revoke(user_id)

class User:
    def __init__(self, system, user_id, attributes):
        self.sk = system.keygen(user_id, attributes)
        self.id = user_id

class Authority:
    def __init__(self, system):
        self.system = system
    
    def revoke_user(self, user_id):
        self.system.revoke(user_id)