from django.contrib.auth.models import User
User = User(username='santana')
User.set_password('testing')
User.save
<bound method User.save of <User: santana>>
User.password
u'bcrypt_sha256$$2b$12$yZwe1z8h3kQ9L0k7DPEyq.TA208Qv0xeorbHN6q3PF7e28o1BOcme'


