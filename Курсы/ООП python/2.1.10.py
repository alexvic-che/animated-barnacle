from string import ascii_letters, digits
from random import choice
class EmailValidator:

    latters = ascii_letters + "._" + digits

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        email=""
        email_end="@gmail.com"
        for i in range(16):
            email+=choice(cls.latters)
        email+=email_end
        return email

    @classmethod
    def check_email(cls,email):
        if cls.__is_email_str(email):
            dot = ""
            for el in email:
                if el in cls.latters:
                    if el == ".":
                        dot+=el
                        if dot == "..":
                            return False
                    else:
                        dot=""
                    continue
                elif el == "@" and email.count("@") == 1:
                    continue
                else:
                    return False

            lst = email.split("@")
            if len(lst[0])<=100 and len(lst[1])<=50 and "." in lst[1]:
                return True
            else:
                return False

        else:
            return False


    @staticmethod
    def __is_email_str(email):
        if type(email) == str:
            return True
        else:
            return False


print(EmailValidator.check_email('sc_lib@list_ru'))

