# პროექტის დასტარტვა

## 1. დაკლონეთ რეპოზიტორია

```
git clone https://github.com/PixelPioners-Technologies/elitcity
```

## 2. ვირტუალური სივრცის გამართვა:

### შექმნა

ვინდოუსზე:

```
python -m venv venv
```

მაკი/ლინუქსი:

```
python3 -m venv venv
```

### აქტივაცია

ვინდოუსზე:

```
venv\Scripts\activate
```

მაკი/ლინუქსი:

```
source venv/bin/activate
```

## 3. პაკეტების ინსტალაცია

```
pip install -r requirements.txt
```

## 4. გაუშვით მიგრაციები

```
python manage.py migrate
```

## 5. შექმენით თქვენი ბრენჩი და იქ იმუშავეთ

```
git checkout -b *ბრენჩის სახელი*
```

- ყოველთვის ამოწმეთ რომელ ბრენჩზე ხართ `git branch` ბრძანებით
- არადროს არ იმუშაოთ main ბრენჩზე, ყოველთვის შექმენით თქვენი ბრენჩი, იქ იმუშავეთ და შემდეგ გამოაგზავნეთ Pull Request-ი
- დაარქვით ბრენჩს სახელი იქიდან გამომდინარე, თუ რა დავალებაზე მუშაობთ
- კომიტებსაც დაარქვით სახელები გარკვევით, რა სამუშაოც შესრულდა ის უნდა ჩანდეს კომიტში მოკლედ
- Pull Request-ის გამოგზავნის დროსაც, გარკვევით, ქართულად აღწერეთ რა გაკეთდა და რა შეცვალეთ

## პროექტის გაშვება

```
python manage.py runserver 0.0.0.0:8000
```

## სუპერიუზერის შექმნა

```
python manage.py createsuperuser
```

# ბექის სერვერის მანიპულაციები

ამ ეტაპისთვის ბექის სერვერი ატვირთულია AWS-ზე.
ეხლანდელი სერვერის საიდუმლო კოდი აირს

### 1. დააკოპირეთ ეს საიდუმლო კოდი

```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAgm1vaOd139ZBnjG6z5cFtKMBNNnTL3nHzV43iFBAC3bn9Pce
OIIAyNZc97AwzTETshh/ngHrkx+/rCeN2GSn8v9jjjw54rjIwUG7Av4uH+lkcBes
UVmypwzjKur8ooevJQSMPZ8OhhqAPjL0RIBycCszF1pU0opdhZ02eXvLLeWxLkm6
4z/269yDSQlO64TRfJYoeJKQwYFmB99SmUTwk9dktSCeFMrQnCNznHZZHdXdFwK/
IwdiEc9xNdZcNrCxNhn3E3c8xhcusA9dXaEhcDwHj7Ui9br+y1cT6X3CJyM8ERdX
WAiETk3d5Hr/zL+mtDj21EDswZMfrCcnwwjtHwIDAQABAoIBADNqRo/5Jot9n9Jn
0jfBVht2YqRd9hVyEWSQ7p1K3WRnlFsKC5zFCuAhOPbfOu24mgYMCErWgPI3gsyv
rwgN7fMp4CoS7dLFe0ZLzhgI8U/dJp3VhzVugbG+r9KcXckIae/S0iH8kLImwkVC
uu5CIFq9fN+I2YVBzEo+xlmvhlHp+J4sqOvPHsY2uuomgJ+DkphXGbtFBTvwgVDT
4Okn8WHJCgHxsaa18ug4ZJBFCFe4o9HzVYKIqiXRJLqA/rUtTvHZwtgCLe1jMXBU
gcKNXe+/wl9NFeHi6Hjpe/brG384mMufTQpkWo3K8fKid73OjerpkAekrBOB1siX
/T2xZgECgYEAxfpmwz20Rud/cXtSzYKCGFNpOeZDX8FvvCVNop+kUOXZzy4VlY0U
o5wMxvY2jE+iovqnVR3+y+Y+//Jn8c4/P21OrI2GvRyh8IgLrRR16XNxtp0/rxwQ
XUeZg5FE7zmEpq/GNzB6ytJeFnuAVcQbIWUT7PRW6X3N1fpk69e8lwECgYEAqKby
lUPcqI/oVHPz5O0vc5wz4KA21Hrf0ZFDdUiVh7txX42bGE0iI3dXQ39/vKqEkJ7o
OhdIxUXhNyuStdqLqZ7F1ZGw+31U83Jm78hH3GMdMbaVd4HJDFDly7cwgZJdv57F
lHhHVM6NoesezwL2O7/vO6pg53fVZadEbjh2pB8CgYEAusbbDlV3b/FVTbXAT7xR
iiufOY2ggIVZKdKzpLoh5mSDEa/zkwzvrM87SrXcjpFO6Z26IlZTHQCS7Rs/r2Qa
TXeNYsN+m4mYyfk/ssF74IwWeudtvoGmeqpjDToPI/ZKzItGYKjvH8xKEcHgOInz
4pSesM1v9YbHm5lIfywgcwECgYAViBLqaZqPTqgbuB4IORvYx7V71RiK8hEHIWOa
YqTsikrEJ0EIzjgwjPjwHiQBw0dfa1o8qGJbBTvmnkKBwyAXjLS3On187hhdaFqp
/EjoYyMECMp2UnSHhQCBjKa9tCER6MRS2zRIKIK+jFUHmtoy8KMrW+o5QvxUmRFM
fRrwgwKBgQCGfhRYunbLlXnyNqlAzwQCq9lss16w2Zpzx3fttbToUPBJwbXrGNLH
L/6/hm0BHfpnTEKkE8JNVo4Izh19GDr66dLu1ZdmnoCwo7kAISB2lcxGzwRKphCI
bXWNyXdBEIcaD8UMWd8DQhldUFiVyn7uLaiCumQ6DQQs0TpuVJT2TA==
-----END RSA PRIVATE KEY-----
```

