##Ensures that the Block class functions properly

from block import Block

transaction1 = {
    'amount' : '30',
    'sender' : 'Bob',
    'reciever' : 'Sarah'
}

transaction2 = {
    'amount' : '45',
    'sender' : 'Steve',
    'reciever' : 'Jobs'
}

transaction3 = {
    'amount' : '85',
    'sender' : 'Bill',
    'reciever' : 'Gates'
}

transaction4 = {
    'amount' : '25',
    'sender' : 'Alice',
    'reciever' : 'Timmy'
}

mempool = [transaction1,transaction2,transaction3,transaction4]

# My new Transaction
myTransaction = {
    'amount' : '55',
    'sender' : 'George',
    'reciever' : 'Bob'
}

mempool.append(myTransaction)

