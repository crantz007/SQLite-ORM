from peewee import *

db= SqliteDatabase('records.sqlite')

class recordman(Model):
    name = CharField()
    country = CharField()
    number_of_catches = IntegerField()

    class Meta :
        database = db

    def __str__(self):
        return f'{self.name} from {self.country} {self.number_of_catches} number of catches'

db.connect()
db.create_tables([recordman])

    # create record objects and call function
print('\nCreate and save 4 records')

janne_Mustonen = recordman(name= "Janne Mustonen",country="Finland",number_of_catches=98)
janne_Mustonen.save()
ian_stewart = recordman(name="Ian Stewart", country="Canada",number_of_catches=94)
ian_stewart.save()
aaron_gregg = recordman(name="Aaron Gregg", country="Canada", number_of_catches=88)
aaron_gregg.save()
chad_taylor = recordman(name="Chad Taylor", country="USA", number_of_catches=78)
chad_taylor.save()

print('\nFind all holders')
holders = recordman.select()
for holder in holders:
    print(holder)

lists_of_holders = list(holders)