### 2. და შეინახეთ ფაილში სახელით. შეინახეთ ეს ფაილი თქვენთვის სასურველ ადგილას.

```
privateKey.pem
```

### 3. ტერმინალში აკრიფეთ შემდეგი ბრძანება.
```
chmod 400 privateKey.pem
```

### 4. გახსენით ტერმინალი და გადადით იქ სადაც privateKey.pem ფაილი გაქვთ შენახული. აკრიფეთ შემდეგი ბრძანება:

```
ssh -i privateKey.pem ubuntu@ec2-34-201-93-104.compute-1.amazonaws.com
```

#### ან

```
sudo ssh -i privateKey.pem ubuntu@ec2-34-201-93-104.compute-1.amazonaws.com
```

მიყევით შემდგომ ინსტრუქციას. დასრულებისას თქვენ უნდა აღმოჩნდეთ შემდეგ მისამართზე:

```
ubuntu@ip-172-31-16-199:~$
```

### 5. იმისათვის რომ ნახოთ გაშვებული პროცესები ჩაწერეთ

```
ps aux | grep manage.py
```

### 6. კონკრეტული პროცესების გასათიშად ჩაწერეთ

```
kill -9 <პროცესის ნომერი>
```

### 7. სანამ ჯანგოს სერვერს თავიდან გაუშვებთ აკრიფეთ

```
screen
```

        თუ არ არის დაყენებული აკრიფეთ

        ```
        sudo apt install screen
        ```

სფეის ღილაკზე დაჭრით გადადით ბოლოში და შემდგომ გაუშვით სერვერი.

### 8. ტერმინალიდან გამოსასვლელად რამოდენიმეჯერ დააჭირეტ ctrl+A+D

# როგორ ვიმუშაოვ 2 სხვადასხვა ტიპის ბაზასთან ბექის გაუმჯობესების დროს.

ჯანგოს პროექტში მოცემულია ორი სეთინგის ფაილი settings copy.py და settings.py
settings.py - აქვს პოსტგრესის კონფიგურაცია.
settings copy.py - აქს ესქიულაითის კონფიგურაცია.
ლოკალურად მუშაობისთვის დაგვჭირდება ამ სეთინგების ფაილებისთვის სახელის გადაკეთება ისე რომ რომელი კონფიგურაციაც ჩვენ გვჭირდება, იმ ფაილს ერქვას settings.py
