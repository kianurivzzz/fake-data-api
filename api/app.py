from fastapi import FastAPI, Request, Query, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from faker import Faker
from typing import Optional, List, Union
import logging

from .models import (
    ProfileResponse, NameResponse, AddressResponse, EmailResponse,
    JobResponse, TextResponse, IPResponse, MACResponse, PhoneResponse,
    CompanyResponse, URLResponse, CreditCardResponse, UserAgentResponse,
    AllDataResponse, BatchResponse
)
from .utils import add_timestamp, get_faker_instance, parse_name
from .middleware import RateLimitMiddleware, LoggingMiddleware

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title='Fake Data API',
    description='A powerful API for generating realistic fake data on demand. Built with FastAPI and Faker.',
    version='2.0.0',
    docs_url='/docs',
    redoc_url='/redoc'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.add_middleware(RateLimitMiddleware, requests_per_minute=100)
app.add_middleware(LoggingMiddleware)


@app.get('/')
async def read_root(request: Request):
    return RedirectResponse(f'{request.url}docs')


@app.get('/profile', response_model=Union[ProfileResponse, BatchResponse])
async def get_fake_profile(
    count: int = Query(1, ge=1, le=100, description="Number of profiles to generate"),
    locale: str = Query('en_US', description="Locale for data generation (e.g., en_US, ru_RU, fr_FR)")
):
    faker = get_faker_instance(locale)

    if count == 1:
        profile = faker.profile()
        return add_timestamp({'profile': profile})

    profiles = [faker.profile() for _ in range(count)]
    return add_timestamp({
        'data': profiles,
        'count': count
    })


@app.get('/name', response_model=Union[NameResponse, BatchResponse])
async def get_fake_name(
    count: int = Query(1, ge=1, le=100, description="Number of names to generate"),
    locale: str = Query('en_US', description="Locale for data generation")
):
    faker = get_faker_instance(locale)

    if count == 1:
        full_name = faker.name()
        name_data = parse_name(full_name)
        return add_timestamp(name_data)

    names = [parse_name(faker.name()) for _ in range(count)]
    return add_timestamp({
        'data': names,
        'count': count
    })


@app.get('/address', response_model=Union[AddressResponse, BatchResponse])
async def get_fake_address(
    count: int = Query(1, ge=1, le=100, description="Number of addresses to generate"),
    locale: str = Query('en_US', description="Locale for data generation"),
    detailed: bool = Query(False, description="Include city, country, and zipcode")
):
    faker = get_faker_instance(locale)

    if count == 1:
        address_data = {'address': faker.address()}
        if detailed:
            address_data.update({
                'city': faker.city(),
                'country': faker.country(),
                'zipcode': faker.zipcode()
            })
        return add_timestamp(address_data)

    addresses = []
    for _ in range(count):
        addr = {'address': faker.address()}
        if detailed:
            addr.update({
                'city': faker.city(),
                'country': faker.country(),
                'zipcode': faker.zipcode()
            })
        addresses.append(addr)

    return add_timestamp({
        'data': addresses,
        'count': count
    })


@app.get('/email', response_model=Union[EmailResponse, BatchResponse])
async def get_fake_email(
    count: int = Query(1, ge=1, le=100, description="Number of emails to generate"),
    locale: str = Query('en_US', description="Locale for data generation")
):
    faker = get_faker_instance(locale)

    if count == 1:
        return add_timestamp({'email': faker.free_email()})

    emails = [{'email': faker.free_email()} for _ in range(count)]
    return add_timestamp({
        'data': emails,
        'count': count
    })


@app.get('/job', response_model=Union[JobResponse, BatchResponse])
async def get_fake_job(
    count: int = Query(1, ge=1, le=100, description="Number of jobs to generate"),
    locale: str = Query('en_US', description="Locale for data generation")
):
    faker = get_faker_instance(locale)

    if count == 1:
        return add_timestamp({'job': faker.job()})

    jobs = [{'job': faker.job()} for _ in range(count)]
    return add_timestamp({
        'data': jobs,
        'count': count
    })


@app.get('/text', response_model=Union[TextResponse, BatchResponse])
async def get_fake_text(
    count: int = Query(1, ge=1, le=100, description="Number of texts to generate"),
    locale: str = Query('en_US', description="Locale for data generation"),
    max_chars: int = Query(200, ge=10, le=5000, description="Maximum number of characters")
):
    faker = get_faker_instance(locale)

    if count == 1:
        return add_timestamp({'text': faker.text(max_nb_chars=max_chars)})

    texts = [{'text': faker.text(max_nb_chars=max_chars)} for _ in range(count)]
    return add_timestamp({
        'data': texts,
        'count': count
    })


