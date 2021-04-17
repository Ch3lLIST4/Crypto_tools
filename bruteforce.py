import itertools
import string
import hashlib

def guess_password(password_hash):
    chars = string.ascii_lowercase + string.digits +string.punctuation
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)

            md5_hash = hashlib.md5(guess.encode()).hexdigest()
            sha1_md5_hash = hashlib.sha1(md5_hash.encode()).hexdigest()
            sha2_md5_hash = hashlib.sha256(sha1_md5_hash.encode()).hexdigest()

            guess_hash = sha2_md5_hash
            if guess_hash == password_hash:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
            # print(guess, attempts)

# ch3lhash = '47b0e210692dbf5267b4e84fde2f37f6de99614e9e0e4c4c7afc540fe7c43cb6'
password = 'c037c03ee627047a85df540c42d59c6b6028841704a7c706feff584a997fd2a3'
print(guess_password(password))
