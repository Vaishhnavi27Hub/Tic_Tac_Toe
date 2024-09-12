a=input().split()
b=input().split()
c=input().split() 
case_1O= (a[0]==b[0]==c[0]=='O' or a[1]==b[1]==c[1]=='O' or a[2]==b[2]==c[2]=='O')
case_2O=(a[0]==a[1]==a[2]=='O' or b[0]==b[1]==b[2]=='O' or c[0]==c[1]==c[2]=='O')
case_3O=(a[0]==b[1]==c[2]=='O' or a[2]==b[1]==c[0]=='O')

case_1X= (a[0]==b[0]==c[0]=='X' or a[1]==b[1]==c[1]=='X' or a[2]==b[2]==c[2]=='X')
case_2X=(a[0]==a[1]==a[2]=='X' or b[0]==b[1]==b[2]=='X' or c[0]==c[1]==c[2]=='X')
case_3X=(a[0]==b[1]==c[2]=='X' or a[2]==b[1]==c[0]=='X') 

if (case_1O or case_2O or case_3O):
    print("Abhinav Wins") 
elif (case_1X or case_2X or case_3X):
    print("Anjali Wins") 
else:
    print("Tie")