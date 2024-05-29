from address import Address
from mailing import Mailing

to_address = Address("523028", 'Никольск', 'Новая', '23', 'нет')
from_address = Address('442142', 'Москва', 'Пушкина', '13', '22')
mailing = Mailing(to_address, from_address, 1000, 'Номер1')

print(f'Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},' 
    f'{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartmen} '
    f'в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street},'
    f'{mailing.to_address.house} - {mailing.to_address.apartmen}. Стоимость {mailing.cost} рублей.')