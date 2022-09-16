from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

users = []

@app.get('/')
async def root():
    return {
        'message': 'hello world'
    }


@app.post('/register-user')
async def registerUser(email: str = Form(), psw: str = Form()):
                    #    number: str = Form(), address: str = Form(),
                    #    pincode: str = Form()):
    print(f'User is {email} password is {psw}')
    users.append([email,psw])
    
    return {
        'username': email,
        'password': psw
        # 'pincode': pincode

    }


