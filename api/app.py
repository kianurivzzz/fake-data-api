'''
It's a simple API that generates fake data on demand. Created using FastAPI and Faker.
'''

from time import time, localtime, asctime

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from faker import Faker


app = FastAPI(
    title='Fake Data API',
    description='It\'s a simple API that generates fake data on demand. Created using FastAPI and Faker.',
    version='1.0.0'
)

faker = Faker()


# Docs page
@app.get('/')
async def read_root(request: Request):
    return RedirectResponse(f'{request.url}docs')


# Fake profiles
@app.get('/profile')
async def get_fake_profile():
    fake_profile = faker.profile()
    timestamp = time()
    datetime = asctime(localtime(timestamp))
    return {
        'profile': fake_profile,
        'timestamp': timestamp,
        'datetime': datetime
    }


# Fake full names, first names and second names
@app.get('/name')
async def get_fake_name():
    fake_name = faker.name()
    fake_name_split = fake_name.split(' ')
    fake_first_name = fake_name_split[0]
    fake_second_name = fake_name_split[1]
    timestamp = time()
    datetime = asctime(localtime(timestamp))
    return {
        'full_name': fake_name,
        'first_name': fake_first_name,
        'second_name': fake_second_name,
        'timestamp': timestamp,
        'datetime': datetime
        }


# Fake address
@app.get('/address')
async def get_fake_address():
    fake_address = faker.address()
    timestamp = time()
    datetime = asctime(localtime(timestamp))
    return {
        'address': fake_address,
        'timestamp': timestamp,
        'datetime': datetime
    }


# Fake email address
@app.get('/email')
async def get_fake_email():
    fake_email = faker.free_email()
    timestamp = time()
    datetime = asctime(localtime(timestamp))
    return {
        'email': fake_email,
        'timestamp': timestamp,
        'datetime': datetime
    }


# Fake job
@app.get('/job')
async def get_fake_job():
    fake_job = faker.job()
    timestamp = time()
    datetime = asctime(localtime(timestamp))
    return {
        'job': fake_job,
        'timestamp': timestamp,
        'datetime': datetime
    }


# Fake text
@app.get('/text')
async def get_fake_text():
    fake_text = faker.text()
    timestamp = time()
    datetime = asctime(localtime(timestamp))
    return {
        'text': fake_text,
        'timestamp': timestamp,
        'datetime': datetime
    }


# Fake ipv4
@app.get('/ip')
async def get_fake_ipv4():
    fake_ipv4 = faker.ipv4()
    timestamp = time()
    datetime = asctime(localtime(timestamp))
    return {
        'ipv4_address': fake_ipv4,
        'timestamp': timestamp,
        'datetime': datetime
    }


# Fake Mac address
@app.get('/mac')
async def get_fake_mac_address():
    fake_mac_address = faker.mac_address()
    timestamp = time()
    datetime = asctime(localtime(timestamp))
    return {
        'mac_address': fake_mac_address,
        'timestamp': timestamp,
        'datetime': datetime
    }


# Fake all data
@app.get('/all')
async def get_all_fakes():
    fake_profile = faker.profile()
    fake_name = faker.name()
    fake_name_split = fake_name.split(' ')
    fake_first_name = fake_name_split[0]
    fake_second_name = fake_name_split[1]
    fake_address = faker.address()
    fake_email = faker.free_email()
    fake_job = faker.job()
    fake_text = faker.text()
    fake_ipv4 = faker.ipv4()
    fake_mac_address = faker.mac_address()
    timestamp = time()
    datetime = asctime(localtime(timestamp))
    return {
        'profile': fake_profile,
        'full_name': fake_name,
        'first_name': fake_first_name,
        'second_name': fake_second_name,
        'address': fake_address,
        'email': fake_email,
        'job': fake_job,
        'text': fake_text,
        'ipv4': fake_ipv4,
        'mac_address': fake_mac_address,
        'timestamp': timestamp,
        'datetime': datetime
    }
