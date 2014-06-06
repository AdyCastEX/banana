# Hardcoded user credentials for logging in
db_user = {
	1 : {
		'username' : 'admin',
		'password' : 'password'
	},

	2 : {
		'username' : 'foo',
		'password' : 'bar'
	}
}

# Hardcoded input for testing
input_commands = (
    "banana login admin password",
    "banana basecamp add 06/06/14 2.5 'Daenerys Targaryen' 'feed dragons'",
    "banana logout",
)

# Hardcoded error message
error = {
    'error_unknown' : 'Unknown Command.',
    'error_syntax' : 'Syntax Error.',
    'error_already_logged' : 'You are already logged in. Log current account first.',
    'error_login' : 'User does not exsist or username and password is incorrect.',
}

# Hardcoded notif message
notif = {
    'notif_login_success' : 'Login Success',
    'notif_logout_success' : 'You have been successfully logged out.',
}


##########################################################

logged_user = None

##########################################################

# Parses and identifies the command
def parse_command(input):
    tokens = input.split(' ')

    if tokens[0] == "banana":
        
        if tokens[1] == "login":
            login(tokens)
        
        if tokens[1] == "logout":
            logout()

        if tokens[1] == "basecamp":
            pass


#
def logout():

    logged_user = None
    print notif['notif_logout_success']


# checks credentials and login user
def login(tokens):

    global logged_user

    correct_credentials = False

    for user in db_user.items():
        if user[1]['username'] == tokens[2] and user[1]['password'] == tokens[3]:

            correct_credentials = True
            
            if  logged_user is not None:
                print error['error_already_logged']

            elif user[1]['username'] == logged_user:
                print error['error_already_logged']

            else:
                logged_user = user[1]['username']
                print notif['notif_login_success']

    if not correct_credentials:
        print error['error_login']


##########################################################

parse_command(input_commands[0])