from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

users = []
passwordsUsers = []

admins = []
passwordsAdmins = []
locationsAdmins = []
contactAdmins = []
shopNameAdmins = []
ownerNameAdmins = []



@app.get('/')
async def root():
    '''This is just for the HOME PAGE - TEST'''
    return {
        'message': 'hello world'
    }


@app.post('/register-user')
async def registerUser(email: str = Form(), psw: str = Form()):

    ''' registerUser function provides a way for storing of people's IDs and passwords.  '''
    print(f'User is {email} password is {psw}')
    # users.append([email,psw])
    users.append(email)
    passwordsUsers.append(psw)

    # print(users)
    
    return {
        'username': email,
        'password': psw
        # 'pincode': pincode

    }

@app.post('/register-admin')
async def registerAdmin(email: str = Form(), psw: str = Form(),location: str = Form(),
                        shop_name: str = Form(),
                        owner_name: str=Form(),contact: str = Form(),
                                ):

    ''' registerAdmin function provides a way for storing of ADMINS's IDs and passwords.  '''
    print(f'Details: {email} {psw} {shop_name} {owner_name} {contact} {location}')
    # users.append([email,psw])
    admins.append(email)
    passwordsAdmins.append(psw)
    locationsAdmins.append(location)
    contactAdmins.append(contact)
    shopNameAdmins.append(shop_name)
    ownerNameAdmins.append(owner_name)
    # print(users)
    
    return {
        'email': email,
        'password': psw,
        'owner': owner_name,
        'location':location,
        'shop_name':shop_name,
        'owner_name':owner_name,
        'contact':contact
        # 'pincode': pincode

    }



@app.post('/login-user')
async def loginUser(email: str=Form(),psw: str = Form()):
    '''
    LoginUser provides the way for authentication of the person
    '''

    # print
    if (email in users) and (psw in passwordsUsers):
        return {
            'message':'confirmed'
        }
    else:
        return{
            'message':'blocked'
        }


@app.post('/login-admin')
async def loginAdmin(email: str=Form(),psw: str = Form()):
    '''
    LoginAdmin provides the way for authentication of the administrating people
    '''

    # print
    if (email in admins) and (psw in passwordsAdmins):
        return {
            'message':'confirmed'
        }
    else:
        return{
            'message':'blocked'
        }


