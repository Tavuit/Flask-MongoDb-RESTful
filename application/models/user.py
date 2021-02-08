from manager import db
#Defind Model
class User(db.Document):
    account_number = db.IntField()
    balance = db.IntField()
    firstname = db.StringField()
    lastname = db.StringField()
    age = db.IntField()
    gender = db.StringField()
    address = db.StringField()
    employer = db.StringField()
    email = db.StringField()
    city = db.StringField()
    state = db.StringField()

    def to_json(self):
        return {
            'account_number': self.account_number,
            'balance': self.balance,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'age': self.age,
            'gender': self.gender,
            'address': self.address,
            'employer': self.employer,
            'email': self.email,
            'city': self.city,
            'state': self.city
        }
