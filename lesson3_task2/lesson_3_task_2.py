from smartphone  import Smartphone

catalog = []
phone1 = Smartphone('Samsung', 'Z fold3 5G', '+79996998989')
phone2 = Smartphone('Apple','iPhone14', '+79895556421')
phone3 = Smartphone('OnePlus', 'Nord3', '+79856664411' )
phone4 = Smartphone('Tecno', 'Pova 6 Pro 5G', '+79273695587')
phone5 = Smartphone('infinix', 'Note 30 Pro', '+79695852424')

catalog.append(phone1)   #добавление каждой вариации девайса в список catalog
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.phone_number}')