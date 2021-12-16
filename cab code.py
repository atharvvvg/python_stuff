"""
cab booking software

you input your departure and arrival location

it shows distance when user inputs locations

then input date and time

it 'll show price based on the petrol price, distance and your choice of vehicle 

also enter coupon: thankyouatharv     
"""

import fontstyle
print(fontstyle.apply("     Welcome to Some Random Cab Service     ", 'bold/italic/white_BG/black/underline/faint'))
print('')

#places where we can start journey
dep = ["Vasant Kunj", "Hauz Khas", "Dwarka", "Connaught Place", "Janakpuri"]
print("From: ")
for i in dep:
    print(i)
    
#input for departure
while True:
    try:
        dep_in=input("Enter pickup location: ")
        if dep_in.lower() == "dwarka" or dep_in.lower()=="vasant kunj" or dep_in.lower()=="connaught place" or dep_in.lower()=="janakpuri":
            print("")
            break
        else:
            print("Please enter a location")
    except ValueError:
        continue


#places where we can stop
arv = dep
print("To: ")
for i in arv:
    print(i)

#input for arrival
while True:
    try:
        arv_in=input("Enter pickup location: ")
        if arv_in.lower() == "dwarka" or arv_in.lower()=="vasant kunj" or arv_in.lower()=="connaught place" or arv_in.lower()=="janakpuri":
            print("")
            break
        else:
            print("Please enter a location")
    except ValueError:
        continue

#distances
b="The distance is: "
d1='9'   #vk to hk
d2='15'   #vk to dwarka
d3='19'   #vk to cp
d4='18'   #vk to janakpuri
da1='20'  #hk to dwarka
da2='11'  #hk to cp
da3='22'  #hk to janakpuri
db1='23'  #dw to cp
db2='12'  #dw to jk
dc1='21'  #cp to jk

if dep_in.lower()=='dwarka' and arv_in.lower()=='vasant kunj' or dep_in.lower()=='vasant kunj' and arv_in.lower()=='dwarka':
    print(b+d2+'km')
elif dep_in.lower()=='hauz khas' and arv_in.lower()=='vasant kunj' or dep_in.lower()=='vasant kunj' and arv_in.lower()=='hauz khas':
    print(b+d1+'km')
elif dep_in.lower()=='connaught place' and arv_in.lower()=='vasant kunj' or dep_in.lower()=='vasant kunj' and arv_in.lower()=='connaught place':
    print(b+d3+'km')
elif dep_in.lower()=='janakpuri' and arv_in.lower()=='vasant kunj' or dep_in.lower()=='vasant kunj' and arv_in.lower()=='janakpuri':
    print(b+d4+'km')

elif dep_in.lower()=='hauz khas' and arv_in.lower()=='dwarka' or dep_in.lower()=='dwarka' and arv_in.lower()=='hauz khas':
    print(b+da1+'km')
elif dep_in.lower()=='hauz khas' and arv_in.lower()=='connaught place' or dep_in.lower()=='connaught place' and arv_in.lower()=='hauz khas':
    print(b+da2+'km')
elif dep_in.lower()=='hauz khas' and arv_in.lower()=='janakpuri' or dep_in.lower()=='janakpuri' and arv_in.lower()=='hauz khas':
    print(b+da3+'km')

elif dep_in.lower()=='dwarka' and arv_in.lower()=='janakpuri' or dep_in.lower()=='janakpuri' and arv_in.lower()=='dwarka':
    print(b+db2+'km')
elif dep_in.lower()=='dwarka' and arv_in.lower()=='connaught place' or dep_in.lower()=='connaught place' and arv_in.lower()=='dwarka':
    print(b+db1+'km')

elif dep_in.lower()=='connaught place' and arv_in.lower()=='janakpuri' or dep_in.lower()=='janakpuri' and arv_in.lower()=='connaught place':
    print(b+dc1+'km')
    
#date and time
prl = 7
d1=int(d1)   #vk to hk
d2=int(d2)   #vk to dwarka
d3=int(d3)   #vk to cp
d4=int(d4)   #vk to janakpuri
da1=int(da1)  #hk to dwarka
da2=int(da2)  #hk to cp
da3=int(da3)  #hk to janakpuri
db1=int(db1)  #dw to cp
db2=int(db2)  #dw to jk
dc1=int(dc1)  #cp to jk

import calendar
yr=int(input("Enter Year: "))   #year
mnth=int(input("Enter Month: "))    #month
print('')
print(calendar.month(yr,mnth))
date=int(input("Select a date from the calendar: "))
time=input("Enter your desired time(24-hour): ")
print('')

