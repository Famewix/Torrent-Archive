from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

pw = bcrypt.generate_password_hash('White__bilboard1').decode('utf-8')
print(pw)