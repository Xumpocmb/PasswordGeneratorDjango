import random
import string

from django.shortcuts import render


def index(request):
    context = {
        'title': 'Password Generator',
    }
    return render(request, 'password_generator/index.html', context=context)


def password(request):
    password_length = int(request.GET.get('length', 12))
    add_digits = True if request.GET.get('digits', False) else False
    add_special = True if request.GET.get('special', False) else False

    result = ''

    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)

    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    part1 = round(password_length * (30 / 100))
    part2 = round(password_length * (20 / 100))

    generated_password = []
    if add_digits and add_special:
        for x in range(part1):
            generated_password.append(s1[x])
            generated_password.append(s2[x])

        for x in range(part2):
            generated_password.append(s3[x])
            generated_password.append(s4[x])

        random.shuffle(generated_password)
        result = ''.join(generated_password)

    elif add_digits:
        for x in range(part1):
            generated_password.append(s1[x])
            generated_password.append(s2[x])

        for x in range(part2):
            generated_password.append(s3[x])

        random.shuffle(generated_password)
        result = ''.join(generated_password)

    elif add_special:
        for x in range(part1):
            generated_password.append(s1[x])
            generated_password.append(s2[x])

        for x in range(part2):
            generated_password.append(s4[x])

        random.shuffle(generated_password)
        result = ''.join(generated_password)

    else:
        for x in range(part1):
            generated_password.append(s1[x])
            generated_password.append(s2[x])

        for x in range(part2):
            generated_password.append(s1[x])
            generated_password.append(s2[x])

        random.shuffle(generated_password)
        result = ''.join(generated_password)

    context = {
        'title': 'Password Generator',
        'password': result
    }
    return render(request, 'password_generator/password.html', context=context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'password_generator/about.html', context=context)
