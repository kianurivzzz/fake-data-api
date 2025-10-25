<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />
<div align="center">
  <a href="https://github.com/kianurivzzz/fake-data-api">
    <img src="img/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Fake Data API</h3>

  <p align="center">
    A powerful API for generating realistic fake data on demand. Built with FastAPI and Faker.
    <br />
    <a href="https://github.com/kianurivzzz/fake-data-api"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kianurivzzz/fake-data-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/kianurivzzz/fake-data-api/issues">Request Feature</a>
  </p>
</div>

## About The Project

A comprehensive REST API that generates realistic fake data for testing, development, and demonstration purposes. Built with FastAPI and Faker, this API provides multiple endpoints for generating various types of fake data with support for localization and batch generation.

### Features

- **Multiple Data Types**: Names, addresses, emails, phone numbers, companies, URLs, credit cards, and more
- **Localization Support**: Generate data in multiple languages (en_US, ru_RU, fr_FR, etc.)
- **Batch Generation**: Generate multiple records at once with the `count` parameter
- **Rate Limiting**: Built-in rate limiting to prevent abuse
- **CORS Support**: Cross-Origin Resource Sharing enabled
- **Docker Support**: Easy deployment with Docker and Docker Compose
- **Comprehensive Tests**: Full test coverage with pytest
- **CI/CD Pipeline**: Automated testing with GitHub Actions
- **Interactive Documentation**: Auto-generated API docs with Swagger UI

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Installation

### Using Python

1. Clone the repo
   ```sh
   git clone git@github.com:kianurivzzz/fake-data-api.git
   ```

2. Move to project directory
   ```sh
   cd fake-data-api
   ```

3. Install pip packages
   ```sh
   pip3 install -r requirements.txt
   ```

4. Run the server
   ```sh
   python main.py
   ```

### Using Docker

1. Clone the repo
   ```sh
   git clone git@github.com:kianurivzzz/fake-data-api.git
   cd fake-data-api
   ```

2. Build and run with Docker Compose
   ```sh
   docker-compose up -d
   ```

3. Access the API at `http://localhost:8000`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## API Endpoints

### Base URL
```
http://localhost:8000
```

### Available Endpoints

#### `/profile` - Generate Fake Profile
```bash
curl "http://localhost:8000/profile"
curl "http://localhost:8000/profile?count=5&locale=ru_RU"
```

#### `/name` - Generate Fake Name
```bash
curl "http://localhost:8000/name"
curl "http://localhost:8000/name?count=3&locale=en_US"
```

#### `/address` - Generate Fake Address
```bash
curl "http://localhost:8000/address"
curl "http://localhost:8000/address?detailed=true&locale=fr_FR"
```

#### `/email` - Generate Fake Email
```bash
curl "http://localhost:8000/email"
curl "http://localhost:8000/email?count=10"
```

#### `/job` - Generate Fake Job Title
```bash
curl "http://localhost:8000/job"
```

#### `/text` - Generate Fake Text
```bash
curl "http://localhost:8000/text?max_chars=100"
```

#### `/ip` - Generate Fake IP Address
```bash
curl "http://localhost:8000/ip"
curl "http://localhost:8000/ip?ipv6=true"
```

#### `/mac` - Generate Fake MAC Address
```bash
curl "http://localhost:8000/mac"
```

#### `/phone` - Generate Fake Phone Number
```bash
curl "http://localhost:8000/phone?locale=ru_RU"
```

#### `/company` - Generate Fake Company Name
```bash
curl "http://localhost:8000/company"
```

#### `/url` - Generate Fake URL
```bash
curl "http://localhost:8000/url"
```

#### `/credit-card` - Generate Fake Credit Card
```bash
curl "http://localhost:8000/credit-card"
```

#### `/user-agent` - Generate Fake User Agent
```bash
curl "http://localhost:8000/user-agent"
```

#### `/all` - Generate All Data Types
```bash
curl "http://localhost:8000/all"
curl "http://localhost:8000/all?count=2&locale=ru_RU"
```

### Query Parameters

- `count` (integer): Number of records to generate (1-100, default: 1)
- `locale` (string): Locale for data generation (e.g., en_US, ru_RU, fr_FR, default: en_US)
- `detailed` (boolean): Include additional details (address endpoint only)
- `max_chars` (integer): Maximum characters for text (text endpoint only)
- `ipv6` (boolean): Generate IPv6 instead of IPv4 (ip endpoint only)

### Response Format

Single record:
```json
{
  "email": "example@email.com",
  "timestamp": 1634567890.123,
  "datetime": "Mon Oct 18 12:34:50 2021"
}
```

Multiple records:
```json
{
  "data": [
    {"email": "example1@email.com"},
    {"email": "example2@email.com"}
  ],
  "count": 2,
  "timestamp": 1634567890.123,
  "datetime": "Mon Oct 18 12:34:50 2021"
}
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Testing

Run tests with pytest:
```sh
pytest tests/ -v
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Project Structure

```
fake-data-api/
├── api/
│   ├── app.py           # Main FastAPI application
│   ├── models.py        # Pydantic models
│   ├── utils.py         # Utility functions
│   └── middleware.py    # Custom middleware
├── tests/
│   └── test_api.py      # API tests
├── .github/
│   └── workflows/
│       └── ci.yml       # GitHub Actions CI/CD
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose configuration
└── README.md            # This file
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Supported Locales

- `en_US` - English (United States)
- `ru_RU` - Russian (Russia)
- `fr_FR` - French (France)
- `de_DE` - German (Germany)
- `es_ES` - Spanish (Spain)
- `it_IT` - Italian (Italy)
- `ja_JP` - Japanese (Japan)
- `zh_CN` - Chinese (China)
- And many more...

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Nikita Karasyov - [@Nikita_Karasyov](https://t.me/Nikita_Karasyov) – Telegram

Project Link: [https://github.com/kianurivzzz/fake-data-api](https://github.com/kianurivzzz/fake-data-api)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/kianurivzzz/fake-data-api.svg?style=for-the-badge
[contributors-url]: https://github.com/kianurivzzz/fake-data-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kianurivzzz/fake-data-api.svg?style=for-the-badge
[forks-url]: https://github.com/kianurivzzz/fake-data-api/network/members
[stars-shield]: https://img.shields.io/github/stars/kianurivzzz/fake-data-api.svg?style=for-the-badge
[stars-url]: https://github.com/kianurivzzz/fake-data-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/kianurivzzz/fake-data-api.svg?style=for-the-badge
[issues-url]: https://github.com/kianurivzzz/fake-data-api/issues
[license-shield]: https://img.shields.io/github/license/kianurivzzz/fake-data-api.svg?style=for-the-badge
[license-url]: https://github.com/kianurivzzz/fake-data-api/blob/master/LICENSE.txt
