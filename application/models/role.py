from manager import db

class Role(db.Document):
    email = db.EmailField()
    role = db.StringField()

    def to_json(self):
        return {
            'role': self.role
        }

    def get_role(self, email):
        role = Role.objects(email=email).first()
        if not role:
            return {
                'role': 'user'
            }
        return role.to_json()