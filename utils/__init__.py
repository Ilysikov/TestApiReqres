from utils.random_data import RandomLastName, RandomEmail, RandomMobile, RandomPicture, \
    RandomDatetime, RandomSubjects, RandomStatesCity, RandomHobbies, RandomGender, RandomCurrentAddress, RandomFirstName

first_object = RandomFirstName()
first_name = first_object.my_dict()

las_object = RandomLastName()
las_name = las_object.my_dict()

email_object = RandomEmail()
email_ = email_object.my_dict()

mobile_object = RandomMobile()
mobile_ = mobile_object.my_dict()

picture_object = RandomPicture()
picture_ = picture_object.my_dict()

address_object = RandomCurrentAddress()
address_ = address_object.my_dict()

date_object = RandomDatetime()
date_ = date_object.my_dict()

subject_object = RandomSubjects()
subject_ = subject_object.my_dict()

states_object = RandomStatesCity()
states_ = states_object.my_dict()

hobbies_object = RandomHobbies()
hobbies_ = hobbies_object.my_dict()

gender_object = RandomGender()
gender_ = gender_object.my_dict()
