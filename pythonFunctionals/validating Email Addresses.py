def fun(email):
    try:
        username, url = email.split('@')
        websitename, extention = url.split('.')

    except Exception:
        return False

    if not username.replace('-', '').replace('_', '').isalnum():
        return False
    elif not websitename.isalnum():
        return False
    elif len(extention) > 3:
        return False
    else:
        return True


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
