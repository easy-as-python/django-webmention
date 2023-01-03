# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0] - 2023-01-03
### Added
- Support for Django 4.0+

### Removed
- Support for Django versions less than 2.2
- Support for Python versions less than 3.7

## [2.0.2] - 2021-02-14
### Fixed
- Store source content as a string rather than a bytes object

## [2.0.1] - 2020-08-25
### Fixed
- Render HTML links in the Django admin by using `format_html` instead of the now-deprecated `allow_tags` attribute

## [2.0.0] - 2020-08-20
### Removed
- Support for Python 3.5

### Added
- Compatibility in the `include_webmention_information` decorator for versions of Django with new-style middleware

## [1.1.0] - 2019-07-22
### Changed
- Use static `setup.cfg` for package metadata and tooling configuration
- Use black code style
- Lint with pyflakes

## [1.0.1] - 2018-04-12
### Fixed
- Made `setup.py` aware that the README content type is, in fact, markdown

## [1.0.0] - 2018-04-12
### Added
- Better documentation about testing
- Coverage configuration

### Changed
- Use markdown for PyPI README

## [0.1.0] - 2018-01-02
### Added
- Mention use of `path()` over `url()` in README
- Mention use of new-style `MIDDLEWARE` over old-style `MIDDLEWARE_CLASSES` in README
- Add system check to detect presence of incorrect middleware configuration
- Update imports and other syntax for forward compatibility with Django 1.10+ and Django 2.0+

## [0.0.4] - 2016-07-15
### Changed
- Reworked the unit tests to be runnable under Travis CI to support continuous integration

## [0.0.3] - 2016-01-22
### Changed
- Successful POST requests will now receive a 202 Accepted response rather than a 200 OK response

### Added
- Django 1.9 in frameworks listed in setup.py

### Fixed
- Errors in documentation

## [0.0.2] - 2015-07-11
### Added
- Webmentions are now available for review in the admin console
- Webmentions are now updated or invalidated when a new webmention notification request is sent
- Thorough unit testing

## [0.0.1] - 2015-07-10
### Added
- Pre-alpha initial release
