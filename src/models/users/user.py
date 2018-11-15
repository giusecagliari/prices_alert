import uuid

from src.common.database import Database


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

        def __repr__(self):
            return "<User {}".format(self.email)

    @staticmethod
    def is_login_valid(email,password):
        """
        this meth verify and email/passwd combo as sent by site for is valid
        check that the email exist and that passwd associated to that mail is correct

        :param email: the user's email
        :param password: a sha512 hashed passwd
        :return: true if valid, false otherwise
        """
        user_data = Database.find_one("users", {"email": email})
        if user_data is None:
            #tell the user their email doesn't exist
            pass
        if not Utils.check_hashed_password(password, user_data['password']):
            #tell the user that passwd is wrong
            pass
        return True