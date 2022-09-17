from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

users = []
passwords = []

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
    passwords.append(psw)

    # print(users)
    
    return {
        'username': email,
        'password': psw
        # 'pincode': pincode

    }


@app.post('/login-user')
async def loginUser(email: str=Form(),psw: str = Form()):
    '''
    LoginUser provides the way for authentication of the person
    '''

    # print
    if (email in users) and (psw in passwords):
        return {
            'message':'confirmed'
        }
    else:
        return{
            'message':'blocked'
        }



