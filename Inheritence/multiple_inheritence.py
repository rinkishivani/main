class Male:
    m_name = ''
    def is_male(self):
        print(f'{self.m_name} is male')


class Female:
    f_name = ''
    def is_female(self):
        print(f'{self.f_name} is female')


class Person(Male, Female):
    def gender(self):
        print('male ', self.m_name)
        print('female ', self.f_name)


p = Person()
p.m_name = 'rinki'
p.f_name = 'rinki'
p.gender()

