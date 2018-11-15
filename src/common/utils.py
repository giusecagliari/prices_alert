from passlib import pbkdf2_sha512

class Utils(object):

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        checks that the passwd the users sent matches that of the db
        Tje database passwd is encrypted more han the user's passwd at this stage
        :param password: passwd sha512
        :param hashed_password: pbkdf2_sha512 encrypted passwd
        :return: true is passwd match, false otherwise

        """
        return pbkdf2_sha512.verify(password, hashed_password)