global dealer_id
global user_id
global admin_id
import sqlite3
conn = sqlite3.connect("cabsbooking.db")
c = conn.cursor()
def dealer_registration():
    cab_dealer_name = input("Enter the name:-")
    cab_dealer_password = input("Enter the Password:-")
    cab_dealer_email = input("Enter the email:-")
    cab_dealer_phone = input("Enter the phone number:-")
    ins = "insert into cab_dealers(cab_dealer_name,cab_dealer_password,cab_dealer_email,cab_dealer_phone) values('"+cab_dealer_name+"','"+cab_dealer_password+"','"+cab_dealer_email+"','"+cab_dealer_phone+"')"
    c.execute(ins)
    conn.commit()
    print("Dealer created.............")
    init()
def user_registration():
    user_name = input("Enter the name:-")
    user_password = input("Enter the Password:-")
    user_email = input("Enter the email:-")
    user_phone = input("Enter the phone number:-")
    data = c.execute("select * from users where user_email='"+user_email+"'")
    t = len(data.fetchall())
    if(t==0):
        ins = "insert into users(user_name,user_password, user_email,user_phone) values('" + user_name + "','" + user_password + "','" +  user_email + "','" + user_phone + "')"
        c.execute(ins)
        conn.commit()
        print("User created.............")
        init()
    else:
        print("User Email already exit..........")
        user_registration()
def dealer_login():
    global dealer_id
    cab_dealer_name = input("Enter the name:-")
    cab_dealer_password = input("Enter the Password:-")
    data = c.execute("select * from cab_dealers where cab_dealer_name = '"+cab_dealer_name+"' and cab_dealer_password = '"+cab_dealer_password+"'")
    d = data.fetchall()
    for a in d:
        dealer_id = a[0]
    t = len(d)
    if(t==1):
        print("Login successfully")
        init_dealer()
    else:
        print("Invalid Username and Password !")
        dealer_login()
def update_cab():
    global dealer_id
    cab_name = input("Enter the Cab Name :-")
    cab_type = input("Enter the Cab Type :-")
    cab_model = input("Enter the Cab Model :-")
    cab_dealer_id = dealer_id
    cab_from = input("Enter the Cab From :-")
    cab_to = input("Enter the Cab To :-")
    cab_number = input("Enter the Cab number :-")
    cab_id = input("Enter the cab id :-")
    upd = "update cabs set cab_name = '"+cab_name+"',cab_type = '"+cab_type+"',cab_model = '"+cab_model+"',cab_from = '"+cab_from+"',cab_to = '"+cab_to+"',cab_number = '"+cab_number+"' where  cab_id = '"+str(cab_id)+"'"
    c.execute(upd)
    conn.commit()
    print("cab updated successfully..........")
    init_dealer()

def init_dealer():
    global dealer_id
    print(" 1. Add cabs\n 2. View cabs\n 3. Delete cabs\n 4. Update cabs\n 5. Logout")
    dc = int(input("Enter the Dealer Option :-"))
    if (dc == 1):
        add_cab()
    elif (dc == 2):
        display_cab()
    elif (dc == 3):
        del_cab()
    elif (dc == 4):
        update_cab()
    elif (dc == 5):
        del dealer_id
        init()
def add_cab():
    global dealer_id
    cab_name = input("Enter the Cab Name :-")
    cab_type = input("Enter the Cab Type :-")
    cab_model = input("Enter the Cab Model :-")
    cab_dealer_id = dealer_id
    cab_from = input("Enter the Cab From :-")
    cab_to = input("Enter the Cab To :-")
    cab_number = input("Enter the Cab number :-")
    ins = "insert into cabs(cab_name,cab_type,cab_model,cab_dealer_id,cab_from,cab_to,cab_number)values('"+cab_name+"','"+cab_type+"','"+cab_model+"','"+str(cab_dealer_id)+"','"+cab_from+"','"+cab_to+"','"+cab_number+"')"
    c.execute(ins)
    conn.commit()
    print("Cabs created.........")
    init_dealer()
def display_cab():
    global dealer_id
    data = "select c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cab_dealer_name,c.cab_from,c.cab_to,c.cab_number from cabs as c inner join cab_dealers as d on c.cab_dealer_id = d.cab_dealer_id where c.cab_dealer_id ='"+str(dealer_id)+"'"
    cabdata = c.execute(data)
    finalcabdata = cabdata.fetchall()
    print("{0:15}{1:15}{2:15}{3:15}{4:20}{5:15}{6:15}{7:15}".format("Cab_id","Cab Name","Cab type","Cab Model","Cab Dealer Name","Cab From","Cab TO","Cab Number"))
    for d in finalcabdata:
        print("{0:<15}{1:<15}{2:<15}{3:<15}{4:<20}{5:<15}{6:<15}{7:<15}".format(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7]))
    print("\n")
    init_dealer()

