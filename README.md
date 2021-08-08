# Lab 19 - Automation

*Author*: Kassie Bradshaw

[Link to Pull Request](https://github.com/kassiebradshaw/automation/pull/1)

[Link to My Code](automation/code.py)

---

## Overview

A colleague has abruptly left the team to pursue a career as a novelist. This colleague's last days (and weeks) on the job were a mixed bag in terms of productivity.

Looking through the documents left behind, there is some important contact info in the form of email addresses and phone numbers. Unfortunately, it's mixed in with a bunch of useless notes.

Your job is to find the needles in the haystack.

## Feature Tasks & Requirements

* [x] Given a document `potential-contacts` - find and collect all the email addresses and phone numbers
  * [x] Phone numbers may be in various formats
    * (xxx) yyy-zzzz
    * xxx-yyy-zzzz
    * yyy-zzzz
  * [x] Phone numbers with missing area code should presume 206
  * [x] Phone numbers should be stored in **xxx-yyy-zzzz** format

* [x] Once emails and phone numbers are found they should be stored in two separate documents.
* [x] The information should be sorted in ascending order.
* [x] Duplicate entries are not allowed

phone_numbers.txt

```Python
123-456-7890
206-678-9012
234-567-8901
```

emails.txt

```Python
ana@foo.bar
bill_x@foo.bar
chris.schmidt@bar.baz
```

## Stretch Goals

* [ ] It turns out some of the contacts are already in our system. Compare your collected data against `existing-contacts.txt` and only include info NOT already in the system.

* [ ] Handle phone numbers with extensions
  * Example: (123) 456-7890 x 123

## User Acceptance Tests

* The `phone_numbers.txt` and `emails.txt` files will be verified by an automated system. So make sure to match the naming/formatting requirements exactly.

## Collaboration & Credit
