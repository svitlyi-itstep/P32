import requests

# Функція для створення нової колоди. Повертає код цієї колоди
def create_new_deck():
    url = f'https://deckofcardsapi.com/api/deck/new/shuffle/'
    response = requests.get(url, params={'deck_count': 1})

    if response.ok:
        return response.json()['deck_id']
    response.raise_for_status()

# Функція для отримання інформації про колоду по її коду
def get_deck(deck_id):
    url = f'https://deckofcardsapi.com/api/deck/{deck_id}/'
    response = requests.get(url)

    if response.ok:
        return response.json()
    response.raise_for_status()

# Витягти вказану кількість карт з колоди. Повертає список у наступному форматі:
# [{'code': '3H', 'value': '3', 'suit': 'HEARTS'}, {'code': '4S', 'value': '4', 'suit': 'SPADES'}]
def draw_cards(deck_id, count):
    url = f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/'
    response = requests.get(url, params={'count': count})

    if response.ok:
        return [
            {
                'code': card['code'],
                'value': card['value'],
                'suit': card['suit'],
             }
            for card in response.json()['cards']]
    response.raise_for_status()

# Виведення карти або списку карт у відформатованому вигляді
def format_card(cards):
    suits = {
        'HEARTS': '♥',
        'DIAMONDS': '♦',
        'CLUBS': '♣',
        'SPADES': '♠',
    }
    if not isinstance(cards, list):
        cards = [cards]

    return ', '.join([f"{card['value'][0]}{suits[card['suit']]}" for card in cards])


deck = create_new_deck()
print(get_deck(deck))
cards = draw_cards(deck, 4)
print(format_card(cards[0]))
print(format_card(cards))

# card = {'code': '3H', 'value': '3', 'suit': 'HEARTS'}
# '3♥'
# card = [{'code': '3H', 'value': '3', 'suit': 'HEARTS'}, {'code': '4S', 'value': '4', 'suit': 'SPADES'}]
# '3♥, 4♠'
# S (Spades ♠), D (Diamonds ♦), C (Clubs ♣), or H (Hearts ♥)
# ♥♦♣♠ ♥♣♦♠