nominee_1 = input('Enter the name of first nominee: ')
nominee_2 = input('Enter the name of second nominee: ')

nm1_votes = 0
nm2_votes = 0

voter_id = [123,456,789]
no_of_voters = len(voter_id)

while True:
    voter = int(input('Enter your voter id: '))

    if voter in voter_id:

        voter_id.remove(voter)
        print('-----------------------------------')
        print('Welcome to the online voting system')
        print('-----------------------------------')
        print('----------------------------------------------------------------')
        print('Nominees for the election are', nominee_1 +' ''and'' ' +nominee_2)
        print('To give vote to', nominee_1, 'Press 1')
        print('To give vote to', nominee_2, 'Press 2')
        print('----------------------------------------------------------------')
        vote = int(input('Enter your precious vote: '))
        if vote==1:
            nm1_votes +=1
            print('YOu voted for', nominee_1)
            print('Thank you for voting.')
        elif vote==2:
            nm2_votes +=1
            print('You voted for', nominee_2)
            print('Thank you for voting.')
        else:
            print('Sorry your vote has been disqualified.')
    
    else:
        print('You are not registered voter.')
        print('Enter the valid voter id.')
        continue

    if voter_id== []:
        print('Voting session is over.')
        if nm1_votes>nm2_votes:
            percent=(nm1_votes/no_of_voters)*100
            print(nominee_1,'has won the election by', percent, '% of total votes')
            break
        elif nm2_votes>nm1_votes:
            percent=(nm2_votes/no_of_voters)*100
            print(nominee_2,'has won the election' , percent, '% of total votes')
            break
        else:
            print('Both nominees have got the equal vote.')
            break