def del_cab():
    global dealer_id
    cabid = input("Enter the cab id for Deletion:-")
    del1 = "Delete from cabs where cab_id = '"+cabid+"' and cab_dealer_id = '"+str(dealer_id)+"'"
    c.execute(del1)
    conn.commit()
    print("Data deleted.....")
    display_cab()
def del_cab_by_admin():
    userc = int(input("Enter the choice 1 for deletion 2 for admin menu :-"))
    if userc==1:
        cabid = input("Enter the cab id for Deletion:-")
        del1 = "Delete from cabs where cab_id = '"+cabid+"' "
        c.execute(del1)
        conn.commit()
        print("Data deleted.....")
    else:
        init_admin()
def user_login():
    global user_id
    user_name = input("Enter the name:-")
    user_password = input("Enter the Password:-")
    data = c.execute("select * from users where user_name = '"+user_name+"' and user_password = '"+user_password+"'")
    d = data.fetchall()
    for a in d:
        user_id = a[0]
    t = len(d)
    if(t==1):
        print("Login successfully")
        init_user()
    else:
        print("Invalid Username and Password !")
        user_login()
def display_cab_user(cab_from = '',cab_to = ''):
    if cab_from!="" and cab_to!="":
        data = "select c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cab_dealer_name,c.cab_from,c.cab_to,c.cab_number from cabs as c inner join cab_dealers as d on c.cab_dealer_id = d.cab_dealer_id where cab_from ='"+cab_from+"' and cab_to ='"+cab_to+"'"
    else:
        data = "select c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cab_dealer_name,c.cab_from,c.cab_to,c.cab_number from cabs as c inner join cab_dealers as d on c.cab_dealer_id = d.cab_dealer_id"
    cabdata = c.execute(data)
    finalcabdata = cabdata.fetchall()
    print("{0:15}{1:15}{2:15}{3:15}{4:20}{5:15}{6:15}{7:15}".format("Cab_id", "Cab Name", "Cab type", "Cab Model",
                                                                    "Cab Dealer Name", "Cab From", "Cab TO",
                                                                    "Cab Number"))
    for d in finalcabdata:
        print(
            "{0:<15}{1:<15}{2:<15}{3:<15}{4:<20}{5:<15}{6:<15}{7:<15}".format(d[0], d[1], d[2], d[3], d[4], d[5], d[6],
                                                                              d[7]))
    print("\n")
    init_user()
def user_update():
    global user_id
    user_email = input("Enter the email :-")
    user_phone = input("Enter the Phone Number:-")
    upd = "update users set user_email = '"+user_email+"',user_phone = '"+user_phone+"' where user_id = '"+str(user_id)+"'"
    c.execute(upd)
    conn.commit()
    print("User updated successfully.....")
    init_user()
def change_pass():
    global user_id
    old = input("Enter Old password:-")
    data = c.execute("Select * from users where user_password = '"+old+"' and user_id = '"+str(user_id)+"'")
    d = data.fetchall()
    t = len(d)
    if t==1:
        new_pass = input("Enter the new password:-")
        c_pass = input("Enter the confirm password:-")
        if new_pass == c_pass:
            upd = "update users set user_password = '"+new_pass+"' where user_id = '"+str(user_id)+"'"
            c.execute(upd)
            conn.commit()
            print("Password Updated successfully........")
            init_user()
        else:
            print("New password and confirm password not matching....")
            init_user()
    else:
        print("Invalid Old Password........")
        init_user()
def admin_change_pass():
    global admin_id
    old = input("Enter Old password:-")
    data = c.execute("Select * from admin where admin_password = '" + old + "' and admin_id = '" + str(admin_id) + "'")
    d = data.fetchall()
    t = len(d)
    if t == 1:
        new_pass = input("Enter the new password:-")
        c_pass = input("Enter the confirm password:-")
        if new_pass == c_pass:
            upd = "update admin set admin_password = '" + new_pass + "' where admin_id = '" + str(admin_id) + "'"
            c.execute(upd)
            conn.commit()
            print("Password Updated successfully........")
            init_admin()
        else:
            print("New password and confirm password not matching....")
            init_admin()
    else:
        print("Invalid Old Password........")
        init_admin()

