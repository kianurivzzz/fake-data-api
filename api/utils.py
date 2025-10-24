from time import time, localtime, asctime
from typing import Dict, Any
from faker import Faker


def get_faker_instance(locale: str = 'en_US') -> Faker:
    return Faker(locale)


def add_timestamp(data: Dict[str, Any]) -> Dict[str, Any]:
    timestamp = time()
    datetime = asctime(localtime(timestamp))
    data.update({
        'timestamp': timestamp,
        'datetime': datetime
    })
    return data


def generate_multiple(generator_func, count: int, locale: str = 'en_US'):
    faker = get_faker_instance(locale)
    results = []
    for _ in range(count):
        results.append(generator_func(faker))
    return results


def parse_name(full_name: str) -> Dict[str, str]:
    name_parts = full_name.split()
    if len(name_parts) >= 2:
        first_name = name_parts[0]
        last_name = ' '.join(name_parts[1:])
    else:
        first_name = full_name
        last_name = ''

    return {
        'full_name': full_name,
        'first_name': first_name,
        'last_name': last_name
    }
