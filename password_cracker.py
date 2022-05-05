import hashlib

def crack_sha1_hash(hash, use_salts=False):
  with open('top-10000-passwords.txt', 'r') as passwords:
    for password in passwords:
      password = password.replace('\n', '')
      if use_salts:
        with open('known-salts.txt', 'r') as salts:
          for salt in salts:
            salt = salt.replace('\n', '')
            new_password = salt+password
            
            if hashlib.sha1(new_password.encode()).hexdigest() == hash:
              return new_password.replace(salt, '')

            new_password = password+salt
            
            if hashlib.sha1(new_password.encode()).hexdigest() == hash:
              return new_password.replace(salt, '')
      else:
        if hashlib.sha1(password.encode()).hexdigest() == hash:
          return password

    return 'PASSWORD NOT IN DATABASE'