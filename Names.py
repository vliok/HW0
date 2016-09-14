import random

CLASSES =  {
    4: [ 'Ayman', 'Shaeq', 'Patrick', 'Yvonne', 'Wilson',
         'Brian', 'Farhan', 'Janet', 'Harry', 'Kevin',
         'Nicholas', 'Jason', 'Yikai', 'Emma', 'Kenneth',
         'Nala', 'Karol', 'Elias', 'Ely', 'Reo', 'Dhiraj',
         'Amy', 'Arvind', 'Nobel', 'Angela', 'Edward',
         'Jonathan', 'Celine', 'Daniel', 'Lindsey', 'Ziyan', 'Elina'],
    8: ['Julian', 'Sebastian', 'Jordan', 'Alan', 'Yuki',
        'Chloe', 'Noah', 'Edvic', 'Jia Qi', 'Shan', 'Rodda',
        'Anya', 'Edmond', 'Asher', 'Kathy', 'Sharon', 'Vincent',
        'Lawrence', 'Sachal', 'Gabriel', 'Jason', 'Daniel',
        'Felix', 'Jacob', 'Bayle', 'Fortune', 'Gio',
        'Kelly', 'William', 'Jordan', 'Haley', 'Henry'],
    9: ['James', 'Vanna', 'Zicheng', 'Quinn', 'Anthony C',
        'Joel', 'Steph', 'Xinhui', 'Richard', 'Misha',
        'Maddie', 'Winston', 'Shariar', 'Nancy', 'Jerry',
        'Michael', 'Stiven', 'Will',  'Olivia', 'Constantine',
        'Jessica', 'Kate', 'Shamaul', 'Max', 'Sarah', 'Anthony L',
        'Brandon', 'Nicole', 'Brian', 'Issac', 'Seiji', 'Lorenz']
} 

def getName( period ):
    if period == 4:
        return random.choice( CLASSES[4] )
    if period == 8:
        return random.choice( CLASSES[8] )
    if period == 9:
        return random.choice( CLASSES[9] )

print getName(4)