@app.get('/ip', response_model=Union[IPResponse, BatchResponse])
async def get_fake_ipv4(
    count: int = Query(1, ge=1, le=100, description="Number of IPs to generate"),
    ipv6: bool = Query(False, description="Generate IPv6 instead of IPv4")
):
    faker = Faker()

    if count == 1:
        ip = faker.ipv6() if ipv6 else faker.ipv4()
        key = 'ipv6_address' if ipv6 else 'ipv4_address'
        return add_timestamp({key: ip})

    ips = []
    for _ in range(count):
        ip = faker.ipv6() if ipv6 else faker.ipv4()
        key = 'ipv6_address' if ipv6 else 'ipv4_address'
        ips.append({key: ip})

    return add_timestamp({
        'data': ips,
        'count': count
    })


@app.get('/mac', response_model=Union[MACResponse, BatchResponse])
async def get_fake_mac_address(
    count: int = Query(1, ge=1, le=100, description="Number of MAC addresses to generate")
):
    faker = Faker()

    if count == 1:
        return add_timestamp({'mac_address': faker.mac_address()})

    macs = [{'mac_address': faker.mac_address()} for _ in range(count)]
    return add_timestamp({
        'data': macs,
        'count': count
    })


@app.get('/phone', response_model=Union[PhoneResponse, BatchResponse])
async def get_fake_phone(
    count: int = Query(1, ge=1, le=100, description="Number of phone numbers to generate"),
    locale: str = Query('en_US', description="Locale for data generation")
):
    faker = get_faker_instance(locale)

    if count == 1:
        return add_timestamp({'phone_number': faker.phone_number()})

    phones = [{'phone_number': faker.phone_number()} for _ in range(count)]
    return add_timestamp({
        'data': phones,
        'count': count
    })


@app.get('/company', response_model=Union[CompanyResponse, BatchResponse])
async def get_fake_company(
    count: int = Query(1, ge=1, le=100, description="Number of companies to generate"),
    locale: str = Query('en_US', description="Locale for data generation")
):
    faker = get_faker_instance(locale)

    if count == 1:
        return add_timestamp({'company': faker.company()})

    companies = [{'company': faker.company()} for _ in range(count)]
    return add_timestamp({
        'data': companies,
        'count': count
    })


@app.get('/url', response_model=Union[URLResponse, BatchResponse])
async def get_fake_url(
    count: int = Query(1, ge=1, le=100, description="Number of URLs to generate")
):
    faker = Faker()

    if count == 1:
        return add_timestamp({'url': faker.url()})

    urls = [{'url': faker.url()} for _ in range(count)]
    return add_timestamp({
        'data': urls,
        'count': count
    })


@app.get('/credit-card', response_model=Union[CreditCardResponse, BatchResponse])
async def get_fake_credit_card(
    count: int = Query(1, ge=1, le=100, description="Number of credit cards to generate")
):
    faker = Faker()

    if count == 1:
        return add_timestamp({
            'provider': faker.credit_card_provider(),
            'number': faker.credit_card_number(),
            'expire': faker.credit_card_expire(),
            'security_code': faker.credit_card_security_code()
        })

    cards = []
    for _ in range(count):
        cards.append({
            'provider': faker.credit_card_provider(),
            'number': faker.credit_card_number(),
            'expire': faker.credit_card_expire(),
            'security_code': faker.credit_card_security_code()
        })

    return add_timestamp({
        'data': cards,
        'count': count
    })


@app.get('/user-agent', response_model=Union[UserAgentResponse, BatchResponse])
async def get_fake_user_agent(
    count: int = Query(1, ge=1, le=100, description="Number of user agents to generate")
):
    faker = Faker()

    if count == 1:
        return add_timestamp({'user_agent': faker.user_agent()})

    user_agents = [{'user_agent': faker.user_agent()} for _ in range(count)]
    return add_timestamp({
        'data': user_agents,
        'count': count
    })


@app.get('/all', response_model=Union[AllDataResponse, BatchResponse])
async def get_all_fakes(
    count: int = Query(1, ge=1, le=50, description="Number of complete datasets to generate"),
    locale: str = Query('en_US', description="Locale for data generation")
):
    faker = get_faker_instance(locale)

    def generate_all_data():
        full_name = faker.name()
        name_data = parse_name(full_name)
        return {
            'profile': faker.profile(),
            'full_name': name_data['full_name'],
            'first_name': name_data['first_name'],
            'last_name': name_data['last_name'],
            'address': faker.address(),
            'email': faker.free_email(),
            'job': faker.job(),
            'text': faker.text(),
            'ipv4': faker.ipv4(),
            'mac_address': faker.mac_address(),
            'phone_number': faker.phone_number(),
            'company': faker.company(),
            'url': faker.url()
        }

    if count == 1:
        return add_timestamp(generate_all_data())

    all_data = [generate_all_data() for _ in range(count)]
    return add_timestamp({
        'data': all_data,
        'count': count
    })


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return {
        'error': exc.detail,
        'status_code': exc.status_code
    }


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return {
        'error': 'Internal server error',
        'status_code': 500
    }
