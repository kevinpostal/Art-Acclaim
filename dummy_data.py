from django.core.management import setup_environ
import settings

setup_environ(settings)

from portfolio.models import *
from profiles.models import *
from django.contrib.auth.models import User
from voting.models import Vote

def main():
    #add_portfolios(10000)
    #make_users(10)
    #del_portfolios()
    del_users()
    #make_users_and_art(3,100,True)
    print 1

def vote_on_objects(object,user):
    Vote.objects.record_vote(object, user, +1)

def make_users_and_art(amount=1,art_ammount=1,vote=False):
    del_users()
    for i in range(amount):
        user = User.objects.create_user('test_%s' % (i), '%s@test.com' % (i), 'password')
        user.is_active = False
        user.save()
        profile = Profile(user=user,quote="TEST_TEST")
        profile.save()
        for z in range(art_ammount):
            portfolio = Portfolio(user=user,title='test_%s' % (z),materials="TEST_TEST")
            portfolio.save()
            print z
            if vote == True:
                vote_on_objects(portfolio,user)
        print i    

def make_users(amount=1):
    for i in range(amount):
        user = User.objects.create_user('test_%s' % (i), '%s@test.com' % (i), 'password')
        user.is_active = False
        user.save()
        print i
        
def del_users():
    User.objects.filter(is_active=False).delete()

def del_portfolios():
    Portfolio.objects.filter(materials="TEST_TEST").delete()

def add_portfolios(amount=1):
    id = 1
    user = User.objects.get(id=id)
    for i in range(amount):
        Portfolio(user=user,title="test_%s" % (i) ,materials="TEST_TEST").save() 
        print i
        
        
if __name__ == "__main__":
    main()
