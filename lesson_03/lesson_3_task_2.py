from smartphone import Smartphone

catalog = [
    Smartphone("Xiaom", "POCO C65", "+79522644321"),
    Smartphone("Samsung", "Galaxy S22", "+79515677889"),
    Smartphone("Sony", "Xperia 10", "+79209876543"),
    Smartphone("Apple iPhone", "16 e", "+79001230945"),
    Smartphone("Huawei", "Pura 70", "+79515641415")
]
for Smartphone in catalog:
    print(f"{Smartphone.phone_brand} - {Smartphone.phone_model} -  {Smartphone.subscriber_number}")