#option to choose between AC/non-AC
def ac():
    print("Do you wish to travel in AC or non-AC vehicle?\n1 - AC || 2 - non-AC")
    type= input("")
    if type=='1':
        print('\nYou chose AC cab')   #input yahan
        print('')
        print("The cab will cost you- (in INR)")
        if dep_in.lower()=='dwarka' and arv_in.lower()=='vasant kunj' or dep_in.lower()=='vasant kunj' and arv_in.lower()=='dwarka':
            print(prl*d2+(prl*d2)*20/100+(prl*d2+(prl*d2)*20/100)*5/100+100)
        elif dep_in.lower()=='hauz khas' and arv_in.lower()=='vasant kunj' or dep_in.lower()=='vasant kunj' and arv_in.lower()=='hauz khas':
            print(prl*d1+(prl*d1)*20/100+(prl*d1+(prl*d1)*20/100)*5/100+100)
        elif dep_in.lower()=='connaught place' and arv_in.lower()=='vasant kunj' or dep_in.lower()=='vasant kunj' and arv_in.lower()=='connaught place':
            print(prl*d3+(prl*d3)*20/100+(prl*d3+(prl*d3)*20/100)*5/100+100)
        elif dep_in.lower()=='janakpuri' and arv_in.lower()=='vasant kunj' or dep_in.lower()=='vasant kunj' and arv_in.lower()=='janakpuri':
            print(prl*d4+(prl*d4)*20/100+(prl*d4+(prl*d4)*20/100)*5/100+100)

        elif dep_in.lower()=='hauz khas' and arv_in.lower()=='dwarka' or dep_in.lower()=='dwarka' and arv_in.lower()=='hauz khas':
            print(prl*da1+(prl*da1)*20/100+(prl*da1+(prl*da1)*20/100)*5/100+100)
        elif dep_in.lower()=='hauz khas' and arv_in.lower()=='connaught place' or dep_in.lower()=='connaught place' and arv_in.lower()=='hauz khas':
            print(prl*da2+(prl*da2)*20/100+(prl*da2+(prl*da2)*20/100)*5/100+100)
        elif dep_in.lower()=='hauz khas' and arv_in.lower()=='janakpuri' or dep_in.lower()=='janakpuri' and arv_in.lower()=='hauz khas':
            print(prl*da3+(prl*da3)*20/100+(prl*da3+(prl*da3)*20/100)*5/100+100)

        elif dep_in.lower()=='dwarka' and arv_in.lower()=='janakpuri' or dep_in.lower()=='janakpuri' and arv_in.lower()=='dwarka':
            print(prl*db2+(prl*db2)*20/100+(prl*db2+(prl*db2)*20/100)*5/100+100)
        elif dep_in.lower()=='dwarka' and arv_in.lower()=='connaught place' or dep_in.lower()=='connaught place' and arv_in.lower()=='dwarka':
            print(prl*db1+(prl*db1)*20/100+(prl*db1+(prl*db1)*20/100)*5/100+100)

        elif dep_in.lower()=='connaught place' and arv_in.lower()=='janakpuri' or dep_in.lower()=='janakpuri' and arv_in.lower()=='connaught place':
            print(prl*dc1+(prl*dc1)*20/100+(prl*dc1+(prl*dc1)*20/100)*5/100+100)
    
    elif type=='2':
        print('You chose non-AC cab')
        if dep_in.lower()=='dwarka' and arv_in.lower()=='vasant kunj' or dep_in.lower()=='vasant kunj' and arv_in.lower()=='dwarka':
            print(prl*d2+(prl*d2)*20/100+(prl*d2+(prl*d2)*20/100)*5/100)
        elif dep_in.lower()=='hauz khas' and arv_in.lower()=='vasant kunj' or dep_in.lower()=='vasant kunj' and arv_in.lower()=='hauz khas':
            print(prl*d1+(prl*d1)*20/100+(prl*d1+(prl*d1)*20/100)*5/100)
        elif dep_in.lower()=='connaught place' and arv_in.lower()=='vasant kunj' or dep_in.lower()=='vasant kunj' and arv_in.lower()=='connaught place':
            print(prl*d3+(prl*d3)*20/100+(prl*d3+(prl*d3)*20/100)*5/100)
        elif dep_in.lower()=='janakpuri' and arv_in.lower()=='vasant kunj' or dep_in.lower()=='vasant kunj' and arv_in.lower()=='janakpuri':
            print(prl*d4+(prl*d4)*20/100+(prl*d4+(prl*d4)*20/100)*5/100)

        elif dep_in.lower()=='hauz khas' and arv_in.lower()=='dwarka' or dep_in.lower()=='dwarka' and arv_in.lower()=='hauz khas':
            print(prl*da1+(prl*da1)*20/100+(prl*da1+(prl*da1)*20/100)*5/100)
        elif dep_in.lower()=='hauz khas' and arv_in.lower()=='connaught place' or dep_in.lower()=='connaught place' and arv_in.lower()=='hauz khas':
            print(prl*da2+(prl*da2)*20/100+(prl*da2+(prl*da2)*20/100)*5/100)
        elif dep_in.lower()=='hauz khas' and arv_in.lower()=='janakpuri' or dep_in.lower()=='janakpuri' and arv_in.lower()=='hauz khas':
            print(prl*da3+(prl*da3)*20/100+(prl*da3+(prl*da3)*20/100)*5/100)

        elif dep_in.lower()=='dwarka' and arv_in.lower()=='janakpuri' or dep_in.lower()=='janakpuri' and arv_in.lower()=='dwarka':
            print(prl*db2+(prl*db2)*20/100+(prl*db2+(prl*db2)*20/100)*5/100)
        elif dep_in.lower()=='dwarka' and arv_in.lower()=='connaught place' or dep_in.lower()=='connaught place' and arv_in.lower()=='dwarka':
            print(prl*db1+(prl*db1)*20/100+(prl*db1+(prl*db1)*20/100)*5/100)

        elif dep_in.lower()=='connaught place' and arv_in.lower()=='janakpuri' or dep_in.lower()=='janakpuri' and arv_in.lower()=='connaught place':
            print(prl*dc1+(prl*dc1)*20/100+(prl*dc1+(prl*dc1)*20/100)*5/100)
    else:
        print("Please choose either of the two")
        return ac()
ac()

#coupons
c=str(input("Do you wish to avail coupon? ( if any ):\n     "))
if c.upper()=="THANKYOUATHARV":
    print(fontstyle.apply("\n You appreciate the lord, the saviour Atharv, and you get to ride with 1% off ", 'bold/italic/underline'))
else:
    exit()

print(fontstyle.apply("\nPleased to serve you, but please don't make the driver wait (′◕ᴗ◕‵) \n\n\n\n(⌐■_■)–︻╦╤─  (we also provide hitman services)",'faint'))
    