def init_user():
    global user_id
    print(" 1. View all cabs\n 2. search cabs\n 3. Update profile\n 4. Change Password\n 5. Logout")
    userc = int(input("Enter the user choice:-"))
    if userc == 1:
        display_cab_user()
    elif userc == 2:
        cab_from = input("Enter the cab from :-")
        cab_to = input("Enter the cab to :-")
        display_cab_user(cab_from,cab_to)
    elif userc == 3:
        user_update()
    elif userc == 4:
        change_pass()
    elif userc == 5:
        del user_id
        init()
def admin_login():
    global admin_id
    admin_username = input("Enter the name:-")
    admin_password = input("Enter the Password:-")
    data = c.execute(
        "select * from admin where admin_username = '" + admin_username + "' and admin_password = '" + admin_password + "'")
    d = data.fetchall()
    for a in d:
        admin_id = a[0]
    t = len(d)
    if (t == 1):
        print("Login successfully")
        init_admin()
    else:
        print("Invalid Username and Password !")
        admin_login()
def display_user():
    print("{0:^15}{1:^15}{2:^15}{3:^20}".format("User id","User Name","User Email","User Phone"))
    data = "select * from users"
    alldata = c.execute(data)
    fetchall = alldata.fetchall()
    for d in fetchall:
        print("{0:^15}{1:^15}{2:^15}{3:^20}".format(d[0],d[1],d[3],d[4]))
    userc = int(input("\nEnter 1 for  delete user otherwise press 0:-"))
    if userc == 1:
        id = input("Enter the User id :-")
        deldata = "Delete from users where user_id = '"+str(id)+"'"
        c.execute(deldata)
        conn.commit()
        print("User deleted successfully........")
        init_admin()
    else:
        init_admin()
def display_dealer():
    print("{0:^15}{1:^15}{2:^15}{3:^20}".format("Dealer id", "Dealer Name", "Dealer Email", "Dealer Phone"))
    data = "select * from cab_dealers"
    alldata = c.execute(data)
    fetchall = alldata.fetchall()
    for d in fetchall:
        print("{0:^15}{1:^15}{2:^15}{3:^20}".format(d[0], d[1], d[3], d[4]))
    userc = int(input("\nEnter 1 for  delete user otherwise press 0:-"))
    if userc == 1:
        dealer_id = input("Enter the Dealer id :-")
        deldata = "Delete from cab_dealers where cab_dealer_id = '" + str(dealer_id) + "'"
        c.execute(deldata)
        conn.commit()
        print("Dealer deleted successfully........")
        init_admin()
    else:
        init_admin()
def display_cab_admin(cab_from='', cab_to=''):
    if cab_from != "" and cab_to != "":
        data = "select c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cab_dealer_name,c.cab_from,c.cab_to,c.cab_number from cabs as c inner join cab_dealers as d on c.cab_dealer_id = d.cab_dealer_id where cab_from ='" + cab_from + "' and cab_to ='" + cab_to + "'"
    else:
        data = "select c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cab_dealer_name,c.cab_from,c.cab_to,c.cab_number from cabs as c inner join cab_dealers as d on c.cab_dealer_id = d.cab_dealer_id"
        cabdata = c.execute(data)
        finalcabdata = cabdata.fetchall()
        print("{0:15}{1:15}{2:15}{3:15}{4:20}{5:15}{6:15}{7:15}".format("Cab_id", "Cab Name", "Cab type", "Cab Model",
                                                                        "Cab Dealer Name", "Cab From", "Cab TO",
                                                                        "Cab Number"))
        for d in finalcabdata:
            print(
                "{0:<15}{1:<15}{2:<15}{3:<15}{4:<20}{5:<15}{6:<15}{7:<15}".format(d[0], d[1], d[2], d[3], d[4], d[5],
                                                                                  d[6],
                                                                                  d[7]))
        print("\n")
        del_cab_by_admin()
def init_admin():
    global admin_id
    print(' \n 1. View all Users\n 2. View all dealers\n 3. View cabs\n 4. change password\n 5. Logout')
    userc = int(input("Enter the choice :-"))
    if userc == 1:
        display_user()
    elif userc == 2:
        display_dealer()
    elif userc == 3:
        display_cab_admin()
        del_cab_by_admin()
    elif userc == 4:
        admin_change_pass()
    elif userc == 5:
        del admin_id
        init()
def init():
    print(' 1. Dealer Registration\n 2. Dealer Login\n 3. User Registration\n 4. User Login\n 5. Admin Login\n 6.Exit')
    userc = int(input("Enter the choice :-"))
    if userc==1:
        dealer_registration()
    elif userc==2:
        dealer_login()
    elif userc==3:
        user_registration()
    elif userc==4:
        user_login()
    elif userc==5:
        admin_login()
    elif userc==6:
        exit()
init()
