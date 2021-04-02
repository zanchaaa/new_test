class University:
    def __init__(self, full_name, mathematics, latvian_language, foreign_language):
        self.full_name = full_name
        self.mathematics = mathematics
        self.latvian_language = latvian_language
        self.foreign_language = foreign_language

    def check_point(self):
        if int(self.mathematics) and int(self.latvian_language) and int(self.foreign_language) > 39:
            return True
        else:
            return False
    def generate_report(self, result):
        response_content = f"""
        <h1>{self.full_name} {result} apply to University</h1>
        """
        return response_content